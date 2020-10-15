import logging
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from typing import Any, Dict, Optional

import click
from tqdm import tqdm

from panoramic.cli.companies.client import CompaniesClient
from panoramic.cli.context import get_company_slug
from panoramic.cli.controller import reconcile
from panoramic.cli.diff import echo_diff
from panoramic.cli.errors import (
    InvalidDatasetException,
    InvalidModelException,
    JoinException,
    ValidationError,
)
from panoramic.cli.file_utils import write_yaml
from panoramic.cli.identifier_generator import IdentifierGenerator
from panoramic.cli.join_detector import JoinDetector
from panoramic.cli.local import get_state as get_local_state
from panoramic.cli.local.executor import LocalExecutor
from panoramic.cli.local.writer import FileWriter
from panoramic.cli.pano_model import PanoModel, PanoModelJoin
from panoramic.cli.paths import Paths
from panoramic.cli.physical_data_source.client import PhysicalDataSourceClient
from panoramic.cli.print import echo_error, echo_errors, echo_info
from panoramic.cli.refresh import Refresher
from panoramic.cli.remote import get_state as get_remote_state
from panoramic.cli.remote.executor import RemoteExecutor
from panoramic.cli.scan import Scanner
from panoramic.cli.state import Action, ActionList
from panoramic.cli.validate import (
    validate_config,
    validate_context,
    validate_local_state,
)

logger = logging.getLogger(__name__)


def configure():
    """Global configuration for CLI."""
    client_id = click.prompt('Enter your client id', type=str)
    client_secret = click.prompt('Enter your client secret', hide_input=True, type=str)

    config_file = Paths.config_file()
    if not config_file.parent.exists():
        config_file.parent.mkdir()

    write_yaml(config_file, {'client_id': client_id, 'client_secret': client_secret})


def initialize():
    """Initialize context."""
    client = CompaniesClient()

    try:
        companies = client.get_companies()
    except Exception:
        logger.debug('Failed to fetch available companies', exc_info=True)
        companies = []

    base_text = 'Enter your company slug'
    if len(companies) == 0:
        prompt_text = base_text
    elif len(companies) > 3:
        prompt_text = f'{base_text} (Available - {{{",".join(list(companies)[:3])}}},...)'
    else:
        prompt_text = f'{base_text} (Available - {{{",".join(companies)}}})'

    company_slug = click.prompt(prompt_text, type=str, default=next(iter(companies), None))
    write_yaml(Paths.context_file(), {'company_slug': company_slug, 'api_version': 'v1'})


def list_connections():
    """List available data connections for company from context."""
    client = PhysicalDataSourceClient()

    sources = client.get_sources(get_company_slug())
    if len(sources) == 0:
        echo_error('No data connections have been found')
    else:
        for source in sources:
            echo_info(source['source_name'])


def list_companies():
    """List available companies for user."""
    client = CompaniesClient()
    companies = client.get_companies()
    if len(companies) == 0:
        echo_error('No companies have been found')
    else:
        for company in companies:
            echo_info(company)


def validate() -> bool:
    """Check local files against schema."""
    errors = []

    try:
        validate_config()
    except ValidationError as e:
        errors.append(e)

    try:
        validate_context()
    except ValidationError as e:
        errors.append(e)

    errors.extend(validate_local_state())

    if len(errors) == 0:
        echo_info("Success: All files are valid.")
        return True

    try:
        echo_errors(errors)
    except Exception:
        # Ignore any errors in error reporting
        logger.debug('Error when logging errros', exc_info=True)

    return False


def scan(source_id: str, table_filter: Optional[str], parallel: int = 1, generate_identifiers: bool = False):
    """Scan all metadata for given source and filter."""
    company_slug = get_company_slug()
    scanner = Scanner(company_slug, source_id)
    scanner.fetch_token()

    tables = list(scanner.scan_tables(table_filter=table_filter))

    if len(tables) == 0:
        echo_info('No tables have been found')
        return

    refresher = Refresher(company_slug, source_id)
    refresher.fetch_token()

    if generate_identifiers:
        id_generator = IdentifierGenerator(company_slug, source_id)
        id_generator.fetch_token()

    writer = FileWriter()

    progress_bar = tqdm(total=len(tables))

    def _process_table(table: Dict[str, Any]):
        # drop source name from table name
        table_name = table['data_source'].split('.', 1)[1]

        try:
            refresher.refresh_table(table_name)
            if generate_identifiers:
                identifiers = id_generator.generate(table_name)
            else:
                identifiers = []
            for model in scanner.scan_columns_grouped(table_filter=table_name):
                model.identifiers = identifiers
                writer.write_scanned_model(model)
                progress_bar.write(f'Discovered model {model.model_name}')
        except Exception:
            error_msg = f'Metadata could not be scanned for table {table_name}'
            progress_bar.write(f'Error: {error_msg}')
            logger.debug(error_msg, exc_info=True)
            # Create an empty model file even when scan fails
            writer.write_empty_model(table['model_name'])
        finally:
            progress_bar.update()

    executor = ThreadPoolExecutor(max_workers=parallel)
    for _ in executor.map(_process_table, tables):
        pass

    progress_bar.write(f'Scanned {progress_bar.total} tables')


def pull(yes: bool = False, target_dataset: Optional[str] = None, diff: bool = False):
    """Pull models and data sources from remote."""
    company_slug = get_company_slug()
    echo_info('Loading local state...')
    local_state = get_local_state(target_dataset=target_dataset)
    echo_info('Fetching remote state...')
    remote_state = get_remote_state(company_slug, target_dataset=target_dataset)
    echo_info('Reconciling actions...')
    actions = reconcile(current_state=local_state, desired_state=remote_state)
    echo_info('')  # Add a blank row

    if len(actions.actions) == 0:
        if remote_state.is_empty:
            echo_info('No models have been published')
        else:
            echo_info('Local state is up to date')
        return

    echo_diff(actions)

    if diff:
        # User only wants diff print
        return

    if not yes and not click.confirm('Do you want to proceed?'):
        # User decided not to pull
        return

    executor = LocalExecutor()
    successful = 0
    with tqdm(actions.actions) as bar:
        for action in bar:
            try:
                executor.execute(action)
                successful += 1
            except Exception:
                bar.write(f'Error: Failed to execute action {action.description}')
        bar.write(f'Pulled {successful}/{bar.total} models and datasets')


def push(yes: bool = False, target_dataset: Optional[str] = None, diff: bool = False):
    """Push models and data sources to remote."""
    company_slug = get_company_slug()
    echo_info('Loading local state...')
    local_state = get_local_state(target_dataset=target_dataset)
    echo_info('Fetching remote state...')
    remote_state = get_remote_state(company_slug, target_dataset=target_dataset)
    echo_info('Resolving state...')
    actions = reconcile(remote_state, local_state)
    echo_info('')  # Add a blank row

    if len(actions.actions) == 0:
        if local_state.is_empty:
            echo_info('No models to publish')
        else:
            echo_info('Remote state is up to date')
        return

    echo_diff(actions)

    if diff:
        # User only wants diff print
        return

    if not yes and not click.confirm('Do you want to proceed?'):
        # User decided not to push
        return

    executor = RemoteExecutor(company_slug)
    successful = 0
    with tqdm(actions.actions) as bar:
        for action in bar:
            try:
                executor.execute(action)
                successful += 1
            except (InvalidModelException, InvalidDatasetException) as e:
                messages_concat = '\n  '.join(e.messages)
                bar.write(f'Error: Failed to execute action {action.description}:\n  {messages_concat}')
            except Exception as e:
                bar.write(f'Error: Failed to execute action {action.description}:\n  {str(e)}')
        bar.write(f'Updated {successful}/{bar.total} models and datasets')


def detect_joins(target_dataset: Optional[str] = None, diff: bool = False, overwrite: bool = False, yes: bool = False):
    company_slug = get_company_slug()
    echo_info('Loading local state...')
    local_state = get_local_state(target_dataset=target_dataset)

    if local_state.is_empty:
        echo_info('No datasets to detect joins on')

    join_detector = JoinDetector(company_slug=company_slug)
    join_detector.fetch_token()

    models_by_virtual_data_source: Dict[Optional[str], Dict[str, PanoModel]] = defaultdict(dict)
    for model in local_state.models:
        # Prepare a mapping for a quick access when reconciling necessary changes later
        models_by_virtual_data_source[model.virtual_data_source][model.model_name] = model

    actions_list = ActionList(actions=[])

    with tqdm(list(local_state.data_sources)) as bar:
        for dataset in bar:
            try:
                bar.write(f'Detecting joins for dataset {dataset.dataset_slug}')
                joins_by_model = join_detector.detect(dataset.dataset_slug)

                for model_name, joins in joins_by_model.items():
                    if not joins:
                        bar.write(f'No joins detected for {model_name} under dataset {dataset.dataset_slug}')
                        continue

                    bar.write(f'Detected {len(joins)} joins for {model_name} under dataset {dataset.dataset_slug}')

                    detected_join_objects = [PanoModelJoin.from_dict(join_dict) for join_dict in joins]
                    current_model = models_by_virtual_data_source[dataset.dataset_slug][model_name]
                    desired_model = deepcopy(current_model)

                    if overwrite:
                        desired_model.joins = detected_join_objects
                    else:
                        for detected_join in detected_join_objects:
                            # Only append joins that are not already defined
                            if detected_join not in current_model.joins:
                                desired_model.joins.append(detected_join)

                    actions_list.actions.append(Action(current=current_model, desired=desired_model))

            except JoinException as join_exception:
                bar.write(f'Error: {str(join_exception)}')
                logger.debug(str(join_exception), exc_info=True)
            except Exception:
                error_msg = f'An unexpected error occured when detecting joins for {dataset.dataset_slug}'
                bar.write(f'Error: {error_msg}')
                logger.debug(error_msg, exc_info=True)
            finally:
                bar.update()

    if actions_list.is_empty:
        echo_info('No joins detected')
        return

    echo_diff(actions_list)
    if diff:
        # User decided to see the diff only
        return

    if not yes and not click.confirm('Do you want to proceed?'):
        # User decided not to update local models based on join suggestions
        return

    echo_info('Updating local state...')

    executor = LocalExecutor()
    updated_count = 0
    for action in actions_list.actions:
        try:
            executor.execute(action)
            updated_count += 1
        except Exception:
            echo_error(f'Error: Failed to execute action {action.description}')
        echo_info(f'Updated {updated_count}/{actions_list.count} models')
