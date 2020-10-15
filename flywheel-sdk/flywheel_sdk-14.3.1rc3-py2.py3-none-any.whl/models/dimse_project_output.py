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


class DimseProjectOutput(object):

    swagger_types = {
        'id': 'str',
        'created': 'datetime',
        'creator': 'str',
        'aet': 'str',
        'project_id': 'str',
        'host': 'str',
        'port': 'int'
    }

    attribute_map = {
        'id': '_id',
        'created': 'created',
        'creator': 'creator',
        'aet': 'aet',
        'project_id': 'project_id',
        'host': 'host',
        'port': 'port'
    }

    rattribute_map = {
        '_id': 'id',
        'created': 'created',
        'creator': 'creator',
        'aet': 'aet',
        'project_id': 'project_id',
        'host': 'host',
        'port': 'port'
    }

    def __init__(self, id=None, created=None, creator=None, aet=None, project_id=None, host=None, port=None):  # noqa: E501
        """DimseProjectOutput - a model defined in Swagger"""
        super(DimseProjectOutput, self).__init__()

        self._id = None
        self._created = None
        self._creator = None
        self._aet = None
        self._project_id = None
        self._host = None
        self._port = None
        self.discriminator = None
        self.alt_discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if creator is not None:
            self.creator = creator
        if aet is not None:
            self.aet = aet
        if project_id is not None:
            self.project_id = project_id
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port

    @property
    def id(self):
        """Gets the id of this DimseProjectOutput.

        Unique database ID

        :return: The id of this DimseProjectOutput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DimseProjectOutput.

        Unique database ID

        :param id: The id of this DimseProjectOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this DimseProjectOutput.


        :return: The created of this DimseProjectOutput.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DimseProjectOutput.


        :param created: The created of this DimseProjectOutput.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def creator(self):
        """Gets the creator of this DimseProjectOutput.

        Database ID of a user

        :return: The creator of this DimseProjectOutput.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this DimseProjectOutput.

        Database ID of a user

        :param creator: The creator of this DimseProjectOutput.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def aet(self):
        """Gets the aet of this DimseProjectOutput.

        DICOM Application Entity Title

        :return: The aet of this DimseProjectOutput.
        :rtype: str
        """
        return self._aet

    @aet.setter
    def aet(self, aet):
        """Sets the aet of this DimseProjectOutput.

        DICOM Application Entity Title

        :param aet: The aet of this DimseProjectOutput.  # noqa: E501
        :type: str
        """

        self._aet = aet

    @property
    def project_id(self):
        """Gets the project_id of this DimseProjectOutput.

        Unique database ID

        :return: The project_id of this DimseProjectOutput.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DimseProjectOutput.

        Unique database ID

        :param project_id: The project_id of this DimseProjectOutput.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def host(self):
        """Gets the host of this DimseProjectOutput.

        DICOM service hostname or IP

        :return: The host of this DimseProjectOutput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DimseProjectOutput.

        DICOM service hostname or IP

        :param host: The host of this DimseProjectOutput.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this DimseProjectOutput.

        DICOM service port number

        :return: The port of this DimseProjectOutput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DimseProjectOutput.

        DICOM service port number

        :param port: The port of this DimseProjectOutput.  # noqa: E501
        :type: int
        """

        self._port = port


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
        if not isinstance(other, DimseProjectOutput):
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
