# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['RealmEvents']


class RealmEvents(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_events_details_enabled: Optional[pulumi.Input[bool]] = None,
                 admin_events_enabled: Optional[pulumi.Input[bool]] = None,
                 enabled_event_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 events_enabled: Optional[pulumi.Input[bool]] = None,
                 events_expiration: Optional[pulumi.Input[int]] = None,
                 events_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows for managing Realm Events settings within Keycloak.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        realm_events = keycloak.RealmEvents("realmEvents",
            realm_id=realm.id,
            events_enabled=True,
            events_expiration=3600,
            admin_events_enabled=True,
            admin_events_details_enabled=True,
            enabled_event_types=[
                "LOGIN",
                "LOGOUT",
            ],
            events_listeners=["jboss-logging"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_events_details_enabled: When `true`, saved admin events will included detailed information for create/update requests. Defaults to `false`.
        :param pulumi.Input[bool] admin_events_enabled: When `true`, admin events are saved to the database, making them available through the admin console. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_event_types: The event types that will be saved to the database. Omitting this field enables all event types. Defaults to `[]` or all event types.
        :param pulumi.Input[bool] events_enabled: When `true`, events from `enabled_event_types` are saved to the database, making them available through the admin console. Defaults to `false`.
        :param pulumi.Input[int] events_expiration: The amount of time in seconds events will be saved in the database. Defaults to `0` or never.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] events_listeners: The event listeners that events should be sent to. Defaults to `[]` or none. Note that new realms enable the `jboss-logging` listener by default, and this resource will remove that unless it is specified.
        :param pulumi.Input[str] realm_id: The name of the realm the event settings apply to.
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

            __props__['admin_events_details_enabled'] = admin_events_details_enabled
            __props__['admin_events_enabled'] = admin_events_enabled
            __props__['enabled_event_types'] = enabled_event_types
            __props__['events_enabled'] = events_enabled
            __props__['events_expiration'] = events_expiration
            __props__['events_listeners'] = events_listeners
            if realm_id is None:
                raise TypeError("Missing required property 'realm_id'")
            __props__['realm_id'] = realm_id
        super(RealmEvents, __self__).__init__(
            'keycloak:index/realmEvents:RealmEvents',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_events_details_enabled: Optional[pulumi.Input[bool]] = None,
            admin_events_enabled: Optional[pulumi.Input[bool]] = None,
            enabled_event_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            events_enabled: Optional[pulumi.Input[bool]] = None,
            events_expiration: Optional[pulumi.Input[int]] = None,
            events_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            realm_id: Optional[pulumi.Input[str]] = None) -> 'RealmEvents':
        """
        Get an existing RealmEvents resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_events_details_enabled: When `true`, saved admin events will included detailed information for create/update requests. Defaults to `false`.
        :param pulumi.Input[bool] admin_events_enabled: When `true`, admin events are saved to the database, making them available through the admin console. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_event_types: The event types that will be saved to the database. Omitting this field enables all event types. Defaults to `[]` or all event types.
        :param pulumi.Input[bool] events_enabled: When `true`, events from `enabled_event_types` are saved to the database, making them available through the admin console. Defaults to `false`.
        :param pulumi.Input[int] events_expiration: The amount of time in seconds events will be saved in the database. Defaults to `0` or never.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] events_listeners: The event listeners that events should be sent to. Defaults to `[]` or none. Note that new realms enable the `jboss-logging` listener by default, and this resource will remove that unless it is specified.
        :param pulumi.Input[str] realm_id: The name of the realm the event settings apply to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_events_details_enabled"] = admin_events_details_enabled
        __props__["admin_events_enabled"] = admin_events_enabled
        __props__["enabled_event_types"] = enabled_event_types
        __props__["events_enabled"] = events_enabled
        __props__["events_expiration"] = events_expiration
        __props__["events_listeners"] = events_listeners
        __props__["realm_id"] = realm_id
        return RealmEvents(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminEventsDetailsEnabled")
    def admin_events_details_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, saved admin events will included detailed information for create/update requests. Defaults to `false`.
        """
        return pulumi.get(self, "admin_events_details_enabled")

    @property
    @pulumi.getter(name="adminEventsEnabled")
    def admin_events_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, admin events are saved to the database, making them available through the admin console. Defaults to `false`.
        """
        return pulumi.get(self, "admin_events_enabled")

    @property
    @pulumi.getter(name="enabledEventTypes")
    def enabled_event_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The event types that will be saved to the database. Omitting this field enables all event types. Defaults to `[]` or all event types.
        """
        return pulumi.get(self, "enabled_event_types")

    @property
    @pulumi.getter(name="eventsEnabled")
    def events_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, events from `enabled_event_types` are saved to the database, making them available through the admin console. Defaults to `false`.
        """
        return pulumi.get(self, "events_enabled")

    @property
    @pulumi.getter(name="eventsExpiration")
    def events_expiration(self) -> pulumi.Output[Optional[int]]:
        """
        The amount of time in seconds events will be saved in the database. Defaults to `0` or never.
        """
        return pulumi.get(self, "events_expiration")

    @property
    @pulumi.getter(name="eventsListeners")
    def events_listeners(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The event listeners that events should be sent to. Defaults to `[]` or none. Note that new realms enable the `jboss-logging` listener by default, and this resource will remove that unless it is specified.
        """
        return pulumi.get(self, "events_listeners")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The name of the realm the event settings apply to.
        """
        return pulumi.get(self, "realm_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

