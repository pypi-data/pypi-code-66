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
from agilicus_api.models.user_metadata_spec import UserMetadataSpec  # noqa: E501
from agilicus_api.rest import ApiException

class TestUserMetadataSpec(unittest.TestCase):
    """UserMetadataSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserMetadataSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.user_metadata_spec.UserMetadataSpec()  # noqa: E501
        if include_optional :
            return UserMetadataSpec(
                user_id = 'tuU7smH86zAXMl76sua6xQ', 
                org_id = 'IAsl3dl40aSsfLKiU76', 
                app_id = 'IAsl3dl40aSsfLKiU76', 
                name = '0', 
                data_type = 'mfa_enrollment_expiry', 
                data = '2020-08-26T16:59:28+00:00'
            )
        else :
            return UserMetadataSpec(
                user_id = 'tuU7smH86zAXMl76sua6xQ',
        )

    def testUserMetadataSpec(self):
        """Test UserMetadataSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
