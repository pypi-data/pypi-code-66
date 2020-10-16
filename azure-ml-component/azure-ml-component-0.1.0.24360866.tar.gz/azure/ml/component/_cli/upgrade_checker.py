# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import requests
import logging
import os

from _thread import start_new_thread
from functools import wraps, reduce
from multiprocessing import Queue

try:
    from azure.cli.core.extension import get_extension
except ImportError:
    from azure.cli.core.extensions import get_extension


# This file is only used in CLI, hard code the logger name start with 'cli.'
# The logger name starts with 'cli.' to make use of the log handlers and formatters of azure-cli.
# Otherwise the 'info' and 'warning' messages will not be shown in the terminal in the CLI,
# which is unexpected.
cli_logger = logging.getLogger('cli.upgrade_checker')


PIP_JSON_URL = 'https://aka.ms/local-module-cli-versions'
AZURE_CLI_EXT_URL = 'https://azurecliextensionsync.blob.core.windows.net/index1/index.json'


def greater_version(v1, v2):
    v1_split = v1.split('.')
    v2_split = v2.split('.')
    for i in range(min(len(v1_split), len(v2_split))):
        version_part_v1, version_part_v2 = int(v1_split[i]), int(v2_split[i])
        if version_part_v1 > version_part_v2:
            return v1
        if version_part_v1 < version_part_v2:
            return v2
    # If all version parts are the same but v1 is longer than v2, v1 is greater than v2.
    return v1 if len(v1_split) > len(v2_split) else v2


def get_latest_version_from_url(url, versions_loader: callable):
    resp = requests.get(url)
    if resp.status_code != 200:
        return
    data = resp.json()
    versions = versions_loader(data)
    return reduce(greater_version, versions)


def load_versions_from_pip_data(data):
    return data['releases']


def get_latest_version_from_pip():
    return get_latest_version_from_url(PIP_JSON_URL, load_versions_from_pip_data)


def load_versions_from_azure_cli_ext_data(data):
    return (release['metadata']['version'] for release in data['extensions']['azure-cli-ml'])


def get_latest_version_from_azure_cli_ext():
    return get_latest_version_from_url(AZURE_CLI_EXT_URL, load_versions_from_azure_cli_ext_data)


def put_latest_version_to_queue(result_queue: Queue, get_latest_version: callable):
    try:
        result_queue.put(get_latest_version())
    except BaseException as e:
        cli_logger.warning("Exception occurs when getting the latest version of module-cli, exception='{}'.".format(e))


def check_upgrade(func):
    """This decorator checks if there's a new version of the azure-cli-ml.
    If new version detected, show a warning message to the CLI to guide the user to upgrade to new version."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_queue = Queue(1)
        if not os.environ.get('SKIP_CLI_MODULE_VERSION_CHECK'):
            # Note: the following code will fail in dev_setup env if 'azure-cli-ml' not installed.
            version = get_extension('azure-cli-ml').version
            # If the version is 0.1.0.x, it is an internal version which is published to pip,
            # otherwise it is a public version in azure-cli
            get_latest_version_func = get_latest_version_from_pip \
                if version.startswith('0.1.0') else get_latest_version_from_azure_cli_ext
            # Start another thread to get the latest version.
            start_new_thread(put_latest_version_to_queue, (result_queue, get_latest_version_func))
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Wrap any exceptions as ModuleCliError for better error message display
            # TODO: change this logic to a specific decorator.
            from .utils import ModuleCliError
            if isinstance(e, ModuleCliError):
                raise e
            raise ModuleCliError(e) from e
        finally:
            # If the latest version is ready, we check whether we are the latest version.
            if not result_queue.empty():
                latest_version = result_queue.get()
                if greater_version(latest_version, version) != version:
                    cli_logger.warning("New version of module-cli detected. "
                                       "Please upgrade module-cli following the guidelines: "
                                       "https://aka.ms/module-cli-walk-through.")
    wrapper.unwrapped = func
    return wrapper
