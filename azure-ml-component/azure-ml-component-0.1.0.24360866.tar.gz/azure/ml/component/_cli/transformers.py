# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from azure.ml.component.core import ComponentDefinition


def component_definition_to_detail_dict(component: ComponentDefinition):
    """Dumps a component definition object into a dict representation, display detail information."""
    return {
        'name': component.name,
        'namespace': component.namespace,
        'moduleID': component.identifier,
        'description': component.description,
        'version': component.version,
        'versions': component.registration_context.all_versions,
        'type': component.type,
        'contact': component.contact,
        'registeredBy': component.creation_context.registered_by,
        'registeredOn': component.creation_context.created_date,
        'lastUpdatedOn': component.creation_context.last_modified_date,
        'source': component.registration_context.source,
        'yamlLink': component.registration_context.yaml_link,
        'helpDocument': component.help_document,
        'status': component.registration_context.status,
        'tags': ', '.join(component.tags) if component.tags else None,
        'shared_scope': component.registration_context.shared_scope,
    }


def component_definition_to_validation_result_dict(component: ComponentDefinition):
    """Dumps a component definition object into a dict representation, display for validation result."""
    return {
        'name': component.name,
        'namespace': component.namespace,
        'description': component.description,
        'version': component.version,
        'type': component.type,
        'contact': component.contact,
        'source': component.registration_context.source,
        'yamlLink': component.registration_context.yaml_link,
        'helpDocument': component.help_document,
        'tags': ', '.join(component.tags) if component.tags else None,
    }


def component_definition_to_summary_dict(component: ComponentDefinition):
    """Dumps a component definition object into a dict representation, display only summary information."""
    return {
        'name': component.name,
        'namespace': component.namespace,
        'defaultVersion': component.registration_context.default_version,
        'tags': ', '.join(component.tags) if component.tags else None,
        'status': component.registration_context.status
    }
