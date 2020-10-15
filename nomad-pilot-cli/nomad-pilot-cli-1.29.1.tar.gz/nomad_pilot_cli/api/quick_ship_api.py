# coding: utf-8

"""
    Nomad Pilot

    This is the API descriptor for the Nomad Pilot API, responsible for shipping and logistics processing. Developed by `Samarkand Global <https://samarkand.global>`_ in partnership with `SF Express <https://www.sf- express.com/cn/sc/>`_, `eSinotrans <http://www.esinotrans.com/haitao.html>`_. Read the documentation online at `Nomad API Suite <https://api.samarkand.io/>`_ and Check out the detailed `changelog <https://gitlab.com/samarkand-nomad/nomad_readme/-/raw/master/history/nomad_pilot.md>`_. - Install for node with ``npm install nomad_pilot_cli`` - Install for python with ``pip install nomad-pilot-cli``  # noqa: E501

    The version of the OpenAPI document: 1.29.1
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nomad_pilot_cli.api_client import ApiClient
from nomad_pilot_cli.exceptions import (
    ApiTypeError,
    ApiValueError
)


class QuickShipApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def quick_ship(self, carrier, package_quick, **kwargs):  # noqa: E501
        """quickShip  # noqa: E501

        Requests waybill creation from specified carrier. Receives waybill details in return, most carriers provide id and PDF packing label  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quick_ship(carrier, package_quick, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str carrier: Carrier to ship (required)
        :param PackageQuick package_quick: Package to quick ship (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.quick_ship_with_http_info(carrier, package_quick, **kwargs)  # noqa: E501

    def quick_ship_with_http_info(self, carrier, package_quick, **kwargs):  # noqa: E501
        """quickShip  # noqa: E501

        Requests waybill creation from specified carrier. Receives waybill details in return, most carriers provide id and PDF packing label  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quick_ship_with_http_info(carrier, package_quick, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str carrier: Carrier to ship (required)
        :param PackageQuick package_quick: Package to quick ship (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApiResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['carrier', 'package_quick']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quick_ship" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'carrier' is set
        if self.api_client.client_side_validation and ('carrier' not in local_var_params or  # noqa: E501
                                                        local_var_params['carrier'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `carrier` when calling `quick_ship`")  # noqa: E501
        # verify the required parameter 'package_quick' is set
        if self.api_client.client_side_validation and ('package_quick' not in local_var_params or  # noqa: E501
                                                        local_var_params['package_quick'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `package_quick` when calling `quick_ship`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'carrier' in local_var_params:
            path_params['carrier'] = local_var_params['carrier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'package_quick' in local_var_params:
            body_params = local_var_params['package_quick']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ca_key']  # noqa: E501

        return self.api_client.call_api(
            '/quick-ship/{carrier}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
