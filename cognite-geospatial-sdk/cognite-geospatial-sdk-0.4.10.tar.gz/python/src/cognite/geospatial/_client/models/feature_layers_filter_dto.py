# coding: utf-8

"""
    Cognite API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: playground
    Contact: support@cognite.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cognite.geospatial._client.configuration import Configuration


class FeatureLayersFilterDTO(object):
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
        'names': 'list[str]'
    }

    attribute_map = {
        'names': 'names'
    }

    def __init__(self, names=None, local_vars_configuration=None):  # noqa: E501
        """FeatureLayersFilterDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._names = None
        self.discriminator = None

        if names is not None:
            self.names = names

    @property
    def names(self):
        """Gets the names of this FeatureLayersFilterDTO.  # noqa: E501

        a list of layer's names  # noqa: E501

        :return: The names of this FeatureLayersFilterDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this FeatureLayersFilterDTO.

        a list of layer's names  # noqa: E501

        :param names: The names of this FeatureLayersFilterDTO.  # noqa: E501
        :type names: list[str]
        """

        self._names = names

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
        if not isinstance(other, FeatureLayersFilterDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureLayersFilterDTO):
            return True

        return self.to_dict() != other.to_dict()
