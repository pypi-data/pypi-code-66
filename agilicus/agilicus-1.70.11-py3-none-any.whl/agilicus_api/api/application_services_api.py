# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.10.15
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from agilicus_api.api_client import ApiClient
from agilicus_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ApplicationServicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_application_service(self, application_service, **kwargs):  # noqa: E501
        """Create an ApplicationService  # noqa: E501

        It is expected that owners for an organisation will provide connectivity to an ApplicationService by defining one here, then adding a reference to an Application's Environment in the ApplicationService's `assignments` list. To see the list of ApplicationServices for which a given Application Environment has access, see that Environment's read only `applications_services` list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_application_service(application_service, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ApplicationService application_service: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApplicationService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_application_service_with_http_info(application_service, **kwargs)  # noqa: E501

    def create_application_service_with_http_info(self, application_service, **kwargs):  # noqa: E501
        """Create an ApplicationService  # noqa: E501

        It is expected that owners for an organisation will provide connectivity to an ApplicationService by defining one here, then adding a reference to an Application's Environment in the ApplicationService's `assignments` list. To see the list of ApplicationServices for which a given Application Environment has access, see that Environment's read only `applications_services` list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_application_service_with_http_info(application_service, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ApplicationService application_service: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApplicationService, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['application_service']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_application_service" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'application_service' is set
        if self.api_client.client_side_validation and ('application_service' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_service'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_service` when calling `create_application_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'application_service' in local_var_params:
            body_params = local_var_params['application_service']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v2/application_services', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationService',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_application_service(self, app_service_id, org_id, **kwargs):  # noqa: E501
        """Remove an ApplicationService  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_application_service(app_service_id, org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_service_id: Application Service unique identifier (required)
        :param str org_id: Organisation unique identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_application_service_with_http_info(app_service_id, org_id, **kwargs)  # noqa: E501

    def delete_application_service_with_http_info(self, app_service_id, org_id, **kwargs):  # noqa: E501
        """Remove an ApplicationService  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_application_service_with_http_info(app_service_id, org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_service_id: Application Service unique identifier (required)
        :param str org_id: Organisation unique identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['app_service_id', 'org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_application_service" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_service_id' is set
        if self.api_client.client_side_validation and ('app_service_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_service_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_service_id` when calling `delete_application_service`")  # noqa: E501
        # verify the required parameter 'org_id' is set
        if self.api_client.client_side_validation and ('org_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['org_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `org_id` when calling `delete_application_service`")  # noqa: E501

        if self.api_client.client_side_validation and 'app_service_id' in local_var_params and not re.search(r'^[a-zA-Z0-9-]+$', local_var_params['app_service_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `app_service_id` when calling `delete_application_service`, must conform to the pattern `/^[a-zA-Z0-9-]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'org_id' in local_var_params and not re.search(r'^[a-zA-Z0-9-]+$', local_var_params['org_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `org_id` when calling `delete_application_service`, must conform to the pattern `/^[a-zA-Z0-9-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'app_service_id' in local_var_params:
            path_params['app_service_id'] = local_var_params['app_service_id']  # noqa: E501

        query_params = []
        if 'org_id' in local_var_params and local_var_params['org_id'] is not None:  # noqa: E501
            query_params.append(('org_id', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v2/application_services/{app_service_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_application_service(self, app_service_id, org_id, **kwargs):  # noqa: E501
        """Get a single ApplicationService  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_service(app_service_id, org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_service_id: Application Service unique identifier (required)
        :param str org_id: Organisation unique identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApplicationService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_application_service_with_http_info(app_service_id, org_id, **kwargs)  # noqa: E501

    def get_application_service_with_http_info(self, app_service_id, org_id, **kwargs):  # noqa: E501
        """Get a single ApplicationService  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_service_with_http_info(app_service_id, org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_service_id: Application Service unique identifier (required)
        :param str org_id: Organisation unique identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApplicationService, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['app_service_id', 'org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_application_service" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_service_id' is set
        if self.api_client.client_side_validation and ('app_service_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_service_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_service_id` when calling `get_application_service`")  # noqa: E501
        # verify the required parameter 'org_id' is set
        if self.api_client.client_side_validation and ('org_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['org_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `org_id` when calling `get_application_service`")  # noqa: E501

        if self.api_client.client_side_validation and 'app_service_id' in local_var_params and not re.search(r'^[a-zA-Z0-9-]+$', local_var_params['app_service_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `app_service_id` when calling `get_application_service`, must conform to the pattern `/^[a-zA-Z0-9-]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'org_id' in local_var_params and not re.search(r'^[a-zA-Z0-9-]+$', local_var_params['org_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `org_id` when calling `get_application_service`, must conform to the pattern `/^[a-zA-Z0-9-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'app_service_id' in local_var_params:
            path_params['app_service_id'] = local_var_params['app_service_id']  # noqa: E501

        query_params = []
        if 'org_id' in local_var_params and local_var_params['org_id'] is not None:  # noqa: E501
            query_params.append(('org_id', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v2/application_services/{app_service_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationService',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_application_services(self, org_id, **kwargs):  # noqa: E501
        """Get a subset of the ApplicationServices  # noqa: E501

        Retrieves all ApplicationServices owned by the Organisation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_application_services(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str org_id: Organisation unique identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ListApplicationServicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_application_services_with_http_info(org_id, **kwargs)  # noqa: E501

    def list_application_services_with_http_info(self, org_id, **kwargs):  # noqa: E501
        """Get a subset of the ApplicationServices  # noqa: E501

        Retrieves all ApplicationServices owned by the Organisation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_application_services_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str org_id: Organisation unique identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ListApplicationServicesResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_application_services" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'org_id' is set
        if self.api_client.client_side_validation and ('org_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['org_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `org_id` when calling `list_application_services`")  # noqa: E501

        if self.api_client.client_side_validation and 'org_id' in local_var_params and not re.search(r'^[a-zA-Z0-9-]+$', local_var_params['org_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `org_id` when calling `list_application_services`, must conform to the pattern `/^[a-zA-Z0-9-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org_id' in local_var_params and local_var_params['org_id'] is not None:  # noqa: E501
            query_params.append(('org_id', local_var_params['org_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v2/application_services', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListApplicationServicesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_application_service(self, app_service_id, **kwargs):  # noqa: E501
        """Create or update an Application Service.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_application_service(app_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_service_id: Application Service unique identifier (required)
        :param ApplicationService application_service:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ApplicationService
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.replace_application_service_with_http_info(app_service_id, **kwargs)  # noqa: E501

    def replace_application_service_with_http_info(self, app_service_id, **kwargs):  # noqa: E501
        """Create or update an Application Service.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_application_service_with_http_info(app_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str app_service_id: Application Service unique identifier (required)
        :param ApplicationService application_service:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ApplicationService, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['app_service_id', 'application_service']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_application_service" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'app_service_id' is set
        if self.api_client.client_side_validation and ('app_service_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['app_service_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_service_id` when calling `replace_application_service`")  # noqa: E501

        if self.api_client.client_side_validation and 'app_service_id' in local_var_params and not re.search(r'^[a-zA-Z0-9-]+$', local_var_params['app_service_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `app_service_id` when calling `replace_application_service`, must conform to the pattern `/^[a-zA-Z0-9-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'app_service_id' in local_var_params:
            path_params['app_service_id'] = local_var_params['app_service_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'application_service' in local_var_params:
            body_params = local_var_params['application_service']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v2/application_services/{app_service_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationService',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
