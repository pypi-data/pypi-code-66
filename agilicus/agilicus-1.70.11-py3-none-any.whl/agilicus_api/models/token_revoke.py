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


class TokenRevoke(object):
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
        'token': 'str',
        'all_sessions': 'bool'
    }

    attribute_map = {
        'token': 'token',
        'all_sessions': 'all_sessions'
    }

    def __init__(self, token=None, all_sessions=None, local_vars_configuration=None):  # noqa: E501
        """TokenRevoke - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._all_sessions = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if all_sessions is not None:
            self.all_sessions = all_sessions

    @property
    def token(self):
        """Gets the token of this TokenRevoke.  # noqa: E501

        token string  # noqa: E501

        :return: The token of this TokenRevoke.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenRevoke.

        token string  # noqa: E501

        :param token: The token of this TokenRevoke.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def all_sessions(self):
        """Gets the all_sessions of this TokenRevoke.  # noqa: E501

        revoke all sessions associated with token  # noqa: E501

        :return: The all_sessions of this TokenRevoke.  # noqa: E501
        :rtype: bool
        """
        return self._all_sessions

    @all_sessions.setter
    def all_sessions(self, all_sessions):
        """Sets the all_sessions of this TokenRevoke.

        revoke all sessions associated with token  # noqa: E501

        :param all_sessions: The all_sessions of this TokenRevoke.  # noqa: E501
        :type: bool
        """

        self._all_sessions = all_sessions

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
        if not isinstance(other, TokenRevoke):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenRevoke):
            return True

        return self.to_dict() != other.to_dict()
