# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from azure.ml.component._api._api_impl import ComponentAPICaller
from azure.ml.component._api._component_source import ComponentSource, ComponentSourceParams
from azure.ml.component._api._utils import _get_default_namespace, _write_file_to_local, _download_file_to_local
from azure.ml.component._restclients.exceptions import ServiceError


definition_cache = {}


def _dto_2_definition(dto, workspace=None):
    """Convert from ModuleDto to ContainerComponentDefinition.

    :param dto: ModuleDto
    :param workspace: Workspace
    :type dto: azure.ml.component._restclients.designer.models.ModuleDto
    :return: ContainerComponentDefinition
    """
    from ruamel import yaml

    from azure.ml.component.core._component_definition import ContainerComponentDefinition, MetaData
    from azure.ml.component.core._component_contexts import CreationContext, RegistrationContext
    from azure.ml.component.core._run_settings_definition import RunSettingsDefinition, K8sRunSettingsDefinition
    from azure.ml.component._module_dto import ModuleDto

    # Here we use the id of the dto object as a cache key,
    definition_cache_key = id(dto)
    if definition_cache_key in definition_cache:
        return definition_cache[definition_cache_key]

    if not isinstance(dto, ModuleDto):
        dto = ModuleDto(dto)
        dto.correct_module_dto()  # Update some fields to make sure this works well.

    interface = dto.module_python_interface
    # This is a workaround to avoid serialization error if component._module_dto.ModuleDto is passed.
    dto.module_python_interface = None
    attr_dict = dto.serialize(keep_readonly=True)
    dto.module_python_interface = interface

    # TODO: some api returned dto doesn't have yaml_str, use this when SMT support them
    if hasattr(dto, 'yaml_str') and dto.yaml_str is not None and dto.yaml_str != "":
        dct = yaml.safe_load(dto.yaml_str)
        result = ContainerComponentDefinition._from_module_yaml_dict(dct)
        result._runsettings = RunSettingsDefinition.from_dto_runsettings(dto.run_setting_parameters)
        result._k8srunsettings = K8sRunSettingsDefinition.from_dto_runsettings(dto.run_setting_parameters)
    else:
        dct = {
            'name': dto.module_name,
            'version': dto.module_version,
            'namespace': dto.namespace,
            'jobType': dto.job_type,
            'description': dto.description,
            'type': ContainerComponentDefinition.TYPE_NAME,
            'metadata': MetaData({'annotations': {
                'helpDocument': dto.help_document,
                'contact': dto.owner,
                'tags': dto.tags
            }})
        }
        result = ContainerComponentDefinition._from_dict(dct)

    result._workspace = workspace

    result.creation_context = CreationContext(attr_dict)
    result.registration_context = RegistrationContext(attr_dict)
    result._identifier = dto.module_version_id  # This id is the identifier in the backend server.
    result._module_dto = dto

    # This is a workaround that we need to set the mapping from display name to name
    # so Component could be correctly submitted/run.
    for value in dto.module_entity.structured_interface.inputs + dto.module_entity.structured_interface.outputs:
        if value.label:
            result._display_name_to_name[value.label] = value.name

    # Put the result in the cache once the result comes from yaml.
    if hasattr(dto, 'yaml_str') and dto.yaml_str is not None and dto.yaml_str != "":
        definition_cache[definition_cache_key] = result

    return result


class ComponentAPI:
    """CRUD operations for Component.

    Contains some client side logic(Value check, log, etc.)
    Actual CRUD are implemented via CRUDImplementation.
    """

    def __init__(self, workspace, logger, from_cli=False):
        """Init component api

        :param workspace: workspace
        :param logger: logger
        :param from_cli: mark if this service caller is used from cli.
        """
        self.workspace = workspace
        self.imp = ComponentAPICaller(workspace, from_cli)
        self.logger = logger

    def _parse(self, component_source):
        """Parse component source to ModuleDto.

        :param component_source: Local component source.
        :return: ModuleDto
        :rtype: azure.ml.component._restclients.designer.models.ModuleDto
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        with ComponentSourceParams(component_source).create(spec_only=True) as params:
            return self.imp.parse(**params)

    def _validate_component(self, component_source):
        """Validate a component.

        :param component_source: Local component source.
        :return: ModuleDto
        :rtype: azure.ml.component._restclients.designer.models.ModuleDto
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        component_dto = self._parse(component_source)
        entry = component_dto.entry
        if component_source.is_invalid_entry(entry):
            msg = "Entry file '%s' doesn't exist in source directory." % entry
            raise ServiceError(msg)
        return component_dto

    def register(self, spec_file, package_zip, set_as_default, amlignore_file, version):
        """Register the component to workspace.

        :param spec_file: The component spec file. Accepts either a local file path, a GitHub url,
                            or a relative path inside the package specified by --package-zip.
        :type spec_file: Union[str, None]
        :param package_zip: The zip package contains the component spec and implementation code.
                            Currently only accepts url to a DevOps build drop.
        :type package_zip: Union[str, None]
        :param amlignore_file: The .amlignore or .gitignore file used to exclude files/directories in the snapshot.
        :type amlignore_file: Union[str, None]
        :param set_as_default: Whether to update the default version.
        :type set_as_default: Union[str, None]
        :param version: If specified, registered component will use specified value as version
                                            instead of the version in the yaml.
        :type version: Union[str, None]
        :return: ContainerComponentDefinition
        """
        component_source = ComponentSource.from_source(
            spec_file, package_zip, amlignore_file=amlignore_file, logger=self.logger)
        if component_source.is_local_source():
            self._validate_component(component_source)

        register_params = {
            'anonymous_registration': False,
            'validate_only': False,
            'set_as_default': set_as_default,
            'version': version
        }

        with ComponentSourceParams(component_source).create() as params:
            register_params.update(**params)
            component = self.imp.register(**register_params)

        return _dto_2_definition(component, self.workspace)

    def validate(self, spec_file, package_zip):
        """Validate a component.

        :param spec_file: The component spec file. Accepts either a local file path, a GitHub url,
                            or a relative path inside the package specified by --package-zip.
        :type spec_file: str
        :param package_zip: The zip package contains the component spec and implementation code.
                            Currently only accepts url to a DevOps build drop.
        :type package_zip: str
        :return: ContainerComponentDefinition
        """
        component_source = ComponentSource.from_source(spec_file, package_zip, logger=self.logger)
        component = self._validate_component(component_source)
        return _dto_2_definition(component, self.workspace)

    def list(self, include_disabled, continuation_header=None):
        """Return a list of components in the workspace.

        :param include_disabled: Include disabled components in list result
        :param continuation_header: When not all components are returned, use this to list again.
        :return: A list of ContainerComponentDefinition.
        :rtype: builtin.list[ContainerComponentDefinition]
        """
        paginated_component = self.imp.list(include_disabled=include_disabled, continuation_header=continuation_header)

        components = paginated_component.value
        component_definitions = []
        for component in components:
            component_definitions.append(_dto_2_definition(component, self.workspace))

        if paginated_component.continuation_token:
            continuation_header = {'continuationToken': paginated_component.continuation_token}
            component_definitions += self.list(
                include_disabled=include_disabled,
                continuation_header=continuation_header
            )
        return component_definitions

    def get(self, name, namespace, version=None):
        """Return the component object.

        :param name: The name of the component to return.
        :type name: str
        :param namespace: The namespace of the component to return.
        :type namespace: str
        :param version: The version of the component to return.
        :type version: str
        :return: ContainerComponentDefinition
        """
        namespace = namespace or _get_default_namespace()
        component = self.imp.get(name=name, namespace=namespace, version=version)
        return _dto_2_definition(component, self.workspace)

    def enable(self, name, namespace):
        """Enable a component.

        :param name: The name of the component.
        :type name: str
        :param namespace: The namespace of the component.
        :type namespace: str
        :return: ContainerComponentDefinition
        """
        namespace = namespace or _get_default_namespace()
        component = self.imp.enable(name=name, namespace=namespace)
        return _dto_2_definition(component, self.workspace)

    def disable(self, name, namespace):
        """Disable a component.

        :param name: The name of the component.
        :type name: str
        :param namespace: The namespace of the component.
        :type namespace: str
        :return: ContainerComponentDefinition
        """
        namespace = namespace or _get_default_namespace()
        component = self.imp.disable(name=name, namespace=namespace)
        return _dto_2_definition(component, self.workspace)

    def set_default_version(self, name, namespace, version):
        """Set a component's default version.

        :param name: The name of the component.
        :type name: str
        :param version: The version to be set as default.
        :type name: str
        :param namespace: The namespace of the component.
        :type namespace: str
        :return: ContainerComponentDefinition
        """
        namespace = namespace or _get_default_namespace()
        component = self.imp.set_default_version(name=name, namespace=namespace, version=version)
        return _dto_2_definition(component, self.workspace)

    def download(self, name, namespace, version, target_dir, overwrite, include_component_spec=True):
        """Download a component to a local folder.

        :param name: The name of the component.
        :type name: str
        :param namespace: The namespace of the component.
        :type name: str
        :param version: The version of the component.
        :type version: str
        :param target_dir: The directory which you download to.
        :type version: str
        :param overwrite: Set true to overwrite any exist files, otherwise false.
        :type overwrite: bool
        :param include_component_spec: Set true to download component spec file along with the snapshot.
        :type include_component_spec: bool
        :return: The component file path.
        :rtype: dict
        """
        namespace = namespace or _get_default_namespace()
        base_filename = "{0}-{1}-{2}-{3}".format(
            self.imp._workspace.service_context.workspace_name,
            name,
            namespace,
            version or 'default',
        )

        file_path = {}

        if include_component_spec:
            # download component spec
            module_yaml = self.get_module_yaml(name, namespace, version)
            module_spec_file_name = _write_file_to_local(module_yaml, target_dir=target_dir,
                                                         file_name=base_filename + ".yaml", overwrite=overwrite,
                                                         logger=self.logger)
            file_path['module_spec'] = module_spec_file_name

        # download snapshot
        snapshot_url = self.get_snapshot_url(name, namespace, version)
        snapshot_filename = _download_file_to_local(snapshot_url, target_dir=target_dir,
                                                    file_name=base_filename + ".zip", overwrite=overwrite,
                                                    logger=self.logger)
        file_path['snapshot'] = snapshot_filename
        return file_path

    def get_module_yaml(self, name, namespace, version):
        """Get component yaml of component.

        :param name: The name of the component.
        :type name: str
        :param version: The version to be set as default.
        :type name: str
        :param namespace: The namespace of the component.
        :type namespace: str
        :return: yaml content
        """
        yaml = self.imp.get_module_yaml(name=name, namespace=namespace, version=version)
        return yaml

    def get_snapshot_url(self, name, namespace, version):
        """Get a component snapshot download url.

        :param name: The name of the component.
        :type name: str
        :param namespace: The namespace of the component.
        :type namespace: str
        :param version: The version of the component.
        :type version: str
        :return: The component snapshot url.
        """
        snapshot_url = self.imp.get_snapshot_url(name=name, namespace=namespace, version=version)
        return snapshot_url

    def get_snapshot_url_by_id(self, component_id):
        """Get a component snapshot download url by id.

        :param component_id: component version id
        :return: The component snapshot url.
        """
        snapshot_url = self.imp.get_snapshot_url_by_id(component_id=component_id)
        return snapshot_url
