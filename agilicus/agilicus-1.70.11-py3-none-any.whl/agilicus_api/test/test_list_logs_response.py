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
from agilicus_api.models.list_logs_response import ListLogsResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListLogsResponse(unittest.TestCase):
    """ListLogsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListLogsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_logs_response.ListLogsResponse()  # noqa: E501
        if include_optional :
            return ListLogsResponse(
                logs = [
                    agilicus_api.models.log.Log(
                        log = '::ffff:10.162.15.193 - - [22/Jul/2019:14:44:50 +0000] "GET / HTTP/1.1" 200 809 "-" "kube-probe/1.13+"', 
                        stream = 'stdout', 
                        timestamp = '2019-07-22T14:44:50.762Z', 
                        app = 'app-1', 
                        org_id = 'jjkkGmwB9oTJWDjIglTU', 
                        sub_org_id = 'kkkssmwB9oTJWDjIglTU', 
                        env = 'staging', )
                    ], 
                limit = 56
            )
        else :
            return ListLogsResponse(
                limit = 56,
        )

    def testListLogsResponse(self):
        """Test ListLogsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
