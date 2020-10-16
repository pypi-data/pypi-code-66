# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
from pathlib import Path

from azure.ml.component._loggerfactory import _LoggerFactory, track, _PUBLIC_API
from azure.ml.component._telemetry import WorkspaceTelemetryMixin
from azure.ml.component.debug._image import ModuleImage
from azure.ml.component.debug._module_debug_helper import DebugLocalModuleHelper
from azure.ml.component.debug._step_run_debugger import DebugRunner
from azureml.core import Workspace
from azure.ml.component.dsl._component_local_param_builder import _ComponentLocalParamBuilderFromDefinition
from azure.ml.component.dsl._pipeline_project import _get_telemetry_logger
from azure.ml.component.dsl._utils import _print_step_info
from azure.ml.component._module_run_helper import _generate_command
from azure.ml.component import Component


class LocalModuleDebugger(DebugRunner, WorkspaceTelemetryMixin):
    def __init__(self,
                 workspace_name=None,
                 resource_group=None,
                 subscription_id=None,
                 yaml_file=None):
        if None in [yaml_file, workspace_name, resource_group, subscription_id]:
            raise ValueError(
                'yaml_file, workspace_name, resource_group, subscription_id cannot be null.')
        # Need to get the folder name of yaml_file located to specify workspaceFolder.
        # When debug module in container, will mount target to container and use target name to spell workspaceFolder.
        # If yaml_file path is relative, parent folder may be '.', workspaceFolder will point to target parent folder,
        # so need translate to absolute path to get target name.
        target = str(Path(yaml_file).absolute().parent)
        yaml_file = str(Path(yaml_file).absolute().as_posix())
        super().__init__(target=target)

        _print_step_info(f'Preparing module remote debug config')

        self.workspace = Workspace(subscription_id=subscription_id, resource_group=resource_group,
                                   workspace_name=workspace_name)

        WorkspaceTelemetryMixin.__init__(self, workspace=self.workspace)

        module_func = Component.from_yaml(self.workspace, yaml_file)
        self.module = module_func()

        self.module_param_builder = _ComponentLocalParamBuilderFromDefinition(self.module, Path(self.target))
        self.module_param_builder.build()

        self.run = self.run_step(self.local_setup)
        self.dry_run = False

    @track(_get_telemetry_logger, activity_name="LocalModuleDebugger_debug", activity_type=_PUBLIC_API)
    def local_setup(self):
        # won't pull image for test
        if '_TEST_ENV' in os.environ:
            self.dry_run = True

        # log trace
        telemetry_values = WorkspaceTelemetryMixin._get_telemetry_value_from_workspace(self.workspace)
        telemetry_values.update({'job_type': self.module.job_type})
        _LoggerFactory.trace(_get_telemetry_logger(), "LocalModuleDebug", telemetry_values)

        if self.dry_run:
            image_name = ''
        else:
            module_image = ModuleImage(self.module)
            _print_step_info('Preparing module image.')
            image_name = module_image.get_module_image()
            _print_step_info(f'Prepared module image {image_name}.')

        workspace_folder = "/workspace/{}".format(os.path.basename(self.target))
        workspace_mount = "source=${localWorkspaceFolder}," + \
                          f"target={workspace_folder},type=bind,consistency=delegated"

        container_input_prefix = str(self.module_param_builder.input_dir.relative_to(self.target).as_posix())
        container_output_prefix = str(self.module_param_builder.output_dir.relative_to(self.target).as_posix())
        # generate arguments
        # set create_output_folder to false since we already put input/output into data folder via
        # _ComponentLocalParamBuilderFromDefinition
        command, volumes, _ = _generate_command(
            self.module, self.target, True, remove_none_value=False, check_data_exist=False,
            container_input_prefix=container_input_prefix, container_output_prefix=container_output_prefix)

        DebugLocalModuleHelper.prepare_dev_container(image_name,
                                                     name=self.module.name,
                                                     containerEnv={},
                                                     workspaceMount=workspace_mount,
                                                     workspaceFolder=workspace_folder,
                                                     target=self.target
                                                     )
        DebugLocalModuleHelper.create_launch_config(self.module_param_builder.component_file_name,
                                                    command,
                                                    self.target,
                                                    self.module.job_type,
                                                    )
        LocalModuleDebugger.hint_to_reopen_in_container(self.target)
