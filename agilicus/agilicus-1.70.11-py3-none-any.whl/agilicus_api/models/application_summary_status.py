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


class ApplicationSummaryStatus(object):
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
        'application_id': 'str',
        'application_name': 'str',
        'assigned_org_id': 'str',
        'published': 'str',
        'description': 'str',
        'category': 'str',
        'icon_url': 'str',
        'default_role_name': 'str',
        'default_role_id': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'application_name': 'application_name',
        'assigned_org_id': 'assigned_org_id',
        'published': 'published',
        'description': 'description',
        'category': 'category',
        'icon_url': 'icon_url',
        'default_role_name': 'default_role_name',
        'default_role_id': 'default_role_id'
    }

    def __init__(self, application_id=None, application_name=None, assigned_org_id=None, published=None, description=None, category=None, icon_url='https://storage.googleapis.com/agilicus/logo.svg', default_role_name=None, default_role_id=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationSummaryStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_id = None
        self._application_name = None
        self._assigned_org_id = None
        self._published = None
        self._description = None
        self._category = None
        self._icon_url = None
        self._default_role_name = None
        self._default_role_id = None
        self.discriminator = None

        self.application_id = application_id
        self.application_name = application_name
        self.assigned_org_id = assigned_org_id
        self.published = published
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        self.icon_url = icon_url
        self.default_role_name = default_role_name
        self.default_role_id = default_role_id

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationSummaryStatus.  # noqa: E501

        The ID of the application to which this organiastion is assigned.  # noqa: E501

        :return: The application_id of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationSummaryStatus.

        The ID of the application to which this organiastion is assigned.  # noqa: E501

        :param application_id: The application_id of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_id is not None and len(application_id) > 40):
            raise ValueError("Invalid value for `application_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_id is not None and len(application_id) < 1):
            raise ValueError("Invalid value for `application_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this ApplicationSummaryStatus.  # noqa: E501

        The name of the application  # noqa: E501

        :return: The application_name of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ApplicationSummaryStatus.

        The name of the application  # noqa: E501

        :param application_name: The application_name of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_name is None:  # noqa: E501
            raise ValueError("Invalid value for `application_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_name is not None and len(application_name) > 40):
            raise ValueError("Invalid value for `application_name`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_name is not None and len(application_name) < 1):
            raise ValueError("Invalid value for `application_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._application_name = application_name

    @property
    def assigned_org_id(self):
        """Gets the assigned_org_id of this ApplicationSummaryStatus.  # noqa: E501

        The id of the organisation assigned to the application  # noqa: E501

        :return: The assigned_org_id of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._assigned_org_id

    @assigned_org_id.setter
    def assigned_org_id(self, assigned_org_id):
        """Sets the assigned_org_id of this ApplicationSummaryStatus.

        The id of the organisation assigned to the application  # noqa: E501

        :param assigned_org_id: The assigned_org_id of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and assigned_org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `assigned_org_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                assigned_org_id is not None and len(assigned_org_id) > 40):
            raise ValueError("Invalid value for `assigned_org_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                assigned_org_id is not None and len(assigned_org_id) < 1):
            raise ValueError("Invalid value for `assigned_org_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._assigned_org_id = assigned_org_id

    @property
    def published(self):
        """Gets the published of this ApplicationSummaryStatus.  # noqa: E501

        Whether or not this Application is published, and if so, how. An application that has been published somewhere will have high level details about it visible, such as its name and description. The enum values mean the following:   - no: This application is not published. It will only be visibile to users with       permission to access the application, or to administrators.   - public: This application is published to the public catalogue. Any user who       can request access to the organisation will see high level details about this       application.   # noqa: E501

        :return: The published of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this ApplicationSummaryStatus.

        Whether or not this Application is published, and if so, how. An application that has been published somewhere will have high level details about it visible, such as its name and description. The enum values mean the following:   - no: This application is not published. It will only be visibile to users with       permission to access the application, or to administrators.   - public: This application is published to the public catalogue. Any user who       can request access to the organisation will see high level details about this       application.   # noqa: E501

        :param published: The published of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and published is None:  # noqa: E501
            raise ValueError("Invalid value for `published`, must not be `None`")  # noqa: E501
        allowed_values = ["no", "public"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and published not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `published` ({0}), must be one of {1}"  # noqa: E501
                .format(published, allowed_values)
            )

        self._published = published

    @property
    def description(self):
        """Gets the description of this ApplicationSummaryStatus.  # noqa: E501

        A brief description of the application.  # noqa: E501

        :return: The description of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationSummaryStatus.

        A brief description of the application.  # noqa: E501

        :param description: The description of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 100):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def category(self):
        """Gets the category of this ApplicationSummaryStatus.  # noqa: E501

        A category used to group similar applications together.  # noqa: E501

        :return: The category of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ApplicationSummaryStatus.

        A category used to group similar applications together.  # noqa: E501

        :param category: The category of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) > 100):
            raise ValueError("Invalid value for `category`, length must be less than or equal to `100`")  # noqa: E501

        self._category = category

    @property
    def icon_url(self):
        """Gets the icon_url of this ApplicationSummaryStatus.  # noqa: E501

        A url pointing to an icon representing this application.   # noqa: E501

        :return: The icon_url of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this ApplicationSummaryStatus.

        A url pointing to an icon representing this application.   # noqa: E501

        :param icon_url: The icon_url of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and icon_url is None:  # noqa: E501
            raise ValueError("Invalid value for `icon_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                icon_url is not None and len(icon_url) > 1024):
            raise ValueError("Invalid value for `icon_url`, length must be less than or equal to `1024`")  # noqa: E501

        self._icon_url = icon_url

    @property
    def default_role_name(self):
        """Gets the default_role_name of this ApplicationSummaryStatus.  # noqa: E501

        The name of the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access.   # noqa: E501

        :return: The default_role_name of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._default_role_name

    @default_role_name.setter
    def default_role_name(self, default_role_name):
        """Sets the default_role_name of this ApplicationSummaryStatus.

        The name of the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access.   # noqa: E501

        :param default_role_name: The default_role_name of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                default_role_name is not None and len(default_role_name) > 100):
            raise ValueError("Invalid value for `default_role_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                default_role_name is not None and len(default_role_name) < 1):
            raise ValueError("Invalid value for `default_role_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._default_role_name = default_role_name

    @property
    def default_role_id(self):
        """Gets the default_role_id of this ApplicationSummaryStatus.  # noqa: E501

        The unique id the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access.   # noqa: E501

        :return: The default_role_id of this ApplicationSummaryStatus.  # noqa: E501
        :rtype: str
        """
        return self._default_role_id

    @default_role_id.setter
    def default_role_id(self, default_role_id):
        """Sets the default_role_id of this ApplicationSummaryStatus.

        The unique id the default role of the application. This will be granted to users by default when an admin grants access to this application in response to a request for access.   # noqa: E501

        :param default_role_id: The default_role_id of this ApplicationSummaryStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                default_role_id is not None and len(default_role_id) > 40):
            raise ValueError("Invalid value for `default_role_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                default_role_id is not None and len(default_role_id) < 1):
            raise ValueError("Invalid value for `default_role_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._default_role_id = default_role_id

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
        if not isinstance(other, ApplicationSummaryStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationSummaryStatus):
            return True

        return self.to_dict() != other.to_dict()
