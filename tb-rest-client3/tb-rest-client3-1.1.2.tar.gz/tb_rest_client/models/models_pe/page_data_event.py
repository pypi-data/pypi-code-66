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


class PageDataEvent(object):
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
        'data': 'list[Event]',
        'has_next': 'bool',
        'total_elements': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'data': 'data',
        'has_next': 'hasNext',
        'total_elements': 'totalElements',
        'total_pages': 'totalPages'
    }

    def __init__(self, data=None, has_next=None, total_elements=None, total_pages=None):  # noqa: E501
        """PageDataEvent - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._has_next = None
        self._total_elements = None
        self._total_pages = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if has_next is not None:
            self.has_next = has_next
        if total_elements is not None:
            self.total_elements = total_elements
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def data(self):
        """Gets the data of this PageDataEvent.  # noqa: E501


        :return: The data of this PageDataEvent.  # noqa: E501
        :rtype: list[Event]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PageDataEvent.


        :param data: The data of this PageDataEvent.  # noqa: E501
        :type: list[Event]
        """

        self._data = data

    @property
    def has_next(self):
        """Gets the has_next of this PageDataEvent.  # noqa: E501


        :return: The has_next of this PageDataEvent.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this PageDataEvent.


        :param has_next: The has_next of this PageDataEvent.  # noqa: E501
        :type: bool
        """

        self._has_next = has_next

    @property
    def total_elements(self):
        """Gets the total_elements of this PageDataEvent.  # noqa: E501


        :return: The total_elements of this PageDataEvent.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this PageDataEvent.


        :param total_elements: The total_elements of this PageDataEvent.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    @property
    def total_pages(self):
        """Gets the total_pages of this PageDataEvent.  # noqa: E501


        :return: The total_pages of this PageDataEvent.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PageDataEvent.


        :param total_pages: The total_pages of this PageDataEvent.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

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
        if issubclass(PageDataEvent, dict):
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
        if not isinstance(other, PageDataEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
