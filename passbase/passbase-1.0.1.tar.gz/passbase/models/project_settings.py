# coding: utf-8

"""
    Verification API

    # Introduction  <span class=\"subtext\"> Welcome to the Passbase Verifications API docs. This documentation will help you understand our models and the Verification API with its endpoints. Based on this you can build your own system (i.e. verification) and hook it up to Passbase.  In case of feedback or questions you can reach us under this email address: [developer@passbase.com](mailto:developer@passbase.com). </span>  A User submits a video selfie and valid identifying __Resources__ during a __Verification__ guided by the Passbase client-side integration. Once all the necessary __Resources__ are submitted, __Data points__ are extracted, digitized, and authenticated. These Data points then becomes part of the User's __Identity__. The User then consents to share __Resources__ and/or __Data points__ from their Identity with you. This information is passed to you and can be used to make decisions about a User (e.g. activate account). This table below explains our terminology further.  | Term                                    | Description | |-----------------------------------------|-------------| | [Identity](#tag/identity_model)         | A set of Data points and Resources related to and owned by one single User. This data can be accessed by you through a Verification. | | Data points                             | Any data about a User extracted from a Resource (E.g. Passport Number, or Age). | | [Resource](#tag/resource_model)         | A source document used to generate the Data points for a User (E.g. Passport). | | [User](#tag/user_model)                 | The owner of an email address associated with an Identity. | | Verification                            | A transaction through which a User consents to share Data points with you. If the Data points you request are not already available in the User's Identity, the Passbase client will ask the User to submit the necessary Resource required to extract them. | | Re-authentication (login)               | A transaction through which a User can certify the ownership of Personal data previously shared through an Authentication. |   # Authentication  <span class=\"subtext\"> There are two forms of authentication for the API: <br/>&bull; API Key <br/>&bull; Bearer JWT Token  </span>   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectSettings(object):
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
        'id': 'str',
        'slug': 'str',
        'environment': 'str',
        'organization': 'str',
        'customizations': 'ProjectSettingsCustomizations',
        'verification_steps': 'list[ProjectSettingsVerificationSteps]'
    }

    attribute_map = {
        'id': 'id',
        'slug': 'slug',
        'environment': 'environment',
        'organization': 'organization',
        'customizations': 'customizations',
        'verification_steps': 'verification_steps'
    }

    def __init__(self, id=None, slug=None, environment=None, organization=None, customizations=None, verification_steps=None):  # noqa: E501
        """ProjectSettings - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._slug = None
        self._environment = None
        self._organization = None
        self._customizations = None
        self._verification_steps = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
        if environment is not None:
            self.environment = environment
        if organization is not None:
            self.organization = organization
        if customizations is not None:
            self.customizations = customizations
        if verification_steps is not None:
            self.verification_steps = verification_steps

    @property
    def id(self):
        """Gets the id of this ProjectSettings.  # noqa: E501

        Unique ID of the project  # noqa: E501

        :return: The id of this ProjectSettings.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectSettings.

        Unique ID of the project  # noqa: E501

        :param id: The id of this ProjectSettings.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def slug(self):
        """Gets the slug of this ProjectSettings.  # noqa: E501

        slugs are meant to be a way to verify people just with the link  # noqa: E501

        :return: The slug of this ProjectSettings.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this ProjectSettings.

        slugs are meant to be a way to verify people just with the link  # noqa: E501

        :param slug: The slug of this ProjectSettings.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def environment(self):
        """Gets the environment of this ProjectSettings.  # noqa: E501


        :return: The environment of this ProjectSettings.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this ProjectSettings.


        :param environment: The environment of this ProjectSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["sandbox", "production"]  # noqa: E501
        if environment not in allowed_values:
            raise ValueError(
                "Invalid value for `environment` ({0}), must be one of {1}"  # noqa: E501
                .format(environment, allowed_values)
            )

        self._environment = environment

    @property
    def organization(self):
        """Gets the organization of this ProjectSettings.  # noqa: E501

        Name of the organization that owns this project  # noqa: E501

        :return: The organization of this ProjectSettings.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ProjectSettings.

        Name of the organization that owns this project  # noqa: E501

        :param organization: The organization of this ProjectSettings.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def customizations(self):
        """Gets the customizations of this ProjectSettings.  # noqa: E501


        :return: The customizations of this ProjectSettings.  # noqa: E501
        :rtype: ProjectSettingsCustomizations
        """
        return self._customizations

    @customizations.setter
    def customizations(self, customizations):
        """Sets the customizations of this ProjectSettings.


        :param customizations: The customizations of this ProjectSettings.  # noqa: E501
        :type: ProjectSettingsCustomizations
        """

        self._customizations = customizations

    @property
    def verification_steps(self):
        """Gets the verification_steps of this ProjectSettings.  # noqa: E501

        List of the steps through which the user must go through to complete their verification   # noqa: E501

        :return: The verification_steps of this ProjectSettings.  # noqa: E501
        :rtype: list[ProjectSettingsVerificationSteps]
        """
        return self._verification_steps

    @verification_steps.setter
    def verification_steps(self, verification_steps):
        """Sets the verification_steps of this ProjectSettings.

        List of the steps through which the user must go through to complete their verification   # noqa: E501

        :param verification_steps: The verification_steps of this ProjectSettings.  # noqa: E501
        :type: list[ProjectSettingsVerificationSteps]
        """

        self._verification_steps = verification_steps

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
        if issubclass(ProjectSettings, dict):
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
        if not isinstance(other, ProjectSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
