# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from azureml._cli import abstract_subgroup
from azureml._cli import cli_command
from azureml._cli import argument
from azureml._cli.example import Example

NAMESPACE = argument.Argument(
    "namespace", "--namespace", "", required=False,
    help="Namespace of the component.")
COMPONENT_NAME = argument.Argument(
    "component_name", "--name", "-n", required=True,
    help="Name of the component.")
COMPONENT_VERSION = argument.Argument(
    "component_version", "--version", "-v", required=False,
    help="Version of the component.")


class ComponentSubGroup(abstract_subgroup.AbstractSubGroup):
    """This class defines the component sub group."""

    def get_subgroup_name(self):
        """Returns the name of the subgroup.
        This name will be used in the cli command."""
        return "component"

    def get_subgroup_title(self):
        """Returns the subgroup title as string. Title is just for informative purposes, not related
        to the command syntax or options. This is used in the help option for the subgroup."""
        return "component subgroup commands (preview)"

    def get_nested_subgroups(self):
        """Returns sub-groups of this sub-group."""
        return super(ComponentSubGroup, self).compute_nested_subgroups(__package__)

    def get_commands(self, for_azure_cli=False):
        """ Returns commands associated at this sub-group level."""
        commands_list = [
            self._command_component_export(),
            self._command_register(),
            self._command_validate(),
            self._command_list(),
            self._command_show(),
            self._command_enable(),
            self._command_disable(),
            self._command_set_default_version(),
            self._command_download(),
            self._command_init(),
            self._command_build(),
            self._command_debug()
        ]
        return commands_list

    def _command_component_export(self):
        # Note: put export to module_commands because cli requires all handler function in same package
        function_path = "azure.ml.component._cli.component_commands#_export"

        url = argument.Argument("url", "--url", "", required=False,
                                help="url of the PipelineDraft or PipelineRun to export")
        draft_id = argument.Argument("draft_id", "--draft-id", "", required=False,
                                     help="ID of the PipelineDraft to export")
        run_id = argument.Argument("run_id", "--run-id", "", required=False,
                                   help="ID of the PipelineRun to export")
        path = argument.Argument("path", "--path", "-p", required=False,
                                 help="File path to save exported graph to.")
        export_format = argument.Argument("export_format", "--export-format", "", required=False,
                                          help="Export file format of the entry pipeline. One of \
                                          {py, ipynb, Python, JupyterNotebook}. Default value is JupyterNotebook",
                                          default="JupyterNotebook")
        subscription_id = argument.Argument("subscription_id", "--subscription-id", "", required=False,
                                            help="Subscription ID")
        return cli_command.CliCommand("export", "Export pipeline draft or pipeline run as sdk code",
                                      [url,
                                       draft_id,
                                       run_id,
                                       path,
                                       export_format,
                                       subscription_id,
                                       argument.RESOURCE_GROUP_NAME,
                                       argument.WORKSPACE_NAME], function_path)

    def _command_register(self):
        function_path = "azure.ml.component._cli.component_commands#_register_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            argument.Argument(
                "spec_file", "--spec-file", "-f", required=False,
                help="The component spec file. Accepts either a local file path, a GitHub url, "
                     "or a relative path inside the package specified by --package-zip."),
            argument.Argument(
                "package_zip", "--package-zip", "-p", required=False,
                help="The zip package contains the component spec and implemention code. "
                     "Currently only accepts url to a DevOps build drop."),
            argument.Argument(
                "set_as_default", "--set-as-default-version", "-a", action="store_true", required=False,
                help="By default, default version of the component will not be updated "
                     "when registering a new version of component. "
                     "Specify this flag to set the new version as the component's default version."),
            argument.Argument(
                "amlignore_file", "--amlignore-file", "-i", required=False,
                help="The .amlignore or .gitignore file used to exclude files/directories in the snapshot."),
            argument.Argument(
                "fail_if_exists", "--fail-if-exists", "", action="store_true", required=False,
                help="By default, the CLI exits as succeed (exit 0) if the same version of component "
                     "already exists in workspace. "
                     "Specify this flag to exit as failure (exit non-zero) for the case."),
            argument.Argument(
                "version", "--set-version", "", required=False,
                help="If specified, registered component's version will be overwritten to specified value "
                     "instead of the version in the yaml."),
        ]

        examples = [
            Example(
                name="Register from local folder",
                text="az ml component register --spec-file=path/to/component_spec.yaml",
            ),
            Example(
                name="Register a new version of an existing component",
                text="az ml component register --spec-file=path/to/new/version/of/component_spec.yaml",
            ),
            Example(
                name="By default, registering a new version will not update the default version "
                     "of the component. Use --set-as-default-version to update the default version",
                text="az ml component register --spec-file=path/to/new/version/of/component_spec.yaml "
                     "--set-as-default-version",
            ),
            Example(
                name="Register from GitHub url",
                text="az ml component register --spec-file=https://github.com/user/repo/path/to/component_spec.yaml",
            ),
            Example(
                name="Register from a zip package build by DevOps",
                text="az ml component register --package-zip=https://dev.azure.com/path/to/the/component_package.zip "
                     "--spec-file=component_spec.yaml",
            ),
            Example(
                name="Register from local folder with .amlignore",
                text="az ml component register --spec-file=path/to/component_spec.yaml "
                     "--amlignore-file path/to/.amlignore",
            ),
            Example(
                name="Register from local folder with specific version number",
                text="az ml component register --spec-file=path/to/component_spec.yaml --set-version xx.xx.xx",
            ),
            Example(
                name="Register all components inside .componentproject",
                text="az ml component register --spec-file=path/to/.componentproj",
                # TODO: add a user manual for .componentproj here
            ),
        ]

        return cli_command.CliCommand(
            name='register',
            title='Create or upgrade a component.',
            arguments=arguments,
            handler_function_path=function_path,
            description="Components could either be registered from a local folder, a GitHub url, "
                        "or a zip package (typically created by a DevOps CI build job).",
            examples=examples
        )

    def _command_validate(self):
        function_path = "azure.ml.component._cli.component_commands#_validate_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            argument.Argument(
                "spec_file", "--spec-file", "-f", required=False,
                help="The component spec file. Accepts either a local file path, a GitHub url, "
                     "or a relative path inside the package specified by --package-zip."),
            argument.Argument(
                "package_zip", "--package-zip", "-p", required=False,
                help="The zip package contains the component spec and implemention code. "
                     "Currently only accepts url to a DevOps build drop."),
        ]

        examples = [
            Example(
                name="Validate component spec located in a local folder",
                text="az ml component validate-spec --spec-file=path/to/component_spec.yaml",
            ),
            Example(
                name="Validate component spec located in a GitHub repo",
                text="az ml component validate-spec "
                     "--spec-file=https://github.com/user/repo/path/to/component_spec.yaml",
            ),
            Example(
                name="Validate component spec located inside a package zip",
                text="az ml component validate-spec "
                     "--package-zip=https://dev.azure.com/path/to/the/component_package.zip "
                     "--spec-file=component_spec.yaml",
            ),
        ]

        return cli_command.CliCommand(
            name='validate-spec',
            title='Validate component spec file.',
            arguments=arguments,
            handler_function_path=function_path,
            description="Validate component spec before registering to a workspace.\n\n"
                        "The spec file could either located in a local folder or a GitHub url.",
            examples=examples
        )

    def _command_list(self):
        function_path = "azure.ml.component._cli.component_commands#_list_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            argument.Argument(
                "include_disabled", "--include-disabled", "", action="store_true", required=False,
                help="Include disabled components in list result."),
        ]

        examples = [
            Example(
                name="Show component list as table",
                text="az ml component list --output table",
            ),
            Example(
                name="List both active and disabled components in a workspace",
                text="az ml component list --include-disabled",
            ),
        ]

        return cli_command.CliCommand(
            name='list',
            title='List components in a workspace.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )

    def _command_show(self):
        function_path = "azure.ml.component._cli.component_commands#_show_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            NAMESPACE,
            COMPONENT_NAME,
            COMPONENT_VERSION,
        ]

        examples = [
            Example(
                name="Show detail information of a component's default version",
                text='az ml component show --name "component Name"',
            ),
            Example(
                name="Show detail information of a component's specific version",
                text='az ml component show --name "component Name" --version 0.0.1',
            ),
            Example(
                name="Show detail information of a component within specific namespace",
                text='az ml component show --name "component Name" --namespace microsoft.com/azureml/samples',
            ),
        ]

        return cli_command.CliCommand(
            name='show',
            title='Show detail information of a component.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )

    def _command_enable(self):
        function_path = "azure.ml.component._cli.component_commands#_enable_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            NAMESPACE,
            COMPONENT_NAME,
        ]

        examples = [
            Example(
                name="Enable a component",
                text='az ml component enable --name "component Name"',
            ),
            Example(
                name="Enable a component within specific namespace",
                text='az ml component enable --name "component Name" --namespace microsoft.com/azureml/samples',
            ),
        ]

        return cli_command.CliCommand(
            name='enable',
            title='Enable a component.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )

    def _command_disable(self):
        function_path = "azure.ml.component._cli.component_commands#_disable_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            NAMESPACE,
            COMPONENT_NAME,
        ]

        examples = [
            Example(
                name="Disable a component",
                text='az ml component disable --name "component Name"',
            ),
            Example(
                name="Disable a component within specific namespace",
                text='az ml component disable --name "component Name" --namespace microsoft.com/azureml/samples',
            ),
        ]

        return cli_command.CliCommand(
            name='disable',
            title='Disable a component.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )

    def _command_set_default_version(self):
        function_path = "azure.ml.component._cli.component_commands#_component_set_default_version"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            NAMESPACE,
            COMPONENT_NAME,
            argument.Argument("component_version", "--version", "-v", required=True,
                              help="Version to be set as default."),
        ]

        examples = [
            Example(
                name="Set default version of a component",
                text='az ml component set-default-version --name "component Name" --version 0.0.1',
            ),
            Example(
                name="Set default version of a component within specific namespace",
                text='az ml component set-default-version --name "component Name" '
                     '--namespace microsoft.com/azureml/samples',
            ),
        ]

        return cli_command.CliCommand(
            name='set-default-version',
            title='Set default version of a component.',
            arguments=arguments,
            handler_function_path=function_path,
            description="By default, registering a new version to an existing component will not update "
                        "the default version of the component. "
                        "This is useful for a component to be registered for testing.\n\n"
                        "When the tests passed and ready to ship, use this command to update the default version to "
                        "the new version of the component.\n\n"
                        "Also this command could be used to revert a component's version in case when some bugs "
                        "has been detected in the production environment.",
            examples=examples
        )

    def _command_download(self):
        function_path = "azure.ml.component._cli.component_commands#_download_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            NAMESPACE,
            COMPONENT_NAME,
            COMPONENT_VERSION,
            argument.Argument(
                "target_dir", "--target-dir", "",
                help="The target directory to save to. Will use current working directory if not specified."),
            argument.Argument(
                "overwrite", "--overwrite", "-y", action="store_true",
                help="Overwrite if the target directory is not empty.")
        ]

        examples = [
            Example(
                name="Download component spec along with the snapshot to current working directory",
                text='az ml component download --name "component Name"',
            ),
            Example(
                name="Download component to a specific folder",
                text='az ml component download --name "component Name" --target-dir path/to/save',
            ),
            Example(
                name="Download component of specific version",
                text='az ml component download --name "component Name" --version 0.0.1',
            )
        ]

        return cli_command.CliCommand(
            name='download',
            title='Download a component to a specified directory.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )

    def _command_init(self):
        function_path = "azure.ml.component._cli.component_commands#_init_component"

        arguments = [
            argument.Argument(
                "source", "--source", "",
                help="Source for specific mode, could be pacakge.function or path/to/python_file.py "
                     "or path/to/python_file.ipynb."),
            argument.Argument(
                "component_name", "--name", "-n",
                help="Name of the component."),
            argument.Argument(
                "job_type", "--type", "", default='basic', choices=['basic', 'mpi', 'parallel'],
                help="Job type of the component. Could be basic, mpi."),
            argument.Argument(
                "source_dir", "--source-dir", "",
                help="Source directory to init the environment, "
                     "resources(notebook, data, test) will be generated under source directory, "
                     "will be os.cwd() if not set. "
                     "Note when init a component from scratch, a new folder will be generated under source directory. "
                     "Source directory will be that folder in this case."),
            argument.Argument(
                "inputs", "--inputs", "", nargs='+',
                help="Input names of the component when init from an argparse entry"),
            argument.Argument(
                "outputs", "--outputs", "", nargs='+',
                help="Output names of the component when init from an argparse entry"),
            argument.Argument(
                "entry_only", "--entry-only", "", action='store_true',
                help="If specified, only component entry will be generated."),
        ]

        examples = [
            Example(
                name="Create a simple component from template with name \"Sample component\" in "
                     "sample_component folder.",
                text="az ml component init --name \"Sample component\"",
            ),
            Example(
                name="Create an mpi component from template with name \"Sample MPI component\" in "
                     "sample_mpi_component folder.",
                text="az ml component init --name \"Sample MPI component\" --type mpi",
            ),
            Example(
                name="Create a simple component from template with name \"Sample component\" in folder "
                     "my_folder/sample_component. "
                     "Note source directory here is my_folder/sample_component instead of my_folder.",
                text="az ml component init --name \"Sample component\" --source-dir my_folder",
            ),
            Example(
                name="Create a component from existing function 'add' in 'my_component.py' in folder add.",
                text="az ml component init --source my_component.add"
            ),
            Example(
                name="Create a component from existing function 'add' in 'my_component.py' and use name \"My Add\" "
                     "in folder my_add.",
                text="az ml component init --source my_component.add --name \"My Add\""
            ),
            Example(
                name="Create a component from an existing python entry 'main.py' in which argparse is used,"
                     " inputs are input1, input2, outputs are output1, output2.",
                text="az ml component init --source main.py --inputs input1 input2 --outputs output1 output2"
            ),
            Example(
                name="Create a component from an existing jupyter notebook entry 'main.ipynb'.",
                text="az ml component init --source main.ipynb"
            ),
            Example(
                name="Create resources from existing dsl.component, source directory would be entry_folder.",
                text="az ml component init --source entry_folder/sample_component.py --source-dir entry_folder"
            ),
            Example(
                name="Create resources from existing dsl.component, source directory would be current folder.",
                text="az ml component init --source my_components.my_component"
            ),
            Example(
                name="Create a simple component entry with name \"Sample component\" in sample_component folder.",
                text="az ml component init --name \"Sample component\" --entry-only"
            )
        ]

        return cli_command.CliCommand(
            name='init',
            title='Add a dsl.component entry file and resources into a component project.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )

    def _command_build(self):
        function_path = "azure.ml.component._cli.component_commands#_build_component"

        arguments = [
            argument.Argument(
                "target", "--target", "",
                help="Target component project or component file. "
                     "Will use current working directory if not specified."),
            argument.Argument(
                "source_dir", "--source-dir", "",
                help="Source directory to build spec, will be os.cwd() if not set.")
        ]

        examples = [
            Example(
                name="Build all dsl.components in component_folder into specs.",
                text="az ml component build --target component_folder",
            ),
            Example(
                name="Build a dsl.component file into spec.",
                text="az ml component build --target component.py",
            ),
            Example(
                name="Build a dsl.component file into spec, spec file will be generated in 'entry_folder', "
                     "source directory will be current folder.",
                text="az ml component build --target entry_folder/component.py"
            ),
            Example(
                name="Build a dsl.component file into spec, source directory will be 'a/b', "
                     "spec file will be generated in 'entry_folder'.",
                text="az ml component build --target a/b/c/component.py --source-dir a/b"
            ),
            Example(
                name="Build all components inside .componentproject",
                text="az ml component build --target=path/to/.componentproj",
                # TODO: add a user manual for .componentproj here
            )
        ]

        return cli_command.CliCommand(
            name='build',
            title='Builds dsl.component.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )

    def _command_debug(self):
        """Debug a step run/component. Put this command here to support 2 debug options: debug a step run with URL;
        debug a step run with auto arg(run id, experiment name, etc.)"""
        function_path = "azure.ml.component._cli.component_commands#_debug_component"

        arguments = [
            argument.WORKSPACE_NAME,
            argument.RESOURCE_GROUP_NAME,
            argument.SUBSCRIPTION_ID,
            argument.Argument("run-id", "--run-id", "-i", help="Step run id."),
            argument.Argument("experiment-name", "--experiment-name", "-e", help="Experiment name."),
            argument.Argument("url", "--url", "-u", help="Step run url."),
            argument.Argument(
                "target", "--target", "",
                help="Target directory to build environment, will use current working directory if not specified."),
            argument.Argument("spec-file", "--spec-file", "", help="The component spec file."),
            argument.Argument("dry-run", "--dry-run", "", action='store_true', help="Dry run.")
        ]

        examples = [
            Example(
                name="Debug a step run and store resources(inputs, outputs, snapshot) in current directory.",
                text='az ml component debug --run-id run-id --experiment-name experiment-name '
                     '--subscription-id subscription-id --resource-group resource-group '
                     '--workspace-name workspace-name',
            ),
            Example(
                name="Debug a step run and store resources(inputs, outputs, snapshot) in specified directory.",
                text='az ml component debug --url url --working_dir ./demo',
            ),
            Example(
                name="Debug component in container.",
                text='az ml component debug --spec-file spec_file '
                     '--subscription-id subscription-id --resource-group resource-group '
                     '--workspace-name workspace-name',
            )
        ]

        return cli_command.CliCommand(
            name='debug',
            title='Debug a component.',
            arguments=arguments,
            handler_function_path=function_path,
            examples=examples
        )
