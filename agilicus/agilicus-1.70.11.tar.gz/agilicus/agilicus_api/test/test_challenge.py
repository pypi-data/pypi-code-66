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
from agilicus_api.models.challenge import Challenge  # noqa: E501
from agilicus_api.rest import ApiException

class TestChallenge(unittest.TestCase):
    """Challenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Challenge
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.challenge.Challenge()  # noqa: E501
        if include_optional :
            return Challenge(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.challenge_spec.ChallengeSpec(
                    challenge_type = '0', 
                    challenge_types = [
                        '0'
                        ], 
                    user_id = '123', 
                    send_now = True, 
                    timeout_seconds = 1, 
                    response_uri = 'https://auth.egov.city/mfa-answer', 
                    origin = '0', 
                    challenge_endpoints = [
                        agilicus_api.models.challenge_endpoint.ChallengeEndpoint(
                            endpoint = '0', 
                            type = '0', )
                        ], ), 
                status = agilicus_api.models.challenge_status.ChallengeStatus(
                    state = 'issued', 
                    public_challenge = '0', )
            )
        else :
            return Challenge(
                spec = agilicus_api.models.challenge_spec.ChallengeSpec(
                    challenge_type = '0', 
                    challenge_types = [
                        '0'
                        ], 
                    user_id = '123', 
                    send_now = True, 
                    timeout_seconds = 1, 
                    response_uri = 'https://auth.egov.city/mfa-answer', 
                    origin = '0', 
                    challenge_endpoints = [
                        agilicus_api.models.challenge_endpoint.ChallengeEndpoint(
                            endpoint = '0', 
                            type = '0', )
                        ], ),
        )

    def testChallenge(self):
        """Test Challenge"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
