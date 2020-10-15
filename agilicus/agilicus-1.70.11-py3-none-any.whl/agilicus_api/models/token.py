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


class Token(object):
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
        'sub': 'str',
        'sub_email': 'str',
        'org': 'str',
        'root_org': 'str',
        'roles': 'Roles',
        'jti': 'str',
        'iat': 'str',
        'exp': 'str',
        'hosts': 'list[HostPermissions]',
        'aud': 'list[str]',
        'session': 'str',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'sub': 'sub',
        'sub_email': 'sub_email',
        'org': 'org',
        'root_org': 'root_org',
        'roles': 'roles',
        'jti': 'jti',
        'iat': 'iat',
        'exp': 'exp',
        'hosts': 'hosts',
        'aud': 'aud',
        'session': 'session',
        'scopes': 'scopes'
    }

    def __init__(self, sub=None, sub_email=None, org=None, root_org=None, roles=None, jti=None, iat=None, exp=None, hosts=None, aud=None, session=None, scopes=None, local_vars_configuration=None):  # noqa: E501
        """Token - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sub = None
        self._sub_email = None
        self._org = None
        self._root_org = None
        self._roles = None
        self._jti = None
        self._iat = None
        self._exp = None
        self._hosts = None
        self._aud = None
        self._session = None
        self._scopes = None
        self.discriminator = None

        if sub is not None:
            self.sub = sub
        if sub_email is not None:
            self.sub_email = sub_email
        if org is not None:
            self.org = org
        if root_org is not None:
            self.root_org = root_org
        if roles is not None:
            self.roles = roles
        if jti is not None:
            self.jti = jti
        if iat is not None:
            self.iat = iat
        if exp is not None:
            self.exp = exp
        if hosts is not None:
            self.hosts = hosts
        if aud is not None:
            self.aud = aud
        if session is not None:
            self.session = session
        if scopes is not None:
            self.scopes = scopes

    @property
    def sub(self):
        """Gets the sub of this Token.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The sub of this Token.  # noqa: E501
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        """Sets the sub of this Token.

        Unique identifier  # noqa: E501

        :param sub: The sub of this Token.  # noqa: E501
        :type: str
        """

        self._sub = sub

    @property
    def sub_email(self):
        """Gets the sub_email of this Token.  # noqa: E501

        User's email address  # noqa: E501

        :return: The sub_email of this Token.  # noqa: E501
        :rtype: str
        """
        return self._sub_email

    @sub_email.setter
    def sub_email(self, sub_email):
        """Sets the sub_email of this Token.

        User's email address  # noqa: E501

        :param sub_email: The sub_email of this Token.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sub_email is not None and len(sub_email) > 100):
            raise ValueError("Invalid value for `sub_email`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sub_email is not None and len(sub_email) < 0):
            raise ValueError("Invalid value for `sub_email`, length must be greater than or equal to `0`")  # noqa: E501

        self._sub_email = sub_email

    @property
    def org(self):
        """Gets the org of this Token.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The org of this Token.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this Token.

        Unique identifier  # noqa: E501

        :param org: The org of this Token.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def root_org(self):
        """Gets the root_org of this Token.  # noqa: E501

        The organisation at the root of the hierachy for which this token provides permissions.   # noqa: E501

        :return: The root_org of this Token.  # noqa: E501
        :rtype: str
        """
        return self._root_org

    @root_org.setter
    def root_org(self, root_org):
        """Sets the root_org of this Token.

        The organisation at the root of the hierachy for which this token provides permissions.   # noqa: E501

        :param root_org: The root_org of this Token.  # noqa: E501
        :type: str
        """

        self._root_org = root_org

    @property
    def roles(self):
        """Gets the roles of this Token.  # noqa: E501


        :return: The roles of this Token.  # noqa: E501
        :rtype: Roles
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Token.


        :param roles: The roles of this Token.  # noqa: E501
        :type: Roles
        """

        self._roles = roles

    @property
    def jti(self):
        """Gets the jti of this Token.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The jti of this Token.  # noqa: E501
        :rtype: str
        """
        return self._jti

    @jti.setter
    def jti(self, jti):
        """Sets the jti of this Token.

        Unique identifier  # noqa: E501

        :param jti: The jti of this Token.  # noqa: E501
        :type: str
        """

        self._jti = jti

    @property
    def iat(self):
        """Gets the iat of this Token.  # noqa: E501

        token issue date  # noqa: E501

        :return: The iat of this Token.  # noqa: E501
        :rtype: str
        """
        return self._iat

    @iat.setter
    def iat(self, iat):
        """Sets the iat of this Token.

        token issue date  # noqa: E501

        :param iat: The iat of this Token.  # noqa: E501
        :type: str
        """

        self._iat = iat

    @property
    def exp(self):
        """Gets the exp of this Token.  # noqa: E501

        token expiry date  # noqa: E501

        :return: The exp of this Token.  # noqa: E501
        :rtype: str
        """
        return self._exp

    @exp.setter
    def exp(self, exp):
        """Sets the exp of this Token.

        token expiry date  # noqa: E501

        :param exp: The exp of this Token.  # noqa: E501
        :type: str
        """

        self._exp = exp

    @property
    def hosts(self):
        """Gets the hosts of this Token.  # noqa: E501

        array of valid hosts  # noqa: E501

        :return: The hosts of this Token.  # noqa: E501
        :rtype: list[HostPermissions]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this Token.

        array of valid hosts  # noqa: E501

        :param hosts: The hosts of this Token.  # noqa: E501
        :type: list[HostPermissions]
        """

        self._hosts = hosts

    @property
    def aud(self):
        """Gets the aud of this Token.  # noqa: E501

        token audience  # noqa: E501

        :return: The aud of this Token.  # noqa: E501
        :rtype: list[str]
        """
        return self._aud

    @aud.setter
    def aud(self, aud):
        """Sets the aud of this Token.

        token audience  # noqa: E501

        :param aud: The aud of this Token.  # noqa: E501
        :type: list[str]
        """

        self._aud = aud

    @property
    def session(self):
        """Gets the session of this Token.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The session of this Token.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this Token.

        Unique identifier  # noqa: E501

        :param session: The session of this Token.  # noqa: E501
        :type: str
        """

        self._session = session

    @property
    def scopes(self):
        """Gets the scopes of this Token.  # noqa: E501

        The list of scopes associated with this access token. Note that these scopes do not indicate whether that permission has been granted. Whether or not the permission has been granted to this token depends on the scope being associated with the token AND whether the user has that permission to begin with.   # noqa: E501

        :return: The scopes of this Token.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this Token.

        The list of scopes associated with this access token. Note that these scopes do not indicate whether that permission has been granted. Whether or not the permission has been granted to this token depends on the scope being associated with the token AND whether the user has that permission to begin with.   # noqa: E501

        :param scopes: The scopes of this Token.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

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
        if not isinstance(other, Token):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Token):
            return True

        return self.to_dict() != other.to_dict()
