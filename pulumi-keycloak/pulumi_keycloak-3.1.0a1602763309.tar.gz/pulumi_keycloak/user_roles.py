# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['UserRoles']


class UserRoles(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a UserRoles resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] realm_id: The realm this user exists in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: A list of role IDs to map to the user
        :param pulumi.Input[str] user_id: The ID of the user this resource should manage roles for.
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

            if realm_id is None:
                raise TypeError("Missing required property 'realm_id'")
            __props__['realm_id'] = realm_id
            if role_ids is None:
                raise TypeError("Missing required property 'role_ids'")
            __props__['role_ids'] = role_ids
            if user_id is None:
                raise TypeError("Missing required property 'user_id'")
            __props__['user_id'] = user_id
        super(UserRoles, __self__).__init__(
            'keycloak:index/userRoles:UserRoles',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            realm_id: Optional[pulumi.Input[str]] = None,
            role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'UserRoles':
        """
        Get an existing UserRoles resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] realm_id: The realm this user exists in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: A list of role IDs to map to the user
        :param pulumi.Input[str] user_id: The ID of the user this resource should manage roles for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["realm_id"] = realm_id
        __props__["role_ids"] = role_ids
        __props__["user_id"] = user_id
        return UserRoles(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm this user exists in.
        """
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of role IDs to map to the user
        """
        return pulumi.get(self, "role_ids")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The ID of the user this resource should manage roles for.
        """
        return pulumi.get(self, "user_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

