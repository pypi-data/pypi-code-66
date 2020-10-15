# coding: utf-8

"""
    Nomad Pilot

    This is the API descriptor for the Nomad Pilot API, responsible for shipping and logistics processing. Developed by `Samarkand Global <https://samarkand.global>`_ in partnership with `SF Express <https://www.sf- express.com/cn/sc/>`_, `eSinotrans <http://www.esinotrans.com/haitao.html>`_. Read the documentation online at `Nomad API Suite <https://api.samarkand.io/>`_ and Check out the detailed `changelog <https://gitlab.com/samarkand-nomad/nomad_readme/-/raw/master/history/nomad_pilot.md>`_. - Install for node with ``npm install nomad_pilot_cli`` - Install for python with ``pip install nomad-pilot-cli``  # noqa: E501

    The version of the OpenAPI document: 1.29.1
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import nomad_pilot_cli
from nomad_pilot_cli.api.freight_forward_api import FreightForwardApi  # noqa: E501
from nomad_pilot_cli.rest import ApiException


class TestFreightForwardApi(unittest.TestCase):
    """FreightForwardApi unit test stubs"""

    def setUp(self):
        self.api = nomad_pilot_cli.api.freight_forward_api.FreightForwardApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_freight_forward(self):
        """Test case for query_freight_forward

        queryFreightForward  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
