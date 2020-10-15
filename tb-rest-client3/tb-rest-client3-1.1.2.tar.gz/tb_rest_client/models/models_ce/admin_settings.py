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


class AdminSettings(object):
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
        'created_time': 'int',
        'id': 'AdminSettingsId',
        'json_value': 'str',
        'key': 'str'
    }

    attribute_map = {
        'created_time': 'createdTime',
        'id': 'id',
        'json_value': 'jsonValue',
        'key': 'key'
    }

    def __init__(self, created_time=None, id=None, json_value=None, key=None):  # noqa: E501
        """AdminSettings - a model defined in Swagger"""  # noqa: E501

        self._created_time = None
        self._id = None
        self._json_value = None
        self._key = None
        self.discriminator = None

        if created_time is not None:
            self.created_time = created_time
        if id is not None:
            self.id = id
        if json_value is not None:
            self.json_value = json_value
        if key is not None:
            self.key = key

    @property
    def created_time(self):
        """Gets the created_time of this AdminSettings.  # noqa: E501


        :return: The created_time of this AdminSettings.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AdminSettings.


        :param created_time: The created_time of this AdminSettings.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this AdminSettings.  # noqa: E501


        :return: The id of this AdminSettings.  # noqa: E501
        :rtype: AdminSettingsId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminSettings.


        :param id: The id of this AdminSettings.  # noqa: E501
        :type: AdminSettingsId
        """

        self._id = id

    @property
    def json_value(self):
        """Gets the json_value of this AdminSettings.  # noqa: E501


        :return: The json_value of this AdminSettings.  # noqa: E501
        :rtype: str
        """
        return self._json_value

    @json_value.setter
    def json_value(self, json_value):
        """Sets the json_value of this AdminSettings.


        :param json_value: The json_value of this AdminSettings.  # noqa: E501
        :type: str
        """

        self._json_value = json_value

    @property
    def key(self):
        """Gets the key of this AdminSettings.  # noqa: E501


        :return: The key of this AdminSettings.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AdminSettings.


        :param key: The key of this AdminSettings.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(AdminSettings, dict):
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
        if not isinstance(other, AdminSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
