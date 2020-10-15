# coding: utf-8

"""
    Robot API

    Robot REST API  # noqa: E501

    OpenAPI spec version: 1.8.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pdhttp.models.point import Point  # noqa: F401,E501
from pdhttp.models.rotation import Rotation  # noqa: F401,E501


class Position(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'point': 'Point',
        'rotation': 'Rotation',
        'blend': 'float',
        'actions': 'list[object]'
    }

    attribute_map = {
        'point': 'point',
        'rotation': 'rotation',
        'blend': 'blend',
        'actions': 'actions'
    }

    def __init__(self, point=None, rotation=None, blend=0.0, actions=None):  # noqa: E501
        """Position - a model defined in Swagger"""  # noqa: E501

        self._point = None
        self._rotation = None
        self._blend = None
        self._actions = None
        self.discriminator = None

        if point is not None:
            self.point = point
        if rotation is not None:
            self.rotation = rotation
        if blend is not None:
            self.blend = blend
        if actions is not None:
            self.actions = actions

    @property
    def point(self):
        """Gets the point of this Position.  # noqa: E501


        :return: The point of this Position.  # noqa: E501
        :rtype: Point
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this Position.


        :param point: The point of this Position.  # noqa: E501
        :type: Point
        """

        self._point = point

    @property
    def rotation(self):
        """Gets the rotation of this Position.  # noqa: E501


        :return: The rotation of this Position.  # noqa: E501
        :rtype: Rotation
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this Position.


        :param rotation: The rotation of this Position.  # noqa: E501
        :type: Rotation
        """

        self._rotation = rotation

    @property
    def blend(self):
        """Gets the blend of this Position.  # noqa: E501


        :return: The blend of this Position.  # noqa: E501
        :rtype: float
        """
        return self._blend

    @blend.setter
    def blend(self, blend):
        """Sets the blend of this Position.


        :param blend: The blend of this Position.  # noqa: E501
        :type: float
        """
        if blend is not None and blend < 0:  # noqa: E501
            raise ValueError("Invalid value for `blend`, must be a value greater than or equal to `0`")  # noqa: E501

        self._blend = blend

    @property
    def actions(self):
        """Gets the actions of this Position.  # noqa: E501


        :return: The actions of this Position.  # noqa: E501
        :rtype: list[object]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Position.


        :param actions: The actions of this Position.  # noqa: E501
        :type: list[object]
        """

        self._actions = actions

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
        if issubclass(Position, dict):
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
        if not isinstance(other, Position):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
