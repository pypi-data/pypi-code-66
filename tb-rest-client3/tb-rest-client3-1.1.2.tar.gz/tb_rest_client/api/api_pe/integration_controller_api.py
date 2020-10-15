# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class IntegrationControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_integration_using_delete(self, integration_id, **kwargs):  # noqa: E501
        """deleteIntegration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_integration_using_delete(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: integrationId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_integration_using_delete_with_http_info(integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_integration_using_delete_with_http_info(integration_id, **kwargs)  # noqa: E501
            return data

    def delete_integration_using_delete_with_http_info(self, integration_id, **kwargs):  # noqa: E501
        """deleteIntegration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.delete_integration_using_delete_with_http_info(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: integrationId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params or
                params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `delete_integration_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/integration/{integrationId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integration_by_id_using_get(self, integration_id, **kwargs):  # noqa: E501
        """getIntegrationById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integration_by_id_using_get(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: integrationId (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_by_id_using_get_with_http_info(integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_by_id_using_get_with_http_info(integration_id, **kwargs)  # noqa: E501
            return data

    def get_integration_by_id_using_get_with_http_info(self, integration_id, **kwargs):  # noqa: E501
        """getIntegrationById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integration_by_id_using_get_with_http_info(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: integrationId (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params or
                params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `get_integration_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/integration/{integrationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Integration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integration_by_routing_key_using_get(self, routing_key, **kwargs):  # noqa: E501
        """getIntegrationByRoutingKey  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integration_by_routing_key_using_get(routing_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integration_by_routing_key_using_get_with_http_info(routing_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integration_by_routing_key_using_get_with_http_info(routing_key, **kwargs)  # noqa: E501
            return data

    def get_integration_by_routing_key_using_get_with_http_info(self, routing_key, **kwargs):  # noqa: E501
        """getIntegrationByRoutingKey  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integration_by_routing_key_using_get_with_http_info(routing_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `get_integration_by_routing_key_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/integration/routingKey/{routingKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Integration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integrations_by_ids_using_get(self, integration_ids, **kwargs):  # noqa: E501
        """getIntegrationsByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integrations_by_ids_using_get(integration_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_ids: integrationIds (required)
        :return: list[Integration]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integrations_by_ids_using_get_with_http_info(integration_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integrations_by_ids_using_get_with_http_info(integration_ids, **kwargs)  # noqa: E501
            return data

    def get_integrations_by_ids_using_get_with_http_info(self, integration_ids, **kwargs):  # noqa: E501
        """getIntegrationsByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integrations_by_ids_using_get_with_http_info(integration_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_ids: integrationIds (required)
        :return: list[Integration]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_ids' is set
        if ('integration_ids' not in params or
                params['integration_ids'] is None):
            raise ValueError("Missing the required parameter `integration_ids` when calling `get_integrations_by_ids_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'integration_ids' in params:
            query_params.append(('integrationIds', params['integration_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/integrations{?integrationIds}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Integration]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_integrations_using_get(self, page_size, page, **kwargs):  # noqa: E501
        """getIntegrations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integrations_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_integrations_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_integrations_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_integrations_using_get_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """getIntegrations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_integrations_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_integrations_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_integrations_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/integrations{?textSearch,sortProperty,sortOrder,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataIntegration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_integration_using_post(self, integration, **kwargs):  # noqa: E501
        """saveIntegration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_integration_using_post(integration, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Integration integration: integration (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_integration_using_post_with_http_info(integration, **kwargs)  # noqa: E501
        else:
            (data) = self.save_integration_using_post_with_http_info(integration, **kwargs)  # noqa: E501
            return data

    def save_integration_using_post_with_http_info(self, integration, **kwargs):  # noqa: E501
        """saveIntegration  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_integration_using_post_with_http_info(integration, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Integration integration: integration (required)
        :return: Integration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration' is set
        if ('integration' not in params or
                params['integration'] is None):
            raise ValueError("Missing the required parameter `integration` when calling `save_integration_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'integration' in params:
            body_params = params['integration']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/integration', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Integration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
