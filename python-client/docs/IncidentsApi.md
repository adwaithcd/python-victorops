# victorops_client.IncidentsApi

All URIs are relative to *https://api.victorops.com/api-public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**incidents_ack_patch**](IncidentsApi.md#incidents_ack_patch) | **PATCH** /incidents/ack | Acknowledge an incident or list of incidents
[**incidents_by_user_ack_patch**](IncidentsApi.md#incidents_by_user_ack_patch) | **PATCH** /incidents/byUser/ack | Acknowledge all incidents for which a user was paged.
[**incidents_by_user_resolve_patch**](IncidentsApi.md#incidents_by_user_resolve_patch) | **PATCH** /incidents/byUser/resolve | Resolve all incidents for which a user was paged.
[**incidents_get**](IncidentsApi.md#incidents_get) | **GET** /incidents | Get current incident information
[**incidents_post**](IncidentsApi.md#incidents_post) | **POST** /incidents | Create a new incident
[**incidents_resolve_patch**](IncidentsApi.md#incidents_resolve_patch) | **PATCH** /incidents/resolve | Resolve an incident or list of incidents


# **incidents_ack_patch**
> AckOrResolveResponse incidents_ack_patch(x_vo_api_id, x_vo_api_key, body)

Acknowledge an incident or list of incidents

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.IncidentsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.AckOrResolveRequest() # AckOrResolveRequest | Ack/Resolve payload

try: 
    # Acknowledge an incident or list of incidents
    api_response = api_instance.incidents_ack_patch(x_vo_api_id, x_vo_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->incidents_ack_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**AckOrResolveRequest**](AckOrResolveRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incidents_by_user_ack_patch**
> AckOrResolveResponse incidents_by_user_ack_patch(x_vo_api_id, x_vo_api_key, body)

Acknowledge all incidents for which a user was paged.

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.IncidentsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.AckOrResolveByUserRequest() # AckOrResolveByUserRequest | Ack/Resolve payload

try: 
    # Acknowledge all incidents for which a user was paged.
    api_response = api_instance.incidents_by_user_ack_patch(x_vo_api_id, x_vo_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->incidents_by_user_ack_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**AckOrResolveByUserRequest**](AckOrResolveByUserRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incidents_by_user_resolve_patch**
> AckOrResolveResponse incidents_by_user_resolve_patch(x_vo_api_id, x_vo_api_key, body)

Resolve all incidents for which a user was paged.

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.IncidentsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.AckOrResolveByUserRequest() # AckOrResolveByUserRequest | Ack/Resolve payload

try: 
    # Resolve all incidents for which a user was paged.
    api_response = api_instance.incidents_by_user_resolve_patch(x_vo_api_id, x_vo_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->incidents_by_user_resolve_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**AckOrResolveByUserRequest**](AckOrResolveByUserRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incidents_get**
> ActiveIncidentList incidents_get(x_vo_api_id, x_vo_api_key)

Get current incident information

Get a list of the currently open, acknowledged and recently resolved incidents. This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.IncidentsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key

try: 
    # Get current incident information
    api_response = api_instance.incidents_get(x_vo_api_id, x_vo_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->incidents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 

### Return type

[**ActiveIncidentList**](ActiveIncidentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incidents_post**
> CreatedIncident incidents_post(x_vo_api_id, x_vo_api_key, body)

Create a new incident

Create a new incident. This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.IncidentsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.CreateIncidentRequest() # CreateIncidentRequest | The incident details

try: 
    # Create a new incident
    api_response = api_instance.incidents_post(x_vo_api_id, x_vo_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->incidents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**CreateIncidentRequest**](CreateIncidentRequest.md)| The incident details | 

### Return type

[**CreatedIncident**](CreatedIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incidents_resolve_patch**
> AckOrResolveResponse incidents_resolve_patch(x_vo_api_id, x_vo_api_key, body)

Resolve an incident or list of incidents

The incident(s) must be currently open.  The user supplied must be a valid VictorOps user and a member of your organization.  This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.IncidentsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.AckOrResolveRequest() # AckOrResolveRequest | Ack/Resolve payload

try: 
    # Resolve an incident or list of incidents
    api_response = api_instance.incidents_resolve_patch(x_vo_api_id, x_vo_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->incidents_resolve_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**AckOrResolveRequest**](AckOrResolveRequest.md)| Ack/Resolve payload | 

### Return type

[**AckOrResolveResponse**](AckOrResolveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

