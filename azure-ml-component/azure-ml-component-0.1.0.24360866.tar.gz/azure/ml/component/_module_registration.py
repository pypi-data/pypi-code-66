# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import re
import os
import warnings
from enum import IntEnum
from typing import BinaryIO

from azure.ml.component._restclients.service_caller_factory import _DesignerServiceCallerFactory
from azure.ml.component._api._component_snapshot import ComponentSnapshot
from azureml.core import Workspace
from azureml.exceptions._azureml_exception import UserErrorException


from ._module_dto import ModuleDto
from ._utils import _scrubbed_exception


class _ModuleSourceType(IntEnum):
    Local = 1
    GithubFile = 2
    GithubFolder = 3
    DevopsArtifactsZip = 4


def _is_github_url(yaml_file: str):
    return re.match(r'^(https?://)?github.com', yaml_file)


def _register_module(workspace: Workspace, module_source_type: _ModuleSourceType, yaml_file: str = None,
                     snapshot_source_zip_file: BinaryIO = None, devops_artifacts_zip_url: str = None,
                     validate_only: bool = False, anonymous_registration: bool = True, set_as_default: bool = False,
                     version: str = None):
    service_caller = _DesignerServiceCallerFactory.get_instance(workspace)
    result = service_caller.register_module(anonymous_registration=anonymous_registration, validate_only=validate_only,
                                            module_source_type=int(module_source_type), yaml_file=yaml_file,
                                            snapshot_source_zip_file=snapshot_source_zip_file,
                                            devops_artifacts_zip_url=devops_artifacts_zip_url,
                                            set_as_default=set_as_default,
                                            overwrite_module_version=version)
    return ModuleDto(result)


def _load_from_local(workspace: Workspace, yaml_file: str, amlignore_file: str = None,
                     anonymous_registration: bool = True, set_as_default: bool = False,
                     version: str = None):
    if not os.path.isfile(yaml_file):
        msg = "The file {} did not exist."
        raise _scrubbed_exception(UserErrorException, msg, yaml_file)
    snapshot_source_zip_file_name = ""

    try:
        _, yaml_file_name = os.path.split(os.path.abspath(yaml_file))
        snapshot = ComponentSnapshot(yaml_file, additional_amlignore_file=amlignore_file)
        snapshot_source_zip_file_name = snapshot.create_snapshot()
        with open(snapshot_source_zip_file_name, 'rb') as snapshot_source_zip_file:
            result = _register_module(workspace, _ModuleSourceType.Local, snapshot.spec_file_relative_path.as_posix(),
                                      snapshot_source_zip_file, anonymous_registration=anonymous_registration,
                                      set_as_default=set_as_default, version=version)
    finally:
        if os.path.isfile(snapshot_source_zip_file_name):
            os.remove(snapshot_source_zip_file_name)

    return result


def _load_from_github(workspace: Workspace, yaml_file: str, anonymous_registration: bool = True,
                      set_as_default: bool = False, version: str = None):
    result = _register_module(workspace,
                              _ModuleSourceType.GithubFile,
                              yaml_file,
                              anonymous_registration=anonymous_registration,
                              set_as_default=set_as_default,
                              version=version)
    return result


def _load_anonymous_module(workspace: Workspace, yaml_file: str):
    if _is_github_url(yaml_file):
        return _load_from_github(workspace, yaml_file)
    else:
        return _load_from_local(workspace, yaml_file)


def _register_module_from_yaml(workspace: Workspace, yaml_file: str, amlignore_file: str = None,
                               set_as_default: bool = False, version: str = None):
    if _is_github_url(yaml_file):
        if amlignore_file is not None:
            warnings.warn(
                "The amlignore_file specified will not work as expected since the yaml_file is GitHub path.")
        return _load_from_github(workspace, yaml_file,
                                 anonymous_registration=False, set_as_default=set_as_default,
                                 version=version)
    else:
        return _load_from_local(workspace, yaml_file, amlignore_file,
                                anonymous_registration=False, set_as_default=set_as_default,
                                version=version)
