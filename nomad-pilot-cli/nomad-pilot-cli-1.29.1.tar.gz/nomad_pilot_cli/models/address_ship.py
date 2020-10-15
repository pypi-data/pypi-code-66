# coding: utf-8

"""
    Nomad Pilot

    This is the API descriptor for the Nomad Pilot API, responsible for shipping and logistics processing. Developed by `Samarkand Global <https://samarkand.global>`_ in partnership with `SF Express <https://www.sf- express.com/cn/sc/>`_, `eSinotrans <http://www.esinotrans.com/haitao.html>`_. Read the documentation online at `Nomad API Suite <https://api.samarkand.io/>`_ and Check out the detailed `changelog <https://gitlab.com/samarkand-nomad/nomad_readme/-/raw/master/history/nomad_pilot.md>`_. - Install for node with ``npm install nomad_pilot_cli`` - Install for python with ``pip install nomad-pilot-cli``  # noqa: E501

    The version of the OpenAPI document: 1.29.1
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nomad_pilot_cli.configuration import Configuration


class AddressShip(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'address1': 'str',
        'address2': 'str',
        'county': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'zip': 'str',
        'tin': 'str',
        'phone': 'str',
        'country_code': 'str',
        'id_card': 'str',
        'email': 'str',
        'company': 'str',
        'ecommerce_website_user_id': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'address1': 'address1',
        'address2': 'address2',
        'county': 'county',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'zip': 'zip',
        'tin': 'tin',
        'phone': 'phone',
        'country_code': 'countryCode',
        'id_card': 'idCard',
        'email': 'email',
        'company': 'company',
        'ecommerce_website_user_id': 'ecommerceWebsiteUserId'
    }

    def __init__(self, first_name=None, last_name=None, address1=None, address2=None, county=None, city=None, state=None, country=None, zip=None, tin=None, phone=None, country_code=None, id_card=None, email=None, company=None, ecommerce_website_user_id=None, local_vars_configuration=None):  # noqa: E501
        """AddressShip - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._first_name = None
        self._last_name = None
        self._address1 = None
        self._address2 = None
        self._county = None
        self._city = None
        self._state = None
        self._country = None
        self._zip = None
        self._tin = None
        self._phone = None
        self._country_code = None
        self._id_card = None
        self._email = None
        self._company = None
        self._ecommerce_website_user_id = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if county is not None:
            self.county = county
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        self.country = country
        self.zip = zip
        if tin is not None:
            self.tin = tin
        self.phone = phone
        if country_code is not None:
            self.country_code = country_code
        if id_card is not None:
            self.id_card = id_card
        if email is not None:
            self.email = email
        if company is not None:
            self.company = company
        if ecommerce_website_user_id is not None:
            self.ecommerce_website_user_id = ecommerce_website_user_id

    @property
    def first_name(self):
        """Gets the first_name of this AddressShip.  # noqa: E501


        :return: The first_name of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AddressShip.


        :param first_name: The first_name of this AddressShip.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this AddressShip.  # noqa: E501


        :return: The last_name of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AddressShip.


        :param last_name: The last_name of this AddressShip.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def address1(self):
        """Gets the address1 of this AddressShip.  # noqa: E501


        :return: The address1 of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this AddressShip.


        :param address1: The address1 of this AddressShip.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this AddressShip.  # noqa: E501


        :return: The address2 of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this AddressShip.


        :param address2: The address2 of this AddressShip.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def county(self):
        """Gets the county of this AddressShip.  # noqa: E501

        The county of current city. 县/区, e.g. 西湖区  # noqa: E501

        :return: The county of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this AddressShip.

        The county of current city. 县/区, e.g. 西湖区  # noqa: E501

        :param county: The county of this AddressShip.  # noqa: E501
        :type: str
        """

        self._county = county

    @property
    def city(self):
        """Gets the city of this AddressShip.  # noqa: E501


        :return: The city of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressShip.


        :param city: The city of this AddressShip.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this AddressShip.  # noqa: E501


        :return: The state of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AddressShip.


        :param state: The state of this AddressShip.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this AddressShip.  # noqa: E501


        :return: The country of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressShip.


        :param country: The country of this AddressShip.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def zip(self):
        """Gets the zip of this AddressShip.  # noqa: E501


        :return: The zip of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this AddressShip.


        :param zip: The zip of this AddressShip.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and zip is None:  # noqa: E501
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def tin(self):
        """Gets the tin of this AddressShip.  # noqa: E501

        TIN; The Chinese ID number of current person.  # noqa: E501

        :return: The tin of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._tin

    @tin.setter
    def tin(self, tin):
        """Sets the tin of this AddressShip.

        TIN; The Chinese ID number of current person.  # noqa: E501

        :param tin: The tin of this AddressShip.  # noqa: E501
        :type: str
        """

        self._tin = tin

    @property
    def phone(self):
        """Gets the phone of this AddressShip.  # noqa: E501


        :return: The phone of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AddressShip.


        :param phone: The phone of this AddressShip.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phone is None:  # noqa: E501
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def country_code(self):
        """Gets the country_code of this AddressShip.  # noqa: E501

        The customs code of country.  # noqa: E501

        :return: The country_code of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this AddressShip.

        The customs code of country.  # noqa: E501

        :param country_code: The country_code of this AddressShip.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def id_card(self):
        """Gets the id_card of this AddressShip.  # noqa: E501

        The Chinese ID number of current person (will be removed since we are using tin).  # noqa: E501

        :return: The id_card of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._id_card

    @id_card.setter
    def id_card(self, id_card):
        """Sets the id_card of this AddressShip.

        The Chinese ID number of current person (will be removed since we are using tin).  # noqa: E501

        :param id_card: The id_card of this AddressShip.  # noqa: E501
        :type: str
        """

        self._id_card = id_card

    @property
    def email(self):
        """Gets the email of this AddressShip.  # noqa: E501


        :return: The email of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AddressShip.


        :param email: The email of this AddressShip.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def company(self):
        """Gets the company of this AddressShip.  # noqa: E501


        :return: The company of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this AddressShip.


        :param company: The company of this AddressShip.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def ecommerce_website_user_id(self):
        """Gets the ecommerce_website_user_id of this AddressShip.  # noqa: E501

        The user ID of that e-commerce website.  # noqa: E501

        :return: The ecommerce_website_user_id of this AddressShip.  # noqa: E501
        :rtype: str
        """
        return self._ecommerce_website_user_id

    @ecommerce_website_user_id.setter
    def ecommerce_website_user_id(self, ecommerce_website_user_id):
        """Sets the ecommerce_website_user_id of this AddressShip.

        The user ID of that e-commerce website.  # noqa: E501

        :param ecommerce_website_user_id: The ecommerce_website_user_id of this AddressShip.  # noqa: E501
        :type: str
        """

        self._ecommerce_website_user_id = ecommerce_website_user_id

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
        if not isinstance(other, AddressShip):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressShip):
            return True

        return self.to_dict() != other.to_dict()
