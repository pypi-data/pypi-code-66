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
from agilicus_api.models.user_summary import UserSummary  # noqa: E501
from agilicus_api.rest import ApiException

class TestUserSummary(unittest.TestCase):
    """UserSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.user_summary.UserSummary()  # noqa: E501
        if include_optional :
            return UserSummary(
                id = '123', 
                external_id = '123', 
                enabled = False, 
                status = 'active', 
                first_name = 'Alice', 
                last_name = 'Kim', 
                email = 'foo@example.com', 
                provider = 'Google', 
                roles = {"app-1":["viewer"],"app-2":["owner"]}, 
                org_id = '123', 
                type = 'user', 
                created = '2015-07-07T15:49:51.230+02:00', 
                updated = '2015-07-07T15:49:51.230+02:00', 
                auto_created = True, 
                upstream_user_identities = [
                    agilicus_api.models.upstream_user_identity.UpstreamUserIdentity(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.upstream_user_identity_spec.UpstreamUserIdentitySpec(
                            upstream_user_id = 'aa-bb-cc-11-22-33', 
                            upstream_idp_id = 'https://auth.cloud.egov.city', 
                            local_user_id = 'tuU7smH86zAXMl76sua6xQ', ), )
                    ]
            )
        else :
            return UserSummary(
        )

    def testUserSummary(self):
        """Test UserSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
