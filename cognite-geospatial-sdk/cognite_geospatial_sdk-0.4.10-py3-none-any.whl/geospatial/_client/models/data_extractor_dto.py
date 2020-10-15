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


class DataExtractorDTO(object):
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
        'attribute': 'str',
        'min': 'str',
        'max': 'str'
    }

    attribute_map = {
        'attribute': 'attribute',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, attribute=None, min=None, max=None, local_vars_configuration=None):  # noqa: E501
        """DataExtractorDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute = None
        self._min = None
        self._max = None
        self.discriminator = None

        self.attribute = attribute
        self.min = min
        self.max = max

    @property
    def attribute(self):
        """Gets the attribute of this DataExtractorDTO.  # noqa: E501

        the attribute name  # noqa: E501

        :return: The attribute of this DataExtractorDTO.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this DataExtractorDTO.

        the attribute name  # noqa: E501

        :param attribute: The attribute of this DataExtractorDTO.  # noqa: E501
        :type attribute: str
        """
        if self.local_vars_configuration.client_side_validation and attribute is None:  # noqa: E501
            raise ValueError("Invalid value for `attribute`, must not be `None`")  # noqa: E501

        self._attribute = attribute

    @property
    def min(self):
        """Gets the min of this DataExtractorDTO.  # noqa: E501

        the minimum value  # noqa: E501

        :return: The min of this DataExtractorDTO.  # noqa: E501
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this DataExtractorDTO.

        the minimum value  # noqa: E501

        :param min: The min of this DataExtractorDTO.  # noqa: E501
        :type min: str
        """
        if self.local_vars_configuration.client_side_validation and min is None:  # noqa: E501
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def max(self):
        """Gets the max of this DataExtractorDTO.  # noqa: E501

        the maximum value  # noqa: E501

        :return: The max of this DataExtractorDTO.  # noqa: E501
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this DataExtractorDTO.

        the maximum value  # noqa: E501

        :param max: The max of this DataExtractorDTO.  # noqa: E501
        :type max: str
        """
        if self.local_vars_configuration.client_side_validation and max is None:  # noqa: E501
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

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
        if not isinstance(other, DataExtractorDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataExtractorDTO):
            return True

        return self.to_dict() != other.to_dict()
