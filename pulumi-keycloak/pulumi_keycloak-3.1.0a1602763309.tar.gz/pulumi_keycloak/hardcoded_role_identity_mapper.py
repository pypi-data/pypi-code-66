# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['HardcodedRoleIdentityMapper']


class HardcodedRoleIdentityMapper(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extra_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 identity_provider_alias: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 realm: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a HardcodedRoleIdentityMapper resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_provider_alias: IDP Alias
        :param pulumi.Input[str] name: IDP Mapper Name
        :param pulumi.Input[str] realm: Realm Name
        :param pulumi.Input[str] role: Role Name
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

            __props__['extra_config'] = extra_config
            if identity_provider_alias is None:
                raise TypeError("Missing required property 'identity_provider_alias'")
            __props__['identity_provider_alias'] = identity_provider_alias
            __props__['name'] = name
            if realm is None:
                raise TypeError("Missing required property 'realm'")
            __props__['realm'] = realm
            __props__['role'] = role
        super(HardcodedRoleIdentityMapper, __self__).__init__(
            'keycloak:index/hardcodedRoleIdentityMapper:HardcodedRoleIdentityMapper',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            extra_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            identity_provider_alias: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            realm: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None) -> 'HardcodedRoleIdentityMapper':
        """
        Get an existing HardcodedRoleIdentityMapper resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_provider_alias: IDP Alias
        :param pulumi.Input[str] name: IDP Mapper Name
        :param pulumi.Input[str] realm: Realm Name
        :param pulumi.Input[str] role: Role Name
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["extra_config"] = extra_config
        __props__["identity_provider_alias"] = identity_provider_alias
        __props__["name"] = name
        __props__["realm"] = realm
        __props__["role"] = role
        return HardcodedRoleIdentityMapper(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extraConfig")
    def extra_config(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "extra_config")

    @property
    @pulumi.getter(name="identityProviderAlias")
    def identity_provider_alias(self) -> pulumi.Output[str]:
        """
        IDP Alias
        """
        return pulumi.get(self, "identity_provider_alias")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        IDP Mapper Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def realm(self) -> pulumi.Output[str]:
        """
        Realm Name
        """
        return pulumi.get(self, "realm")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        Role Name
        """
        return pulumi.get(self, "role")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

