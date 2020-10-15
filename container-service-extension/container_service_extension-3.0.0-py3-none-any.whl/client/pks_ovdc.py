# container-service-extension
# Copyright (c) 2019 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

from pyvcloud.vcd import utils

from container_service_extension.client.response_processor import \
    process_response
from container_service_extension.pyvcloud_utils import get_vdc
import container_service_extension.server_constants as server_constants
import container_service_extension.shared_constants as shared_constants


class PksOvdc:
    def __init__(self, client):
        self.client = client
        self._uri = f"{self.client.get_api_uri()}/{shared_constants.PKS_URL_FRAGMENT}"  # noqa: E501

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

    def update_ovdc(self, enable, ovdc_name, org_name=None,
                    pks_plan=None, pks_cluster_domain=None):
        """Enable/Disable ovdc for k8s for the given container provider.

        :param bool enable: If set to True will enable the vdc for the
            paricular k8s_provider else if set to False, K8 support on
            the vdc will be disabled.
        :param str ovdc_name: Name of org VDC to update
        :param str org_name: Name of org that @ovdc_name belongs to
        :param str pks_plan: PKS plan
        :param str pks_cluster_domain: Suffix of the domain name, which will be
         used to construct FQDN of the clusters.

        :rtype: dict
        """
        method = shared_constants.RequestMethod.PUT
        ovdc = get_vdc(self.client, vdc_name=ovdc_name, org_name=org_name,
                       is_admin_operation=True)
        ovdc_id = utils.extract_id(ovdc.get_resource().get('id'))
        uri = f'{self._uri}/ovdc/{ovdc_id}'

        k8s_provider = server_constants.K8sProvider.PKS
        if not enable:
            k8s_provider = server_constants.K8sProvider.NONE
            pks_plan = None
            pks_cluster_domain = None

        data = {
            shared_constants.RequestKey.OVDC_ID: ovdc_id,
            shared_constants.RequestKey.OVDC_NAME: ovdc_name,
            shared_constants.RequestKey.ORG_NAME: org_name,
            shared_constants.RequestKey.K8S_PROVIDER: k8s_provider,
            shared_constants.RequestKey.PKS_PLAN_NAME: pks_plan,
            shared_constants.RequestKey.PKS_CLUSTER_DOMAIN: pks_cluster_domain
        }

        response = self.client._do_request_prim(
            method,
            uri,
            self.client._session,
            contents=data,
            media_type='application/json',
            accept_type='application/json')
        return process_response(response)

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
