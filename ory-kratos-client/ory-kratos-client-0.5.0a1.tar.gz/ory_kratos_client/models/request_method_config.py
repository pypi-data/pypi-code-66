# coding: utf-8

"""
    Ory Kratos

    Welcome to the ORY Kratos HTTP API documentation!  # noqa: E501

    The version of the OpenAPI document: v0.4.6-alpha.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_kratos_client.configuration import Configuration


class RequestMethodConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'action': 'str',
        'fields': 'list[FormField]',
        'messages': 'list[Message]',
        'method': 'str'
    }

    attribute_map = {
        'action': 'action',
        'fields': 'fields',
        'messages': 'messages',
        'method': 'method'
    }

    def __init__(self, action=None, fields=None, messages=None, method=None, local_vars_configuration=None):  # noqa: E501
        """RequestMethodConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._fields = None
        self._messages = None
        self._method = None
        self.discriminator = None

        self.action = action
        self.fields = fields
        if messages is not None:
            self.messages = messages
        self.method = method

    @property
    def action(self):
        """Gets the action of this RequestMethodConfig.  # noqa: E501

        Action should be used as the form action URL `<form action=\"{{ .Action }}\" method=\"post\">`.  # noqa: E501

        :return: The action of this RequestMethodConfig.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RequestMethodConfig.

        Action should be used as the form action URL `<form action=\"{{ .Action }}\" method=\"post\">`.  # noqa: E501

        :param action: The action of this RequestMethodConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def fields(self):
        """Gets the fields of this RequestMethodConfig.  # noqa: E501

        Fields contains multiple fields  # noqa: E501

        :return: The fields of this RequestMethodConfig.  # noqa: E501
        :rtype: list[FormField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this RequestMethodConfig.

        Fields contains multiple fields  # noqa: E501

        :param fields: The fields of this RequestMethodConfig.  # noqa: E501
        :type: list[FormField]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def messages(self):
        """Gets the messages of this RequestMethodConfig.  # noqa: E501


        :return: The messages of this RequestMethodConfig.  # noqa: E501
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this RequestMethodConfig.


        :param messages: The messages of this RequestMethodConfig.  # noqa: E501
        :type: list[Message]
        """

        self._messages = messages

    @property
    def method(self):
        """Gets the method of this RequestMethodConfig.  # noqa: E501

        Method is the form method (e.g. POST)  # noqa: E501

        :return: The method of this RequestMethodConfig.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this RequestMethodConfig.

        Method is the form method (e.g. POST)  # noqa: E501

        :param method: The method of this RequestMethodConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and method is None:  # noqa: E501
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestMethodConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestMethodConfig):
            return True

        return self.to_dict() != other.to_dict()
