# victorops_client.AlertsApi

All URIs are relative to *https://api.victorops.com/api-public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_uuid_get**](AlertsApi.md#alerts_uuid_get) | **GET** /alerts/{uuid} | Retrieve alert details.


# **alerts_uuid_get**
> GetAlertResponse alerts_uuid_get(x_vo_api_id, x_vo_api_key, uuid)

Retrieve alert details.

Retrieve the details of an alert that was sent VictorOps by you.  This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.AlertsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
uuid = 'uuid_example' # str | The VictorOps uuid of the alert

try: 
    # Retrieve alert details.
    api_response = api_instance.alerts_uuid_get(x_vo_api_id, x_vo_api_key, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->alerts_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **uuid** | **str**| The VictorOps uuid of the alert | 

### Return type

[**GetAlertResponse**](GetAlertResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

