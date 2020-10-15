# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Role']


class Role(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 composite_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows for creating and managing roles within Keycloak.

        Roles allow you define privileges within Keycloak and map them to users and groups.

        ## Example Usage
        ### Realm Role)

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        realm_role = keycloak.Role("realmRole",
            realm_id=realm.id,
            description="My Realm Role")
        ```
        ### Client Role)

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        openid_client = keycloak.openid.Client("openidClient",
            realm_id=realm.id,
            client_id="client",
            enabled=True,
            access_type="CONFIDENTIAL",
            valid_redirect_uris=["http://localhost:8080/openid-callback"])
        client_role = keycloak.Role("clientRole",
            realm_id=realm.id,
            client_id=keycloak_client["openid_client"]["id"],
            description="My Client Role")
        ```
        ### Composite Role)

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        # realm roles
        create_role = keycloak.Role("createRole", realm_id=realm.id)
        read_role = keycloak.Role("readRole", realm_id=realm.id)
        update_role = keycloak.Role("updateRole", realm_id=realm.id)
        delete_role = keycloak.Role("deleteRole", realm_id=realm.id)
        # client role
        openid_client = keycloak.openid.Client("openidClient",
            realm_id=realm.id,
            client_id="client",
            enabled=True,
            access_type="CONFIDENTIAL",
            valid_redirect_uris=["http://localhost:8080/openid-callback"])
        client_role = keycloak.Role("clientRole",
            realm_id=realm.id,
            client_id=keycloak_client["openid_client"]["id"],
            description="My Client Role")
        admin_role = keycloak.Role("adminRole",
            realm_id=realm.id,
            composite_roles=[
                create_role.id,
                read_role.id,
                update_role.id,
                delete_role.id,
                client_role.id,
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: When specified, this role will be created as a client role attached to the client with the provided ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] composite_roles: When specified, this role will be a composite role, composed of all roles that have an ID present within this list.
        :param pulumi.Input[str] description: The description of the role
        :param pulumi.Input[str] name: The name of the role
        :param pulumi.Input[str] realm_id: The realm this role exists within.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['client_id'] = client_id
            __props__['composite_roles'] = composite_roles
            __props__['description'] = description
            __props__['name'] = name
            if realm_id is None:
                raise TypeError("Missing required property 'realm_id'")
            __props__['realm_id'] = realm_id
        super(Role, __self__).__init__(
            'keycloak:index/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            composite_roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_id: When specified, this role will be created as a client role attached to the client with the provided ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] composite_roles: When specified, this role will be a composite role, composed of all roles that have an ID present within this list.
        :param pulumi.Input[str] description: The description of the role
        :param pulumi.Input[str] name: The name of the role
        :param pulumi.Input[str] realm_id: The realm this role exists within.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["client_id"] = client_id
        __props__["composite_roles"] = composite_roles
        __props__["description"] = description
        __props__["name"] = name
        __props__["realm_id"] = realm_id
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[str]]:
        """
        When specified, this role will be created as a client role attached to the client with the provided ID
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="compositeRoles")
    def composite_roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        When specified, this role will be a composite role, composed of all roles that have an ID present within this list.
        """
        return pulumi.get(self, "composite_roles")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the role
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the role
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm this role exists within.
        """
        return pulumi.get(self, "realm_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

