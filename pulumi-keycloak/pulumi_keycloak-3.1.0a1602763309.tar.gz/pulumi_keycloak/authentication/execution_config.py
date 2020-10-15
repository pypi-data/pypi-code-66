# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ExecutionConfig']


class ExecutionConfig(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 execution_id: Optional[pulumi.Input[str]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows for managing an authentication execution's configuration. If a particular authentication execution supports additional
        configuration (such as with the `identity-provider-redirector` execution), this can be managed with this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        flow = keycloak.authentication.Flow("flow",
            realm_id=realm.id,
            alias="my-flow-alias")
        execution = keycloak.authentication.Execution("execution",
            realm_id=realm.id,
            parent_flow_alias=flow.alias,
            authenticator="identity-provider-redirector")
        config = keycloak.authentication.ExecutionConfig("config",
            realm_id=realm.id,
            execution_id=execution.id,
            alias="my-config-alias",
            config={
                "defaultProvider": "my-config-default-idp",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The name of the configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The configuration. Keys are specific to each configurable authentication execution and not checked when applying.
        :param pulumi.Input[str] execution_id: The authentication execution this configuration is attached to.
        :param pulumi.Input[str] realm_id: The realm the authentication execution exists in.
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

            if alias is None:
                raise TypeError("Missing required property 'alias'")
            __props__['alias'] = alias
            if config is None:
                raise TypeError("Missing required property 'config'")
            __props__['config'] = config
            if execution_id is None:
                raise TypeError("Missing required property 'execution_id'")
            __props__['execution_id'] = execution_id
            if realm_id is None:
                raise TypeError("Missing required property 'realm_id'")
            __props__['realm_id'] = realm_id
        super(ExecutionConfig, __self__).__init__(
            'keycloak:authentication/executionConfig:ExecutionConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alias: Optional[pulumi.Input[str]] = None,
            config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            execution_id: Optional[pulumi.Input[str]] = None,
            realm_id: Optional[pulumi.Input[str]] = None) -> 'ExecutionConfig':
        """
        Get an existing ExecutionConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The name of the configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The configuration. Keys are specific to each configurable authentication execution and not checked when applying.
        :param pulumi.Input[str] execution_id: The authentication execution this configuration is attached to.
        :param pulumi.Input[str] realm_id: The realm the authentication execution exists in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["alias"] = alias
        __props__["config"] = config
        __props__["execution_id"] = execution_id
        __props__["realm_id"] = realm_id
        return ExecutionConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The name of the configuration.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The configuration. Keys are specific to each configurable authentication execution and not checked when applying.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="executionId")
    def execution_id(self) -> pulumi.Output[str]:
        """
        The authentication execution this configuration is attached to.
        """
        return pulumi.get(self, "execution_id")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm the authentication execution exists in.
        """
        return pulumi.get(self, "realm_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

