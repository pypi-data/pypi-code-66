# container-service-extension
# Copyright (c) 2019 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

from pyvcloud.vcd import utils
import pyvcloud.vcd.exceptions as vcd_exceptions

from container_service_extension.client.response_processor import \
    process_response
from container_service_extension.pyvcloud_utils import get_vdc
import container_service_extension.shared_constants as shared_constants


class LegacyOvdc:
    def __init__(self, client):
        self.client = client
        self._uri = f"{self.client.get_api_uri()}/{shared_constants.CSE_URL_FRAGMENT}"  # noqa: E501

    def list_ovdc(self, list_pks_plans=False):
        method = shared_constants.RequestMethod.GET
        uri = f'{self._uri}/ovdcs'
        response = self.client._do_request_prim(
            method,
            uri,
            self.client._session,
            accept_type='application/json',
            params={
                shared_constants.RequestKey.LIST_PKS_PLANS: list_pks_plans})
        return process_response(response)

    # TODO(metadata based enablement for < v35): Revisit after decision
    # to support metadata way of enabling for native clusters
    def update_ovdc(self, ovdc_name, k8s_provider, **kwargs):
        """Enable/Disable ovdc for native workflow."""
        msg = "Operation not supported; Under implementation"
        raise vcd_exceptions.OperationNotSupportedException(msg)

    def info_ovdc(self, ovdc_name, org_name):
        """Disable ovdc for k8s for the given container provider.

        :param str ovdc_name: Name of the org VDC to be enabled
        :param str org_name: Name of org that @ovdc_name belongs to

        :rtype: dict
        """
        method = shared_constants.RequestMethod.GET
        ovdc = get_vdc(self.client, vdc_name=ovdc_name, org_name=org_name,
                       is_admin_operation=True)
        ovdc_id = utils.extract_id(ovdc.get_resource().get('id'))
        uri = f'{self._uri}/ovdc/{ovdc_id}'

        response = self.client._do_request_prim(
            method,
            uri,
            self.client._session,
            accept_type='application/json')
        return process_response(response)

    def update_ovdc_compute_policies(self, ovdc_name, org_name,
                                     compute_policy_name, action,
                                     remove_compute_policy_from_vms):
        """Update an ovdc's compute policies.

        :param str ovdc_name: Name of org VDC to update
        :param str org_name: Name of org that @ovdc_name belongs to
        :param str compute_policy_name: Name of compute policy to add or remove
        :param ComputePolicyAction action:

        :rtype: dict
        """
        method = shared_constants.RequestMethod.PUT
        ovdc = get_vdc(self.client, vdc_name=ovdc_name, org_name=org_name,
                       is_admin_operation=True)
        ovdc_id = utils.extract_id(ovdc.get_resource().get('id'))
        uri = f'{self._uri}/ovdc/{ovdc_id}/compute-policies'

        data = {
            shared_constants.RequestKey.OVDC_ID: ovdc_id, # also exists in url
            shared_constants.RequestKey.COMPUTE_POLICY_NAME: compute_policy_name,  # noqa: E501
            shared_constants.RequestKey.COMPUTE_POLICY_ACTION: action,
            shared_constants.RequestKey.REMOVE_COMPUTE_POLICY_FROM_VMS: remove_compute_policy_from_vms  # noqa: E501
        }

        response = self.client._do_request_prim(
            method,
            uri,
            self.client._session,
            contents=data,
            media_type='application/json',
            accept_type='application/json')
        return process_response(response)

    def list_ovdc_compute_policies(self, ovdc_name, org_name):
        """List an ovdc's compute policies.

        :param str ovdc_name: Name of org VDC to update
        :param str org_name: Name of org that @ovdc_name belongs to

        :rtype: dict
        """
        method = shared_constants.RequestMethod.GET
        ovdc = get_vdc(self.client, vdc_name=ovdc_name, org_name=org_name,
                       is_admin_operation=True)
        ovdc_id = utils.extract_id(ovdc.get_resource().get('id'))
        uri = f'{self._uri}/ovdc/{ovdc_id}/compute-policies'

        response = self.client._do_request_prim(
            method,
            uri,
            self.client._session,
            accept_type='application/json')
        return process_response(response)
