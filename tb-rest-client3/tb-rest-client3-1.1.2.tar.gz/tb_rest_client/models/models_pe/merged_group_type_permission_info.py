# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import pprint
import re  # noqa: F401

import six


class MergedGroupTypePermissionInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.    
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_group_ids': 'list[EntityGroupId]',
        'has_generic_read': 'bool'
    }

    attribute_map = {
        'entity_group_ids': 'entityGroupIds',
        'has_generic_read': 'hasGenericRead'
    }

    def __init__(self, entity_group_ids=None, has_generic_read=None):  # noqa: E501
        """MergedGroupTypePermissionInfo - a model defined in Swagger"""  # noqa: E501

        self._entity_group_ids = None
        self._has_generic_read = None
        self.discriminator = None

        if entity_group_ids is not None:
            self.entity_group_ids = entity_group_ids
        if has_generic_read is not None:
            self.has_generic_read = has_generic_read

    @property
    def entity_group_ids(self):
        """Gets the entity_group_ids of this MergedGroupTypePermissionInfo.  # noqa: E501


        :return: The entity_group_ids of this MergedGroupTypePermissionInfo.  # noqa: E501
        :rtype: list[EntityGroupId]
        """
        return self._entity_group_ids

    @entity_group_ids.setter
    def entity_group_ids(self, entity_group_ids):
        """Sets the entity_group_ids of this MergedGroupTypePermissionInfo.


        :param entity_group_ids: The entity_group_ids of this MergedGroupTypePermissionInfo.  # noqa: E501
        :type: list[EntityGroupId]
        """

        self._entity_group_ids = entity_group_ids

    @property
    def has_generic_read(self):
        """Gets the has_generic_read of this MergedGroupTypePermissionInfo.  # noqa: E501


        :return: The has_generic_read of this MergedGroupTypePermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_generic_read

    @has_generic_read.setter
    def has_generic_read(self, has_generic_read):
        """Sets the has_generic_read of this MergedGroupTypePermissionInfo.


        :param has_generic_read: The has_generic_read of this MergedGroupTypePermissionInfo.  # noqa: E501
        :type: bool
        """

        self._has_generic_read = has_generic_read

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(MergedGroupTypePermissionInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MergedGroupTypePermissionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
