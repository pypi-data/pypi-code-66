# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.10.15
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import agilicus_api
from agilicus_api.models.organisation_admin import OrganisationAdmin  # noqa: E501
from agilicus_api.rest import ApiException

class TestOrganisationAdmin(unittest.TestCase):
    """OrganisationAdmin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrganisationAdmin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.organisation_admin.OrganisationAdmin()  # noqa: E501
        if include_optional :
            return OrganisationAdmin(
                id = '123', 
                issuer = 'app1', 
                organisation = 'some name'
            )
        else :
            return OrganisationAdmin(
                issuer = 'app1',
                organisation = 'some name',
        )

    def testOrganisationAdmin(self):
        """Test OrganisationAdmin"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
