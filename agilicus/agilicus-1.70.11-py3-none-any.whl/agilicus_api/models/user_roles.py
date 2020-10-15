# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.10.15
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class UserRoles(object):
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
        'user_id': 'str',
        'roles': 'Roles'
    }

    attribute_map = {
        'user_id': 'user_id',
        'roles': 'roles'
    }

    def __init__(self, user_id=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """UserRoles - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._roles = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if roles is not None:
            self.roles = roles

    @property
    def user_id(self):
        """Gets the user_id of this UserRoles.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The user_id of this UserRoles.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserRoles.

        Unique identifier  # noqa: E501

        :param user_id: The user_id of this UserRoles.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def roles(self):
        """Gets the roles of this UserRoles.  # noqa: E501


        :return: The roles of this UserRoles.  # noqa: E501
        :rtype: Roles
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserRoles.


        :param roles: The roles of this UserRoles.  # noqa: E501
        :type: Roles
        """

        self._roles = roles

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
        if not isinstance(other, UserRoles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRoles):
            return True

        return self.to_dict() != other.to_dict()
