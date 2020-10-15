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


class WebAuthNEnrollmentAnswer(object):
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
        'user_id': 'str',
        'credential_id': 'str',
        'client_data': 'str',
        'authenticator_data': 'str',
        'signature': 'str',
        'user_handle': 'str',
        'transports': 'list[str]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'credential_id': 'credential_id',
        'client_data': 'client_data',
        'authenticator_data': 'authenticator_data',
        'signature': 'signature',
        'user_handle': 'user_handle',
        'transports': 'transports'
    }

    def __init__(self, user_id=None, credential_id=None, client_data=None, authenticator_data=None, signature=None, user_handle=None, transports=None, local_vars_configuration=None):  # noqa: E501
        """WebAuthNEnrollmentAnswer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._credential_id = None
        self._client_data = None
        self._authenticator_data = None
        self._signature = None
        self._user_handle = None
        self._transports = None
        self.discriminator = None

        self.user_id = user_id
        self.credential_id = credential_id
        self.client_data = client_data
        if authenticator_data is not None:
            self.authenticator_data = authenticator_data
        if signature is not None:
            self.signature = signature
        if user_handle is not None:
            self.user_handle = user_handle
        if transports is not None:
            self.transports = transports

    @property
    def user_id(self):
        """Gets the user_id of this WebAuthNEnrollmentAnswer.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The user_id of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WebAuthNEnrollmentAnswer.

        Unique identifier  # noqa: E501

        :param user_id: The user_id of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def credential_id(self):
        """Gets the credential_id of this WebAuthNEnrollmentAnswer.  # noqa: E501

        A base64 encoding of the credential ID choosen by the authenticator  # noqa: E501

        :return: The credential_id of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """Sets the credential_id of this WebAuthNEnrollmentAnswer.

        A base64 encoding of the credential ID choosen by the authenticator  # noqa: E501

        :param credential_id: The credential_id of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and credential_id is None:  # noqa: E501
            raise ValueError("Invalid value for `credential_id`, must not be `None`")  # noqa: E501

        self._credential_id = credential_id

    @property
    def client_data(self):
        """Gets the client_data of this WebAuthNEnrollmentAnswer.  # noqa: E501

        JSON encoded collection of key-value mappings representing the contextual bindings of the relying party and client  # noqa: E501

        :return: The client_data of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._client_data

    @client_data.setter
    def client_data(self, client_data):
        """Sets the client_data of this WebAuthNEnrollmentAnswer.

        JSON encoded collection of key-value mappings representing the contextual bindings of the relying party and client  # noqa: E501

        :param client_data: The client_data of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_data is None:  # noqa: E501
            raise ValueError("Invalid value for `client_data`, must not be `None`")  # noqa: E501

        self._client_data = client_data

    @property
    def authenticator_data(self):
        """Gets the authenticator_data of this WebAuthNEnrollmentAnswer.  # noqa: E501

        Opaque string representing the authentication data, and attestion statements.  # noqa: E501

        :return: The authenticator_data of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._authenticator_data

    @authenticator_data.setter
    def authenticator_data(self, authenticator_data):
        """Sets the authenticator_data of this WebAuthNEnrollmentAnswer.

        Opaque string representing the authentication data, and attestion statements.  # noqa: E501

        :param authenticator_data: The authenticator_data of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :type: str
        """

        self._authenticator_data = authenticator_data

    @property
    def signature(self):
        """Gets the signature of this WebAuthNEnrollmentAnswer.  # noqa: E501

        The raw signature from the authenticator. This value is only included in the Authentication Assertion Response. For details see https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAssertionResponse  # noqa: E501

        :return: The signature of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this WebAuthNEnrollmentAnswer.

        The raw signature from the authenticator. This value is only included in the Authentication Assertion Response. For details see https://developer.mozilla.org/en-US/docs/Web/API/AuthenticatorAssertionResponse  # noqa: E501

        :param signature: The signature of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def user_handle(self):
        """Gets the user_handle of this WebAuthNEnrollmentAnswer.  # noqa: E501

        The user handle returned from the authenticator. This is optionally included in the Authentication Assertion Response.  # noqa: E501

        :return: The user_handle of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._user_handle

    @user_handle.setter
    def user_handle(self, user_handle):
        """Sets the user_handle of this WebAuthNEnrollmentAnswer.

        The user handle returned from the authenticator. This is optionally included in the Authentication Assertion Response.  # noqa: E501

        :param user_handle: The user_handle of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :type: str
        """

        self._user_handle = user_handle

    @property
    def transports(self):
        """Gets the transports of this WebAuthNEnrollmentAnswer.  # noqa: E501

        List of supported transports for this enrolled credential  # noqa: E501

        :return: The transports of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :rtype: list[str]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this WebAuthNEnrollmentAnswer.

        List of supported transports for this enrolled credential  # noqa: E501

        :param transports: The transports of this WebAuthNEnrollmentAnswer.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["internal", "ble", "nfc", "usb"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(transports).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `transports` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(transports) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._transports = transports

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
        if not isinstance(other, WebAuthNEnrollmentAnswer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebAuthNEnrollmentAnswer):
            return True

        return self.to_dict() != other.to_dict()
