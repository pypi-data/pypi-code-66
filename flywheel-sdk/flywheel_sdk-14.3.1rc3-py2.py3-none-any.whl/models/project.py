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

from flywheel.models.analysis_output import AnalysisOutput  # noqa: F401,E501
from flywheel.models.common_editions import CommonEditions  # noqa: F401,E501
from flywheel.models.common_info import CommonInfo  # noqa: F401,E501
from flywheel.models.container_parents import ContainerParents  # noqa: F401,E501
from flywheel.models.file_entry import FileEntry  # noqa: F401,E501
from flywheel.models.ldap_sync import LdapSync  # noqa: F401,E501
from flywheel.models.note import Note  # noqa: F401,E501
from flywheel.models.provider_links import ProviderLinks  # noqa: F401,E501
from flywheel.models.roles_backwards_compatible_role_assignment import RolesBackwardsCompatibleRoleAssignment  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

from .mixins import ProjectMixin

class Project(ProjectMixin):

    swagger_types = {
        'label': 'str',
        'info': 'CommonInfo',
        'description': 'str',
        'group': 'str',
        'providers': 'ProviderLinks',
        'editions': 'CommonEditions',
        'ldap_sync': 'LdapSync',
        'id': 'str',
        'parents': 'ContainerParents',
        'info_exists': 'bool',
        'created': 'datetime',
        'modified': 'datetime',
        'revision': 'int',
        'templates': 'object',
        'permissions': 'list[RolesBackwardsCompatibleRoleAssignment]',
        'files': 'list[FileEntry]',
        'notes': 'list[Note]',
        'tags': 'list[str]',
        'analyses': 'list[AnalysisOutput]'
    }

    attribute_map = {
        'label': 'label',
        'info': 'info',
        'description': 'description',
        'group': 'group',
        'providers': 'providers',
        'editions': 'editions',
        'ldap_sync': 'ldap_sync',
        'id': '_id',
        'parents': 'parents',
        'info_exists': 'info_exists',
        'created': 'created',
        'modified': 'modified',
        'revision': 'revision',
        'templates': 'templates',
        'permissions': 'permissions',
        'files': 'files',
        'notes': 'notes',
        'tags': 'tags',
        'analyses': 'analyses'
    }

    rattribute_map = {
        'label': 'label',
        'info': 'info',
        'description': 'description',
        'group': 'group',
        'providers': 'providers',
        'editions': 'editions',
        'ldap_sync': 'ldap_sync',
        '_id': 'id',
        'parents': 'parents',
        'info_exists': 'info_exists',
        'created': 'created',
        'modified': 'modified',
        'revision': 'revision',
        'templates': 'templates',
        'permissions': 'permissions',
        'files': 'files',
        'notes': 'notes',
        'tags': 'tags',
        'analyses': 'analyses'
    }

    def __init__(self, label=None, info=None, description=None, group=None, providers=None, editions=None, ldap_sync=None, id=None, parents=None, info_exists=None, created=None, modified=None, revision=None, templates=None, permissions=None, files=None, notes=None, tags=None, analyses=None):  # noqa: E501
        """Project - a model defined in Swagger"""
        super(Project, self).__init__()

        self._label = None
        self._info = None
        self._description = None
        self._group = None
        self._providers = None
        self._editions = None
        self._ldap_sync = None
        self._id = None
        self._parents = None
        self._info_exists = None
        self._created = None
        self._modified = None
        self._revision = None
        self._templates = None
        self._permissions = None
        self._files = None
        self._notes = None
        self._tags = None
        self._analyses = None
        self.discriminator = None
        self.alt_discriminator = None

        if label is not None:
            self.label = label
        if info is not None:
            self.info = info
        if description is not None:
            self.description = description
        if group is not None:
            self.group = group
        if providers is not None:
            self.providers = providers
        if editions is not None:
            self.editions = editions
        if ldap_sync is not None:
            self.ldap_sync = ldap_sync
        if id is not None:
            self.id = id
        if parents is not None:
            self.parents = parents
        if info_exists is not None:
            self.info_exists = info_exists
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if revision is not None:
            self.revision = revision
        if templates is not None:
            self.templates = templates
        if permissions is not None:
            self.permissions = permissions
        if files is not None:
            self.files = files
        if notes is not None:
            self.notes = notes
        if tags is not None:
            self.tags = tags
        if analyses is not None:
            self.analyses = analyses

    @property
    def label(self):
        """Gets the label of this Project.

        Application-specific label

        :return: The label of this Project.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Project.

        Application-specific label

        :param label: The label of this Project.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def info(self):
        """Gets the info of this Project.


        :return: The info of this Project.
        :rtype: CommonInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Project.


        :param info: The info of this Project.  # noqa: E501
        :type: CommonInfo
        """

        self._info = info

    @property
    def description(self):
        """Gets the description of this Project.


        :return: The description of this Project.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.


        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group(self):
        """Gets the group of this Project.


        :return: The group of this Project.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Project.


        :param group: The group of this Project.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def providers(self):
        """Gets the providers of this Project.


        :return: The providers of this Project.
        :rtype: ProviderLinks
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this Project.


        :param providers: The providers of this Project.  # noqa: E501
        :type: ProviderLinks
        """

        self._providers = providers

    @property
    def editions(self):
        """Gets the editions of this Project.


        :return: The editions of this Project.
        :rtype: CommonEditions
        """
        return self._editions

    @editions.setter
    def editions(self, editions):
        """Sets the editions of this Project.


        :param editions: The editions of this Project.  # noqa: E501
        :type: CommonEditions
        """

        self._editions = editions

    @property
    def ldap_sync(self):
        """Gets the ldap_sync of this Project.


        :return: The ldap_sync of this Project.
        :rtype: LdapSync
        """
        return self._ldap_sync

    @ldap_sync.setter
    def ldap_sync(self, ldap_sync):
        """Sets the ldap_sync of this Project.


        :param ldap_sync: The ldap_sync of this Project.  # noqa: E501
        :type: LdapSync
        """

        self._ldap_sync = ldap_sync

    @property
    def id(self):
        """Gets the id of this Project.

        Unique database ID

        :return: The id of this Project.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        Unique database ID

        :param id: The id of this Project.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parents(self):
        """Gets the parents of this Project.


        :return: The parents of this Project.
        :rtype: ContainerParents
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this Project.


        :param parents: The parents of this Project.  # noqa: E501
        :type: ContainerParents
        """

        self._parents = parents

    @property
    def info_exists(self):
        """Gets the info_exists of this Project.

        Flag that indicates whether or not info exists on this container

        :return: The info_exists of this Project.
        :rtype: bool
        """
        return self._info_exists

    @info_exists.setter
    def info_exists(self, info_exists):
        """Sets the info_exists of this Project.

        Flag that indicates whether or not info exists on this container

        :param info_exists: The info_exists of this Project.  # noqa: E501
        :type: bool
        """

        self._info_exists = info_exists

    @property
    def created(self):
        """Gets the created of this Project.

        Creation time (automatically set)

        :return: The created of this Project.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Project.

        Creation time (automatically set)

        :param created: The created of this Project.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Project.

        Last modification time (automatically updated)

        :return: The modified of this Project.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Project.

        Last modification time (automatically updated)

        :param modified: The modified of this Project.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def revision(self):
        """Gets the revision of this Project.

        An incremental document revision number

        :return: The revision of this Project.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Project.

        An incremental document revision number

        :param revision: The revision of this Project.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def templates(self):
        """Gets the templates of this Project.


        :return: The templates of this Project.
        :rtype: object
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this Project.


        :param templates: The templates of this Project.  # noqa: E501
        :type: object
        """

        self._templates = templates

    @property
    def permissions(self):
        """Gets the permissions of this Project.


        :return: The permissions of this Project.
        :rtype: list[RolesBackwardsCompatibleRoleAssignment]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Project.


        :param permissions: The permissions of this Project.  # noqa: E501
        :type: list[RolesBackwardsCompatibleRoleAssignment]
        """

        self._permissions = permissions

    @property
    def files(self):
        """Gets the files of this Project.


        :return: The files of this Project.
        :rtype: list[FileEntry]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Project.


        :param files: The files of this Project.  # noqa: E501
        :type: list[FileEntry]
        """

        self._files = files

    @property
    def notes(self):
        """Gets the notes of this Project.


        :return: The notes of this Project.
        :rtype: list[Note]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Project.


        :param notes: The notes of this Project.  # noqa: E501
        :type: list[Note]
        """

        self._notes = notes

    @property
    def tags(self):
        """Gets the tags of this Project.

        Array of application-specific tags

        :return: The tags of this Project.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Project.

        Array of application-specific tags

        :param tags: The tags of this Project.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def analyses(self):
        """Gets the analyses of this Project.


        :return: The analyses of this Project.
        :rtype: list[AnalysisOutput]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        """Sets the analyses of this Project.


        :param analyses: The analyses of this Project.  # noqa: E501
        :type: list[AnalysisOutput]
        """

        self._analyses = analyses


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
        if not isinstance(other, Project):
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
