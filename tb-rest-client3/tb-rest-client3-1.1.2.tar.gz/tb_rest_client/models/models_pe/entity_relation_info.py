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


class EntityRelationInfo(object):
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
        'additional_info': 'str',
        '_from': 'EntityId',
        'from_name': 'str',
        'to': 'EntityId',
        'to_name': 'str',
        'type': 'str',
        'type_group': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        '_from': 'from',
        'from_name': 'fromName',
        'to': 'to',
        'to_name': 'toName',
        'type': 'type',
        'type_group': 'typeGroup'
    }

    def __init__(self, additional_info=None, _from=None, from_name=None, to=None, to_name=None, type=None, type_group=None):  # noqa: E501
        """EntityRelationInfo - a model defined in Swagger"""  # noqa: E501

        self._additional_info = None
        self.__from = None
        self._from_name = None
        self._to = None
        self._to_name = None
        self._type = None
        self._type_group = None
        self.discriminator = None

        if additional_info is not None:
            self.additional_info = additional_info
        if _from is not None:
            self._from = _from
        if from_name is not None:
            self.from_name = from_name
        if to is not None:
            self.to = to
        if to_name is not None:
            self.to_name = to_name
        if type is not None:
            self.type = type
        if type_group is not None:
            self.type_group = type_group

    @property
    def additional_info(self):
        """Gets the additional_info of this EntityRelationInfo.  # noqa: E501


        :return: The additional_info of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this EntityRelationInfo.


        :param additional_info: The additional_info of this EntityRelationInfo.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def _from(self):
        """Gets the _from of this EntityRelationInfo.  # noqa: E501


        :return: The _from of this EntityRelationInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EntityRelationInfo.


        :param _from: The _from of this EntityRelationInfo.  # noqa: E501
        :type: EntityId
        """

        self.__from = _from

    @property
    def from_name(self):
        """Gets the from_name of this EntityRelationInfo.  # noqa: E501


        :return: The from_name of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this EntityRelationInfo.


        :param from_name: The from_name of this EntityRelationInfo.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def to(self):
        """Gets the to of this EntityRelationInfo.  # noqa: E501


        :return: The to of this EntityRelationInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EntityRelationInfo.


        :param to: The to of this EntityRelationInfo.  # noqa: E501
        :type: EntityId
        """

        self._to = to

    @property
    def to_name(self):
        """Gets the to_name of this EntityRelationInfo.  # noqa: E501


        :return: The to_name of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """Sets the to_name of this EntityRelationInfo.


        :param to_name: The to_name of this EntityRelationInfo.  # noqa: E501
        :type: str
        """

        self._to_name = to_name

    @property
    def type(self):
        """Gets the type of this EntityRelationInfo.  # noqa: E501


        :return: The type of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityRelationInfo.


        :param type: The type of this EntityRelationInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_group(self):
        """Gets the type_group of this EntityRelationInfo.  # noqa: E501


        :return: The type_group of this EntityRelationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type_group

    @type_group.setter
    def type_group(self, type_group):
        """Sets the type_group of this EntityRelationInfo.


        :param type_group: The type_group of this EntityRelationInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMMON", "ALARM", "DASHBOARD", "TO_ENTITY_GROUP", "FROM_ENTITY_GROUP", "RULE_CHAIN", "RULE_NODE"]  # noqa: E501
        if type_group not in allowed_values:
            raise ValueError(
                "Invalid value for `type_group` ({0}), must be one of {1}"  # noqa: E501
                .format(type_group, allowed_values)
            )

        self._type_group = type_group

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
        if issubclass(EntityRelationInfo, dict):
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
        if not isinstance(other, EntityRelationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
