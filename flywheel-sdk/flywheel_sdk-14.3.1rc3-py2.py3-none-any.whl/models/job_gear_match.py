# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 14.3.1-rc.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class JobGearMatch(object):

    swagger_types = {
        'group': 'list[str]',
        'gear_name': 'list[str]',
        'tag': 'list[str]',
        'compute_provider': 'list[str]'
    }

    attribute_map = {
        'group': 'group',
        'gear_name': 'gear-name',
        'tag': 'tag',
        'compute_provider': 'compute-provider'
    }

    rattribute_map = {
        'group': 'group',
        'gear-name': 'gear_name',
        'tag': 'tag',
        'compute-provider': 'compute_provider'
    }

    def __init__(self, group=None, gear_name=None, tag=None, compute_provider=None):  # noqa: E501
        """JobGearMatch - a model defined in Swagger"""
        super(JobGearMatch, self).__init__()

        self._group = None
        self._gear_name = None
        self._tag = None
        self._compute_provider = None
        self.discriminator = None
        self.alt_discriminator = None

        if group is not None:
            self.group = group
        if gear_name is not None:
            self.gear_name = gear_name
        if tag is not None:
            self.tag = tag
        if compute_provider is not None:
            self.compute_provider = compute_provider

    @property
    def group(self):
        """Gets the group of this JobGearMatch.

        A set of groups that are in the hierarchy of an input or destination

        :return: The group of this JobGearMatch.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this JobGearMatch.

        A set of groups that are in the hierarchy of an input or destination

        :param group: The group of this JobGearMatch.  # noqa: E501
        :type: list[str]
        """

        self._group = group

    @property
    def gear_name(self):
        """Gets the gear_name of this JobGearMatch.

        A set of gear.name matches

        :return: The gear_name of this JobGearMatch.
        :rtype: list[str]
        """
        return self._gear_name

    @gear_name.setter
    def gear_name(self, gear_name):
        """Sets the gear_name of this JobGearMatch.

        A set of gear.name matches

        :param gear_name: The gear_name of this JobGearMatch.  # noqa: E501
        :type: list[str]
        """

        self._gear_name = gear_name

    @property
    def tag(self):
        """Gets the tag of this JobGearMatch.

        A set of job.tags matches

        :return: The tag of this JobGearMatch.
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this JobGearMatch.

        A set of job.tags matches

        :param tag: The tag of this JobGearMatch.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def compute_provider(self):
        """Gets the compute_provider of this JobGearMatch.

        A set of compute providers to match

        :return: The compute_provider of this JobGearMatch.
        :rtype: list[str]
        """
        return self._compute_provider

    @compute_provider.setter
    def compute_provider(self, compute_provider):
        """Sets the compute_provider of this JobGearMatch.

        A set of compute providers to match

        :param compute_provider: The compute_provider of this JobGearMatch.  # noqa: E501
        :type: list[str]
        """

        self._compute_provider = compute_provider


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobGearMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result
