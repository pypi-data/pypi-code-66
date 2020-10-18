# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains functionality for creating and managing modules in Azure Machine Learning."""

import os
import tempfile
import zipfile
import ruamel
import ntpath
import posixpath
import logging

from shutil import copy2, copytree
from enum import Enum
from pathlib import Path

from azureml.exceptions import UserErrorException
from azureml._project.ignore_file import get_project_ignore_file, IgnoreFile
from azureml._base_sdk_common.cli_wrapper._common import get_default_property

from azure.ml.component._cli.status_indicator import status_indicator
from azure.ml.module._restclient.module_client import ModuleClient, BaseHttpClient


class ModuleWorkingMechanism(Enum):
    Normal = 'Normal'
    OutputToDataset = 'OutputToDataset'


class ModuleSourceType(Enum):
    Local = 'Local'
    GithubFile = 'GithubFile'
    GithubFolder = 'GithubFolder'
    DevopsArtifacts = 'DevopsArtifactsZip'


class ModuleSource:
    def __init__(
        self,
        source_type: ModuleSourceType,
        spec_file: str = None,
        package_zip: str = None,
        snapshot=None,
    ):
        self._source_type = source_type
        self._spec_file = spec_file
        self._package_zip = package_zip
        self._snapshot = snapshot

    @property
    def source_type(self):
        return self._source_type

    def is_local_source(self):
        return self._source_type == ModuleSourceType.Local

    @property
    def spec_file(self):
        return self._spec_file

    @property
    def package_zip(self):
        return self._package_zip

    @property
    def snapshot(self):
        return self._snapshot

    def is_invalid_entry(self, entry_file):
        # We only check whether the entry file for local source, since we don't download snapshot for remote sources.
        if not self.is_local_source():
            return False

        # We don't check absolute path because it might be in the docker image which we are not able to check.
        if self.is_absolute(entry_file):
            return False

        # If the entry file cannot be found in snapshot, it is invalid.
        return not self.snapshot.file_exists(relative_path=entry_file)

    @staticmethod
    def is_absolute(file_path):
        # Here we don't use Path(file).is_absolute because it can only handle the case in current OS,
        # but in our scenario, we may run this code in Windows, but need to check whether the path is posix absolute.
        return posixpath.isabs(file_path) or ntpath.isabs(file_path)


class _DictBased:
    """A base class to enable a class retrieving its properties from a dict."""

    def __init__(self, dct):
        self._dct = dct

    def _get(self, path, default=None):
        return self._dct.get(path, default)

    @property
    def dct(self):
        return self._dct


class Version(_DictBased):

    @property
    def version_id(self):
        return self._get('moduleVersionId')

    @property
    def name(self):
        return self._get('version')


class Module(_DictBased):
    """Defines a module in a worksapce."""
    SOURCE_NAMES = {
        '1': 'Local files',
        '2': 'Github repo',
        '4': 'Azure DevOps artifacts',
    }
    UNKNOWN_SOURCE_NAME = 'Unknown'

    SCOPE_NAMES = {
        '1': 'Global',
        '2': 'Workspace',
        '3': 'Anonymous',
    }
    UNKNOWN_SCOPE_NAME = 'Unknown'

    STATUS_NAMES = {'0': 'Active', '1': 'Deprecated', '2': 'Disabled'}
    UNKNOWN_STATUS_NAME = 'Unknown'

    @property
    def name(self):
        """The name of the module."""
        return self._get('moduleName')

    @property
    def namespace(self):
        """The namespace of the module."""
        return self._get('namespace')

    @property
    def id(self):
        """The id of the module."""
        return self._get('moduleVersionId')

    @property
    def version(self):
        """The version of the module."""
        return self._get('moduleVersion')

    @property
    def default_version(self):
        """The default version of the module."""
        return self._get('defaultVersion')

    @property
    def versions(self):
        """The list of history versions of the module."""
        versions = self._get('versions')
        return [Version(v).name for v in versions] if versions else []

    @property
    def all_versions(self):
        def iter_versions():
            for v in self.versions:
                yield v + ' (Default)' if v == self.default_version else v

        return ', '.join(iter_versions())

    @property
    def type(self):
        """The type of the module."""
        return self._get('jobType')

    @property
    def description(self):
        """The description of the module."""
        return self._get('description')

    @property
    def contact(self):
        """The contact of the module's author."""
        return self._get('owner')

    @property
    def source(self):
        """The source of the module."""
        # rest client will parse int value to str, so use str as key
        raw_value = str(self._get('moduleSourceType'))
        return self.SOURCE_NAMES.get(raw_value, self.UNKNOWN_SOURCE_NAME)

    @property
    def usage(self):
        """The usage of the module"""
        return self._get('usage')

    @property
    def is_builtin_module(self):
        """Whether is a built-in module in AzureML Designer."""
        return self.namespace == 'azureml'

    @property
    def tags(self):
        """Tags of the module."""
        return self._get('tags')

    @property
    def shared_scope(self):
        """The scope of the module."""
        # rest client will parse int value to str, so use str as key
        raw_value = str(self._get('moduleScope'))
        return self.SCOPE_NAMES.get(raw_value, self.UNKNOWN_SCOPE_NAME)

    @property
    def help_document(self):
        """Link to help document."""
        return self._get('helpDocument')

    @property
    def created_date(self):
        """The date the module was created."""
        return self._get('createdDate')

    @property
    def last_modified_date(self):
        """The date the module last modified."""
        return self._get('lastModifiedDate')

    @property
    def registered_by(self):
        """The user/app name who registered the module."""
        return self._get('registeredBy')

    @property
    def status(self):
        """The status of the module."""
        # rest client will parse int value to str, so use str as key
        code = str(self._get('entityStatus'))
        return self.STATUS_NAMES.get(code, self.UNKNOWN_STATUS_NAME)

    @property
    def yaml_link(self):
        """The relative link of the module spec path in the snapshot."""
        return self._get('yamlLink')

    @property
    def last_updated_on(self):
        return self._get('lastModifiedDate')

    def __str__(self):
        """Format Module data into a string.

        :return:
        :rtype: str
        """
        return "Module({name})@v{version}".format(name=self.name, version=self.version)

    @staticmethod
    def list(workspace, include_disabled=False, logger=None):
        """Return a list of modules in the workspace.

        :param workspace: The workspace from which to list modules.
        :type workspace: azureml.core.workspace.Workspace
        :param include_disabled: Include disabled modules in list result
        :return: A list of module objects.
        :rtype: builtin.list[azureml.core.Module]
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.list_modules(include_disabled=include_disabled)
        return [Module(m) for m in result]

    @staticmethod
    def get(workspace, name, namespace=None, version=None, logger=None):
        """Return the module object.

        :param workspace: The workspace that contains the module.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the module to return.
        :type name: str
        :param namespace: The namespace of the module to return.
        :type namespace: str
        :param version: The version of the module to return.
        :type version: str
        :return: The module object.
        :rtype: azureml.core._module.Module
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.get_module(module_name=name, namespace=namespace, version=version)
        return Module(result)

    @staticmethod
    def register(workspace, module_source, set_as_default_version=True, overwrite_module_version=None, logger=None):
        """Register the module object to workspace.

        :param workspace: The workspace
        :type workspace: azureml.core.workspace.Workspace
        :param module_source: Describes where and how to get the module data to be registed.
        :type module_source: ModuleSource
        :param set_as_default_version: Whether to update the default version.
        :type set_as_default_version: A hook for tracking progress.
        :param overwrite_module_version: If specified, registered module will use specified value as version
                                            instead of the version in the yaml.
        :type overwrite_module_version: str
        :return: Returns the module object
        :rtype: azureml.core._module.Module
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.create_or_upgrade_module(module_source=module_source, set_as_default=set_as_default_version,
                                                 overwrite_module_version=overwrite_module_version)
        return Module(result)

    @staticmethod
    def validate(workspace, module_source, logger=None):
        """Validate a module.

        :param workspace: The workspace that contains the module.
        :type workspace: azureml.core.workspace.Workspace
        :param module_source: Describes where and how to get the module data to be registed.
        :type module_source: ModuleSource
        :return: The updated module object.
        :rtype: azureml.core._module.Module
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.validate_module(module_source)
        return Module(result)

    @staticmethod
    def enable(workspace, name, namespace=None, logger=None):
        """Enable a module.

        :param workspace: The workspace that contains the module.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the module.
        :type name: str
        :param namespace: The namespace of the module.
        :type namespace: str
        :return: The updated module object.
        :rtype: azureml.core._module.Module
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.enable_module(module_name=name, namespace=namespace)
        return Module(result)

    @staticmethod
    def disable(workspace, name, namespace=None, logger=None):
        """Disable a module.

        :param workspace: The workspace that contains the module.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the module.
        :type name: str
        :param namespace: The namespace of the module.
        :type namespace: str
        :return: The updated module object.
        :rtype: azureml.core._module.Module
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.disable_module(module_name=name, namespace=namespace)
        return Module(result)

    @staticmethod
    def set_default_version(workspace, name, version, namespace=None, logger=None):
        """Set a module's default version.

        :param workspace: The workspace that contains the module.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the module.
        :type name: str
        :param version: The version to be set as default.
        :type name: str
        :param namespace: The namespace of the module.
        :type namespace: str
        :return: The updated module object.
        :rtype: azureml.core._module.Module
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.set_module_default_version(module_name=name, namespace=namespace, version=version)
        return Module(result)

    @staticmethod
    def get_snapshot_url(workspace, name, namespace=None, version=None, logger=None):
        """Get a module snapshot download url.

        :param workspace: The workspace that contains the module.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the module.
        :type name: str
        :param namespace: The namespace of the module.
        :type namespace: str
        :param version: The version of the module.
        :type version: str
        :return: The module snapshot url.
        :rtype: dict
        """
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.get_snapshot_url(module_name=name, namespace=namespace, version=version)
        return {'url': result}

    @staticmethod
    def get_module_yaml(workspace, name, namespace=None, version=None, logger=None):
        client = ModuleClient(workspace.service_context, parent_logger=logger)
        result = client.get_module_yaml(module_name=name, namespace=namespace, version=version)
        return result

    @staticmethod
    def download(workspace, name, namespace=None, version=None, target_dir=None, overwrite=False,
                 include_module_spec=False, logger=None):
        """Download a module to a local folder.

        :param workspace: The workspace that contains the module.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the module.
        :type name: str
        :param namespace: The namespace of the module.
        :type name: str
        :param version: The version of the module.
        :type version: str
        :param target_dir: The directory which you download to.
        :type version: str
        :param overwrite: Set true to overwrite any exist files, otherwise false.
        :type overwrite: bool
        :param include_module_spec: Set true to download module spec file along with the snapshot.
        :type include_module_spec: bool
        :return: The module file path.
        :rtype: dict
        """
        base_filename = "{0}-{1}-{2}-{3}".format(
            workspace.service_context.workspace_name,
            name,
            namespace,
            version or 'default',
        )

        file_path = {}

        if include_module_spec:
            # download module spec
            module_yaml = Module.get_module_yaml(workspace, name, namespace, version, logger=logger)
            module_spec_file_name = _write_file_to_local(module_yaml, target_dir=target_dir,
                                                         file_name=base_filename + ".yaml", overwrite=overwrite,
                                                         logger=logger)
            file_path['module_spec'] = module_spec_file_name

        # download snapshot
        snapshot_info = Module.get_snapshot_url(workspace, name, namespace, version, logger=logger)
        snapshot_filename = _download_file_to_local(snapshot_info.get('url'), target_dir=target_dir,
                                                    file_name=base_filename + ".zip", overwrite=overwrite,
                                                    logger=logger)
        file_path['snapshot'] = snapshot_filename

        return file_path


class SnapshotItem:
    def __init__(self, absolute_path, *, relative_path_in_snapshot=None):
        self._absolute_path = absolute_path.resolve()

        # This check can NOT be removed.
        # Since the incoming absolute_path might be a symbol link pointing to the parent folder
        # of itself, which will cause infinite length of file paths.
        # Calling `absolute_path.exists()` to raise "OSError: Too many levels of symbol links"
        # to the user for this case.
        if not absolute_path.exists():
            raise FileNotFoundError("File not found: {}".format(absolute_path))

        if not relative_path_in_snapshot:
            raise ValueError("relative_path_in_snapshot must be specified.")
        self._relative_path = Path(relative_path_in_snapshot)

    @property
    def absolute_path(self):
        return self._absolute_path

    @property
    def relative_path(self):
        result = str(self._relative_path.as_posix())
        if self._absolute_path.is_dir():
            result += '/'
        return result

    def __repr__(self):
        return self.relative_path


class ModuleSnapshot:
    """Manage the snapshot of a module."""

    _DEFAULT_AMLIGNORE_FILE_CONFIG_KEY = 'module_amlignore_file'

    def __init__(self, spec_file_path, additional_amlignore_file=None, logger=None):
        # Do the path resolve otherwise when the the spec_file_path is like 'module_spec.yaml'
        # which does not contain the parent paths, the `spec_file_path.parent` will be `.`
        # and result in the wrong folder structure of the created snapshot folder structure.
        self._spec_file_path = Path(spec_file_path).resolve()
        self._snapshot_folder = None

        if not additional_amlignore_file:
            additional_amlignore_file = get_default_property(self._DEFAULT_AMLIGNORE_FILE_CONFIG_KEY)
        self._additional_amlignore_file = \
            Path(additional_amlignore_file).resolve() if additional_amlignore_file else None

        if self._additional_amlignore_file:
            if not self._additional_amlignore_file.is_file():
                raise UserErrorException(
                    'The specified amlignore file: {0} does not exist.'.format(self._additional_amlignore_file))

        try:
            with open(spec_file_path, 'r') as f:
                self._spec_dict = ruamel.yaml.safe_load(f)
        except Exception as e:
            raise UserErrorException('Failed to load spec file {0}.\nException: \n{1}'.format(spec_file_path, e))

        if not logger:
            self.logger = logging.getLogger('snapshot')

        self._check_additional_includes()

    @property
    def base_path(self):
        """The base folder path of the snapshot."""
        # First, go to the folder that contains the spec file
        path = self._spec_file_path.parent

        # Then, if sourceDirectory specified in the module spec, apply as relative directory.
        if self.source_directory:
            path = path / self.source_directory
            if path.resolve() not in self._spec_file_path.parents:
                raise UserErrorException(
                    "Invalid sourceDirectory '{}': "
                    "Source directory must be the parent folders of the module yaml spec file. "
                    "Please refer to https://aka.ms/module-source-directory for details.".format(self.source_directory)
                )

        # Finally, resolve the path and return.
        return path.resolve()

    @property
    def source_directory(self):
        return try_to_get_value_from_multiple_key_paths(
            dct=self._spec_dict,
            key_path_list=[
                'implementation/container/sourceDirectory',
                'implementation/parallel/sourceDirectory',
                'implementation/hdinsight/sourceDirectory',
            ]
        )

    @property
    def spec_file_relative_path(self):
        return self._spec_file_path.relative_to(self.base_path.resolve())

    @property
    def conda_file_relative_path(self):
        return try_to_get_value_from_multiple_key_paths(
            dct=self._spec_dict,
            key_path_list=[
                'implementation/container/amlEnvironment/python/condaDependenciesFile',
                'implementation/parallel/amlEnvironment/python/condaDependenciesFile',
            ]
        )

    @property
    def pip_file_relative_path(self):
        return try_to_get_value_from_multiple_key_paths(
            dct=self._spec_dict,
            key_path_list=[
                'implementation/container/amlEnvironment/python/pipRequirementsFile',
                'implementation/parallel/amlEnvironment/python/pipRequirementsFile',
            ]
        )

    @property
    def conda_file(self):
        """The conda file path of the module (if any)."""
        return self.get_file_or_raise(self.conda_file_relative_path, 'conda')

    @property
    def pip_file(self):
        return self.get_file_or_raise(self.pip_file_relative_path, 'pip requirement')

    def get_file_or_raise(self, relative_path, name):
        if relative_path:
            conda_file_path = self.base_path / relative_path
            if os.path.isfile(conda_file_path):
                return conda_file_path
            else:
                raise UserErrorException('Can not find {0} file: {1}.'.format(name, relative_path))

        return None

    @status_indicator('Packing')
    def create_snapshot(self):
        return self._make_zipfile(snapshot_items_iterator=self._iter_files())

    @status_indicator('Packing')
    def create_snapshot_legacy(self):
        snapshot_folder = self._get_snapshot_folder()
        return self._make_snapshot(snapshot_folder)

    def create_spec_snapshot(self):
        def file_iterator():
            yield SnapshotItem(self._spec_file_path, relative_path_in_snapshot=self.spec_file_relative_path)
            if self.conda_file:
                yield SnapshotItem(self.conda_file, relative_path_in_snapshot=self.conda_file_relative_path)
            if self.pip_file:
                yield SnapshotItem(self.pip_file, relative_path_in_snapshot=self.pip_file_relative_path)
        return self._make_zipfile(snapshot_items_iterator=file_iterator())

    def create_spec_snapshot_legacy(self):
        temp_directory = Path(tempfile.mkdtemp())
        self._copy_to(self._spec_file_path, temp_directory)
        if self.conda_file:
            self._copy_to(self.conda_file, temp_directory)
        return self._make_snapshot(temp_directory)

    def file_exists(self, relative_path):
        """Detect whether a given path exists in the snapshot."""
        if relative_path:
            # First, check snapshot folder
            if (self.base_path / relative_path).is_file():
                return True

            # If not found in snapshot folder, try to find in additional includes
            include_name = Path(relative_path).parts[0]
            for inc in self.additional_includes:
                if Path(inc).name == include_name:
                    full_path = (self.base_path / inc).parent / relative_path
                    if full_path.is_file():
                        return True

            # TODO: handle the case that the file is listed in ignore files.

        # Otherwise, not found
        return False

    def file_exists_legacy(self, relative_path):
        """Detect whether a given path exists in the snapshot."""
        if relative_path:
            if (self.base_path / relative_path).is_file() or (self._get_snapshot_folder() / relative_path).is_file():
                return True
        return False

    @property
    def additional_amlignore_file(self):
        return self._additional_amlignore_file

    def _make_amlignore(self, snapshot_folder):
        if not self.additional_amlignore_file:
            return

        if not self._additional_amlignore_file.is_file():
            raise UserErrorException('The specified amlignore file: {0} is invalid.'
                                     .format(self._additional_amlignore_file))

        # Copy specified .amlignore to snapshot folder if there is not existing one in base folder
        merged_amlignore_file = snapshot_folder / '.amlignore'
        if not merged_amlignore_file.exists():
            self._copy_to(self.additional_amlignore_file, merged_amlignore_file)

        # Append content of specified .amlignore to ignore file in base folder if it exists
        elif merged_amlignore_file.is_file():
            with open(merged_amlignore_file, 'a') as fout, open(self.additional_amlignore_file, 'r') as fin:
                fout.write('\n\n# Additional ignore\n')
                for line in fin:
                    fout.write(line)
                self.logger.debug("Append content of {0} to {1}"
                                  .format(self.additional_amlignore_file, merged_amlignore_file))

        else:
            raise UserErrorException("Unrecognized amlignore file {}".format(merged_amlignore_file))

    @property
    def additional_includes(self):
        additional_includes = self._get_additional_includes_from_file()
        legacy_additional_includes = self._get_additional_includes_from_spec()

        if additional_includes is not None and legacy_additional_includes is not None:
            raise UserErrorException("The 'additionalIncludes' field in module spec is a duplicate configuration. "
                                     "Please remove it when a separate .additional_includes file is provided.")
        elif legacy_additional_includes is not None:
            self.logger.warning("The 'additionalIncludes' in module spec is deprecated. "
                                "Please set the additional includes in {} file, and save it to the same folder of {}. "
                                "Refer to https://aka.ms/module-additional-includes for details.".format(
                                    self._spec_file_path.with_suffix('.additional_includes').name,
                                    self._spec_file_path.name,
                                ))
            additional_includes = legacy_additional_includes

        return additional_includes or []

    @property
    def hdinsight_pyfiles(self):
        """This property gets the pyFiles item inside HDInsight section."""
        pyfiles = get_value_by_key_path(dct=self._spec_dict, key_path='implementation/hdinsight/pyFiles')

        if not pyfiles:
            return None

        if isinstance(pyfiles, str):
            pyfiles = [pyfiles]

        if not isinstance(pyfiles, list):
            raise UserErrorException("The 'implementation/hdinsight/pyFiles' field in module spec got an "
                                     "unexpected type, expected to be a list but got {}.'".format(type(pyfiles)))

        return pyfiles

    def _get_additional_includes_from_spec(self):
        additional_includes = try_to_get_value_from_multiple_key_paths(
            dct=self._spec_dict,
            key_path_list=[
                'implementation/container/additionalIncludes',
                'implementation/parallel/additionalIncludes',
                'implementation/hdinsight/additionalIncludes',
            ]
        )

        if not additional_includes:
            return None

        if isinstance(additional_includes, str):
            additional_includes = [additional_includes]

        if not isinstance(additional_includes, list):
            raise UserErrorException("The 'additionalIncludes' field in module spec got an unexpected type, "
                                     "expected to be a list but got {}.'".format(type(additional_includes)))

        return additional_includes

    def _get_additional_includes_from_file(self):
        additional_includes_file_name = self._spec_file_path.with_suffix('.additional_includes')
        additional_includes_file = self.base_path / additional_includes_file_name
        additional_includes = None
        try:
            if additional_includes_file.is_file():
                with open(additional_includes_file) as f:
                    lines = f.readlines()
                    # Keep the additional_includes is None when the input is empty list
                    if lines:
                        additional_includes = [l.strip() for l in lines if len(l.strip()) > 0]
        except BaseException:
            self.logger.warning("Failed to load additional_includes file: {0}.".format(additional_includes_file))
            self.logger.debug("Failed to load additional_includes file: {0}.".format(additional_includes_file),
                              exc_info=True)

        return additional_includes

    def _remove_suffix(self, path):
        """Given a path, remove the suffix from it.

        >>> str(Path('/mnt/c/hello.zip'))
        '/mnt/c/hello'
        """
        # Get the stem path name. i.e. For /mnt/c/hello.zip, find /mnt/c/hello
        return path.parent / path.stem

    def _should_be_treated_as_zipped_folder(self, path):
        """Given a path, detect whether it should be treated as a zipped folder.

        For example, given /mnt/c/hello.zip,
          1) If a file or folder named /mnt/c/hello.zip exists, return False
          2) Otherwise,
             a) If a folder named /mnt/c/hello, return True
             b) Otherwise, return False
        """
        if not path.suffix == '.zip':
            return False

        # The file or folder with the .zip suffix exists, not treated as zip folder
        if path.exists():
            return False

        # Get the stem path name. i.e. For /mnt/c/hello.zip, find /mnt/c/hello
        stem_path = self._remove_suffix(path)

        # If the folder /mnt/c/hello exists, return True, otherwise return False
        return stem_path.is_dir()

    def _check_additional_includes(self):
        seen = set()
        for inc in self.additional_includes:
            self._check_additional_includes_item(inc, dst_folder=self.base_path)
            name = (self.base_path / inc).resolve().name
            if name in seen:
                raise UserErrorException("Multiple additional includes item named '{}'.".format(name))
            seen.add(name)

    def _check_additional_includes_item(self, inc, dst_folder):
        inc_path = self.base_path / inc
        src = inc_path.resolve()

        # If the resolved file name is different with the origin input file name,
        # it means that the origin input path wasn't specified to a file name
        # e.g. the path "../../" might be resolved to /foo/bar
        if inc_path.name != src.name:
            self.logger.warning("It's recommended to specify the folder or file name in a additional included path, "
                                "e.g. '../src', '../src/python/library1' and '../assets/LICENSE'. "
                                "The current value is: {0}".format(inc))

        if not src.exists() and not self._should_be_treated_as_zipped_folder(src):
            raise UserErrorException('additionalIncludes path {0} was not found.'.format(src))

        # Check if src is root directory
        if len(src.parents) == 0:
            raise UserErrorException('Root directory is not supported for additionalIncludes.')

        dst_path = dst_folder / src.name
        if dst_path.is_symlink():
            # If the dst_path is a symbolic link, check if it points to the same place of src.
            # If so, treat as a good case; Otherwise, raise error.
            if dst_path.resolve() != src.resolve():
                raise UserErrorException('Path {0} has already existed as a symbolic link to {1}. '
                                         'Please check additionalIncludes.'.format(dst_path, dst_path.resolve()))
        elif dst_path.exists():
            raise UserErrorException('Path {0} has already existed. Please check additionalIncludes.'.format(dst_path))

    def _symbol_link_exist(self):
        for f in self.base_path.glob('**/*'):
            if f.is_symlink():
                return True
        return False

    def _copy_to(self, src, dst, try_to_zip_folders=False, folder_to_lookup_ignore_file=None):
        """Copy src file to dst file or copy src file/directory to location under dst directory.

        :param: src: The file or folder to be copied.
        :param: dst: The target folder to be copied to.
        :param: try_to_zip_folders: When the `src` contains a `.zip` suffix, and the file does not exist,
                                    try to find the folder with same name and copy zipped file.
                                    For example, when src is '/mnt/c/hello.zip', but there is no 'hello.zip' file
                                    in /mnt/c, try to find whether there is a folder named '/mnt/c/hello/'.
                                    If exists, package the folder as 'hello.zip' and then copy to dst folder.
        :param: folder_to_lookup_ignore_file: Specify a folder to lookup ignore file.
                                              This is used only when `try_to_zip_folder` is True.
                                              When creating the zip file, the files listed in the ignore files
                                              are skipped.
        """
        src = src.resolve()
        if src.is_file():
            # Identical to copy() except that copy2() also attempts to preserve file metadata.
            copy2(src, dst)
        elif src.is_dir():
            dst = dst / src.name
            copytree(src, dst)
        elif try_to_zip_folders and self._should_be_treated_as_zipped_folder(src):
            stem_path = self._remove_suffix(src)
            temp_zip_folder = Path(tempfile.mkdtemp()) / src.stem
            self._copy_to(stem_path, temp_zip_folder)
            zip_file = self._make_snapshot(temp_zip_folder, folder_to_lookup_ignore_file=folder_to_lookup_ignore_file)
            self._copy_to(Path(zip_file), dst)
        else:
            raise UserErrorException('Path {0} was not found.'.format(src))

    def _get_snapshot_folder(self):
        if self._snapshot_folder:
            return self._snapshot_folder

        additional_includes = self.additional_includes
        if not additional_includes and not self.additional_amlignore_file and not self._symbol_link_exist():
            return self.base_path

        # Copy original base folder to a temporary folder as final snapshot folder
        temp_directory = Path(tempfile.mkdtemp())
        self._copy_to(self.base_path, temp_directory)

        snapshot_folder = temp_directory / self.base_path.name

        self._make_amlignore(snapshot_folder)

        # Copy additional files/folders to snapshot folder
        if additional_includes:
            for inc in additional_includes:
                self._check_additional_includes_item(inc, snapshot_folder)
                inc_path = self.base_path / inc
                self._copy_to(inc_path, snapshot_folder, try_to_zip_folders=True)

        self._snapshot_folder = snapshot_folder
        return snapshot_folder

    def _make_snapshot(self, src_path, folder_to_lookup_ignore_file=None):
        """Make snapshot file and return its path given source file or directory."""
        src_path = Path(src_path)
        if not src_path.exists():
            raise FileNotFoundError("File or directory {} was not found.".format(src_path))
        if src_path.is_file() and src_path.suffix == '.zip':
            return str(src_path)

        temp_directory = Path(tempfile.mkdtemp())
        zip_file_path = str(temp_directory / (src_path.name + '.zip'))

        if not folder_to_lookup_ignore_file:
            folder_to_lookup_ignore_file = src_path
        if not Path(folder_to_lookup_ignore_file).is_dir():
            raise UserErrorException(
                "No such folder {} to lookup .amlignore from.".format(folder_to_lookup_ignore_file))

        exclude_function = get_project_ignore_file(str(folder_to_lookup_ignore_file)).is_file_excluded
        _make_zipfile(zip_file_path, str(src_path), exclude_function=exclude_function)
        return zip_file_path

    def _iter_files(self):
        # Firstly, iterate files from main snapshot folder
        yield from self._iter_files_in_folder(self.base_path, include_top_level_folder=False)

        # Secondly, iterate files from each additional includes
        for inc in self.additional_includes:
            path = self.base_path / inc
            if self._should_be_treated_as_zipped_folder(path):
                folder_to_zip = self._remove_suffix(path)
                zip_file = self._make_zipfile(snapshot_items_iterator=self._iter_files_in_folder(folder_to_zip))
                yield SnapshotItem(absolute_path=zip_file, relative_path_in_snapshot=path.name)
            else:
                yield from self._iter_files_in_folder(path)

        # Then, create zip entry for implementation/hdinsight/pyFiles if needed
        # NOTE: If the pyFiles is specified as zipped, the unzipped version will also included in snapshot.
        # TODO: Exclude unzipped version from snapshot.
        if self.hdinsight_pyfiles:
            for entry in self.hdinsight_pyfiles:
                path = self.base_path / entry
                if self._should_be_treated_as_zipped_folder(path):
                    folder_to_zip = self._remove_suffix(path)
                    zip_file = self._make_zipfile(snapshot_items_iterator=self._iter_files_in_folder(folder_to_zip))
                    yield SnapshotItem(absolute_path=zip_file, relative_path_in_snapshot=path.name)
                else:
                    # TODO: check existance of each entry
                    pass

    def _iter_files_in_folder(self, folder, include_top_level_folder=True):
        def create_snapshot_item(path):
            relative_path = path.relative_to(folder)
            if include_top_level_folder:
                # folder must be resolved before getting name since it may be .. or ~ which do not have valid names
                folder_name = folder.resolve().name
                # Append folder_name to the top level of relative path if `include_top_level_folder` specified.
                relative_path = Path(folder_name) / relative_path

            return SnapshotItem(absolute_path=path, relative_path_in_snapshot=relative_path)

        def is_ignored(path):
            folders_to_check = [p for p in path.parents if p not in folder.parents]
            for parent in folders_to_check:
                ignore_file = get_project_ignore_file(str(parent))
                if ignore_file.is_file_excluded(path):
                    return True

            # If not match with the normal ignore files,
            # check the additional amlignore file to see if there's any match.
            if self.additional_amlignore_file:
                # NOTE: Must use the relative path here since the additional amlignore file
                #       may not layout in the same tree of the source path.
                #       Absolute paths will cause the check fail for that case.
                path = path.relative_to(folder)
                ignore_file = IgnoreFile(self.additional_amlignore_file)
                if ignore_file.is_file_excluded(path):
                    return True

            # If the logic goes here, indicates that the file should not be ignored.
            return False

        if Path(folder).is_file():
            # Yield the item directly if it is a file
            yield SnapshotItem(absolute_path=folder, relative_path_in_snapshot=folder.name)

        else:
            # Otherwise treat as a folder
            if include_top_level_folder:
                yield create_snapshot_item(Path(folder))

            for cur_dir, dirnames, filenames in os.walk(folder, followlinks=True):
                for filename in filenames + dirnames:
                    full_path = Path(cur_dir) / filename
                    if not is_ignored(full_path):
                        yield create_snapshot_item(full_path)

    def _make_zipfile(self, snapshot_items_iterator, zip_file_name='temp.zip'):
        temp_directory = Path(tempfile.mkdtemp())
        zip_file = temp_directory / zip_file_name
        with zipfile.ZipFile(zip_file, 'w') as zf:
            for snapshot_item in snapshot_items_iterator:
                zf.write(snapshot_item.absolute_path, snapshot_item.relative_path)
            return zip_file


def _make_zipfile(zip_file_path, folder_or_file_to_zip, exclude_function=None):
    """Create an archive with exclusive files or directories. Adapted from shutil._make_zipfile.

    :param zip_file_path: Path of zip file to create.
    :param folder_or_file_to_zip: Directory or file that will be zipped.
    :param exclude_function: Function of exclude files or directories
    """
    with zipfile.ZipFile(zip_file_path, "w") as zf:
        if os.path.isfile(folder_or_file_to_zip):
            zf.write(folder_or_file_to_zip, os.path.basename(folder_or_file_to_zip))
        else:
            for dirpath, dirnames, filenames in os.walk(folder_or_file_to_zip):
                relative_dirpath = os.path.relpath(dirpath, folder_or_file_to_zip)
                for name in sorted(dirnames):
                    full_path = os.path.normpath(os.path.join(dirpath, name))
                    relative_path = os.path.normpath(os.path.join(relative_dirpath, name))
                    if exclude_function and exclude_function(full_path):
                        continue
                    zf.write(full_path, relative_path)
                for name in filenames:
                    full_path = os.path.normpath(os.path.join(dirpath, name))
                    relative_path = os.path.normpath(os.path.join(relative_dirpath, name))
                    if exclude_function and exclude_function(full_path):
                        continue
                    if os.path.isfile(full_path):
                        zf.write(full_path, relative_path)


def _replace_invalid_char_in_file_name(file_name, rep='_'):
    """Replace all invalid characters (<>:"/\\|?*) in file name."""
    invalid_file_name_chars = r'<>:"/\|?*'
    return "".join(rep if c in invalid_file_name_chars else c for c in file_name)


def _normalize_file_name(target_dir=None, file_name=None, overwrite=False, logger=None):
    """Return a valid full file path to write."""
    if not target_dir:
        target_dir = os.getcwd()
        logger.debug("Target dir is not provided, use cwd: {}".format(target_dir))
    else:
        target_dir = os.path.abspath(target_dir)
        logger.debug("Normalized target dir: {}".format(target_dir))

    target_path = Path(target_dir)
    if not target_path.exists():
        raise ValueError("Target dir does not exist.")

    if target_path.is_file():
        raise ValueError("Target dir is not a directory.")

    if not file_name:
        raise ValueError("File name is required.")

    file_name = _replace_invalid_char_in_file_name(file_name)
    full_file_path = target_path / file_name

    logger.debug("Normalized file name: {}".format(full_file_path))
    if not overwrite and full_file_path.exists():
        raise ValueError("File already exists, use -y if you attempt to overwrite.")

    return str(full_file_path)


def _download_file_to_local(url, target_dir=None, file_name=None, overwrite=False, logger=None):
    file_name = _normalize_file_name(target_dir=target_dir, file_name=file_name, overwrite=overwrite, logger=logger)

    # download file
    BaseHttpClient(logger).download_file(url, file_name=file_name)
    return file_name


def _write_file_to_local(content, target_dir=None, file_name=None, overwrite=False, logger=None):
    file_name = _normalize_file_name(target_dir=target_dir, file_name=file_name, overwrite=overwrite, logger=logger)

    # save file
    with open(file_name, 'w') as fp:
        # we suppose that content only use '\n' as EOL.
        fp.write(content)
    return file_name


def get_value_by_key_path(dct, key_path, default_value=None):
    """Given a dict, get value from key path.

    >>> dct = {
    ...     'Employee': {
    ...         'Profile': {
    ...             'Name': 'Alice',
    ...             'Age': 25,
    ...         }
    ...     }
    ... }
    >>> get_value_by_key_path(dct, 'Employee/Profile/Name')
    'Alice'
    >>> get_value_by_key_path(dct, 'Employee/Profile/Age')
    25
    >>> get_value_by_key_path(dct, 'Employee/Profile')
    {'Name': 'Alice', 'Age': 25}
    """
    if not key_path:
        raise ValueError("key_path must not be empty")

    segments = key_path.split('/')
    final_flag = object()
    segments.append(final_flag)

    walked = []

    cur_obj = dct
    for seg in segments:
        # If current segment is final_flag,
        # the cur_obj is the object that the given key path points to.
        # Simply return it as result.
        if seg is final_flag:
            # return default_value if cur_obj is None
            return default_value if cur_obj is None else cur_obj

        # If still in the middle of key path, when cur_obj is not a dict,
        # will fail to locate the values
        if not isinstance(cur_obj, dict):
            # TODO: maybe add options to raise exceptions here in the future
            return default_value

        # Move to next segment
        cur_obj = cur_obj.get(seg)
        walked.append(seg)

    raise RuntimeError("Should never go here")


def try_to_get_value_from_multiple_key_paths(dct, key_path_list, default_value=None):
    """Same as get_value_by_key_path, but try to get from multiple key paths,
       try the given key paths one by one."""
    for key_path in key_path_list:
        value = get_value_by_key_path(dct, key_path=key_path)
        if value is not None:
            return value
    return default_value
