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

import agilicus_api
from agilicus_api.api.messages_api import MessagesApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.messages_api.MessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_message(self):
        """Test case for create_message

        Send a message to a specific message endpoint.  # noqa: E501
        """
        pass

    def test_create_user_message(self):
        """Test case for create_user_message

        Send a message to a user on all (optionally of a type) endpoints.  # noqa: E501
        """
        pass

    def test_delete_message_endpoint(self):
        """Test case for delete_message_endpoint

        Delete a messaging endpoint  # noqa: E501
        """
        pass

    def test_get_message_endpoint(self):
        """Test case for get_message_endpoint

        Get a message endpoint  # noqa: E501
        """
        pass

    def test_list_message_endpoints(self):
        """Test case for list_message_endpoints

        List all message endpoints (all users or a single user)  # noqa: E501
        """
        pass

    def test_list_messages_config(self):
        """Test case for list_messages_config

        Get the config of the endpoint-types (e.g. public keys etc).  # noqa: E501
        """
        pass

    def test_replace_message_endpoint(self):
        """Test case for replace_message_endpoint

        Update a messaging endpoint  # noqa: E501
        """
        pass

    def test_update_message_endpoint(self):
        """Test case for update_message_endpoint

        Register a messaging endpoint on a user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
