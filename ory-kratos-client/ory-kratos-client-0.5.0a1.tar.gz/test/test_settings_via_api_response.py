# coding: utf-8

"""
    Ory Kratos

    Welcome to the ORY Kratos HTTP API documentation!  # noqa: E501

    The version of the OpenAPI document: v0.5.0-alpha.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ory_kratos_client
from ory_kratos_client.models.settings_via_api_response import SettingsViaApiResponse  # noqa: E501
from ory_kratos_client.rest import ApiException

class TestSettingsViaApiResponse(unittest.TestCase):
    """SettingsViaApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SettingsViaApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ory_kratos_client.models.settings_via_api_response.SettingsViaApiResponse()  # noqa: E501
        if include_optional :
            return SettingsViaApiResponse(
                flow = ory_kratos_client.models.flow_represents_a_settings_flow.Flow represents a Settings Flow(
                    active = '0', 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '0', 
                    identity = ory_kratos_client.models.identity.Identity(
                        id = '0', 
                        recovery_addresses = [
                            ory_kratos_client.models.recovery_address.RecoveryAddress(
                                id = '0', 
                                value = '0', 
                                via = '0', )
                            ], 
                        schema_id = '0', 
                        schema_url = '0', 
                        traits = ory_kratos_client.models.traits.traits(), 
                        verifiable_addresses = [
                            ory_kratos_client.models.verifiable_address.VerifiableAddress(
                                id = '0', 
                                status = '0', 
                                value = '0', 
                                verified = True, 
                                verified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                via = '0', )
                            ], ), 
                    issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    messages = [
                        ory_kratos_client.models.message.Message(
                            context = ory_kratos_client.models.context.context(), 
                            id = 56, 
                            text = '0', 
                            type = '0', )
                        ], 
                    methods = {
                        'key' : ory_kratos_client.models.settings_flow_method.settingsFlowMethod(
                            config = ory_kratos_client.models.settings_flow_method_config.settingsFlowMethodConfig(
                                action = '0', 
                                fields = [
                                    ory_kratos_client.models.form_field.formField(
                                        disabled = True, 
                                        name = '0', 
                                        pattern = '0', 
                                        required = True, 
                                        type = '0', 
                                        value = ory_kratos_client.models.value.value(), )
                                    ], 
                                method = '0', ), 
                            method = '0', )
                        }, 
                    request_url = '0', 
                    state = '0', 
                    type = '0', ), 
                identity = ory_kratos_client.models.identity.Identity(
                    id = '0', 
                    recovery_addresses = [
                        ory_kratos_client.models.recovery_address.RecoveryAddress(
                            id = '0', 
                            value = '0', 
                            via = '0', )
                        ], 
                    schema_id = '0', 
                    schema_url = '0', 
                    traits = ory_kratos_client.models.traits.traits(), 
                    verifiable_addresses = [
                        ory_kratos_client.models.verifiable_address.VerifiableAddress(
                            id = '0', 
                            status = '0', 
                            value = '0', 
                            verified = True, 
                            verified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            via = '0', )
                        ], )
            )
        else :
            return SettingsViaApiResponse(
                flow = ory_kratos_client.models.flow_represents_a_settings_flow.Flow represents a Settings Flow(
                    active = '0', 
                    expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '0', 
                    identity = ory_kratos_client.models.identity.Identity(
                        id = '0', 
                        recovery_addresses = [
                            ory_kratos_client.models.recovery_address.RecoveryAddress(
                                id = '0', 
                                value = '0', 
                                via = '0', )
                            ], 
                        schema_id = '0', 
                        schema_url = '0', 
                        traits = ory_kratos_client.models.traits.traits(), 
                        verifiable_addresses = [
                            ory_kratos_client.models.verifiable_address.VerifiableAddress(
                                id = '0', 
                                status = '0', 
                                value = '0', 
                                verified = True, 
                                verified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                via = '0', )
                            ], ), 
                    issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    messages = [
                        ory_kratos_client.models.message.Message(
                            context = ory_kratos_client.models.context.context(), 
                            id = 56, 
                            text = '0', 
                            type = '0', )
                        ], 
                    methods = {
                        'key' : ory_kratos_client.models.settings_flow_method.settingsFlowMethod(
                            config = ory_kratos_client.models.settings_flow_method_config.settingsFlowMethodConfig(
                                action = '0', 
                                fields = [
                                    ory_kratos_client.models.form_field.formField(
                                        disabled = True, 
                                        name = '0', 
                                        pattern = '0', 
                                        required = True, 
                                        type = '0', 
                                        value = ory_kratos_client.models.value.value(), )
                                    ], 
                                method = '0', ), 
                            method = '0', )
                        }, 
                    request_url = '0', 
                    state = '0', 
                    type = '0', ),
                identity = ory_kratos_client.models.identity.Identity(
                    id = '0', 
                    recovery_addresses = [
                        ory_kratos_client.models.recovery_address.RecoveryAddress(
                            id = '0', 
                            value = '0', 
                            via = '0', )
                        ], 
                    schema_id = '0', 
                    schema_url = '0', 
                    traits = ory_kratos_client.models.traits.traits(), 
                    verifiable_addresses = [
                        ory_kratos_client.models.verifiable_address.VerifiableAddress(
                            id = '0', 
                            status = '0', 
                            value = '0', 
                            verified = True, 
                            verified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            via = '0', )
                        ], ),
        )

    def testSettingsViaApiResponse(self):
        """Test SettingsViaApiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
