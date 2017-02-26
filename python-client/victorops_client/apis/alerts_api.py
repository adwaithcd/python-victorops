# coding: utf-8

"""
    VictorOps API

    This API allows you to interact with the VictorOps platform in various ways. Your account may be limited to a total number of API calls per month. Also, some of these API calls have rate limits.  NOTE: In this documentation when creating a sample curl request (clicking the TRY IT OUT! button), in some API viewing interfaces, the '@' in an email address may be encoded. Please note that the REST endpoints will not process the encoded version. Make sure that the encoded character '%40' is changed to its unencoded form before submitting the curl request. 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AlertsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def alerts_uuid_get(self, x_vo_api_id, x_vo_api_key, uuid, **kwargs):
        """
        Retrieve alert details.
        Retrieve the details of an alert that was sent VictorOps by you.  This API may be called a maximum of 6 times per minute. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alerts_uuid_get(x_vo_api_id, x_vo_api_key, uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_vo_api_id: Your API ID (required)
        :param str x_vo_api_key: Your API Key (required)
        :param str uuid: The VictorOps uuid of the alert (required)
        :return: GetAlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.alerts_uuid_get_with_http_info(x_vo_api_id, x_vo_api_key, uuid, **kwargs)
        else:
            (data) = self.alerts_uuid_get_with_http_info(x_vo_api_id, x_vo_api_key, uuid, **kwargs)
            return data

    def alerts_uuid_get_with_http_info(self, x_vo_api_id, x_vo_api_key, uuid, **kwargs):
        """
        Retrieve alert details.
        Retrieve the details of an alert that was sent VictorOps by you.  This API may be called a maximum of 6 times per minute. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.alerts_uuid_get_with_http_info(x_vo_api_id, x_vo_api_key, uuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_vo_api_id: Your API ID (required)
        :param str x_vo_api_key: Your API Key (required)
        :param str uuid: The VictorOps uuid of the alert (required)
        :return: GetAlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_vo_api_id', 'x_vo_api_key', 'uuid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alerts_uuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_vo_api_id' is set
        if ('x_vo_api_id' not in params) or (params['x_vo_api_id'] is None):
            raise ValueError("Missing the required parameter `x_vo_api_id` when calling `alerts_uuid_get`")
        # verify the required parameter 'x_vo_api_key' is set
        if ('x_vo_api_key' not in params) or (params['x_vo_api_key'] is None):
            raise ValueError("Missing the required parameter `x_vo_api_key` when calling `alerts_uuid_get`")
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params) or (params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `alerts_uuid_get`")


        collection_formats = {}

        resource_path = '/alerts/{uuid}'.replace('{format}', 'json')
        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']

        query_params = {}

        header_params = {}
        if 'x_vo_api_id' in params:
            header_params['X-VO-Api-Id'] = params['x_vo_api_id']
        if 'x_vo_api_key' in params:
            header_params['X-VO-Api-Key'] = params['x_vo_api_key']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetAlertResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
