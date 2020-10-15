# coding: utf-8

# flake8: noqa

"""
    Verification API

    # Introduction  <span class=\"subtext\"> Welcome to the Passbase Verifications API docs. This documentation will help you understand our models and the Verification API with its endpoints. Based on this you can build your own system (i.e. verification) and hook it up to Passbase.  In case of feedback or questions you can reach us under this email address: [developer@passbase.com](mailto:developer@passbase.com). </span>  A User submits a video selfie and valid identifying __Resources__ during a __Verification__ guided by the Passbase client-side integration. Once all the necessary __Resources__ are submitted, __Data points__ are extracted, digitized, and authenticated. These Data points then becomes part of the User's __Identity__. The User then consents to share __Resources__ and/or __Data points__ from their Identity with you. This information is passed to you and can be used to make decisions about a User (e.g. activate account). This table below explains our terminology further.  | Term                                    | Description | |-----------------------------------------|-------------| | [Identity](#tag/identity_model)         | A set of Data points and Resources related to and owned by one single User. This data can be accessed by you through a Verification. | | Data points                             | Any data about a User extracted from a Resource (E.g. Passport Number, or Age). | | [Resource](#tag/resource_model)         | A source document used to generate the Data points for a User (E.g. Passport). | | [User](#tag/user_model)                 | The owner of an email address associated with an Identity. | | Verification                            | A transaction through which a User consents to share Data points with you. If the Data points you request are not already available in the User's Identity, the Passbase client will ask the User to submit the necessary Resource required to extract them. | | Re-authentication (login)               | A transaction through which a User can certify the ownership of Personal data previously shared through an Authentication. |   # Authentication  <span class=\"subtext\"> There are two forms of authentication for the API: <br/>&bull; API Key <br/>&bull; Bearer JWT Token  </span>   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from passbase.api.identity_api import IdentityApi
from passbase.api.project_api import ProjectApi
# import ApiClient
from passbase.api_client import ApiClient
from passbase.configuration import Configuration
# import models into sdk package
from passbase.models.cursor import Cursor
from passbase.models.data_points import DataPoints
from passbase.models.identity import Identity
from passbase.models.identity_resource import IdentityResource
from passbase.models.paginated_identities import PaginatedIdentities
from passbase.models.paginated_resources import PaginatedResources
from passbase.models.project_settings import ProjectSettings
from passbase.models.project_settings_customizations import ProjectSettingsCustomizations
from passbase.models.project_settings_verification_steps import ProjectSettingsVerificationSteps
from passbase.models.resource import Resource
from passbase.models.resource_file import ResourceFile
from passbase.models.resource_files import ResourceFiles
from passbase.models.resource_files_inner import ResourceFilesInner
from passbase.models.resource_files_input import ResourceFilesInput
from passbase.models.resource_files_input_inner import ResourceFilesInputInner
from passbase.models.resource_input import ResourceInput
from passbase.models.resource_type import ResourceType
from passbase.models.user import User
from passbase.models.watchlist_response import WatchlistResponse
