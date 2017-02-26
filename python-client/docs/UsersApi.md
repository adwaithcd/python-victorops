# victorops_client.UsersApi

All URIs are relative to *https://api.victorops.com/api-public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get**](UsersApi.md#user_get) | **GET** /user | List users
[**user_post**](UsersApi.md#user_post) | **POST** /user | Add a user
[**user_user_delete**](UsersApi.md#user_user_delete) | **DELETE** /user/{user} | Remove a user
[**user_user_get**](UsersApi.md#user_user_get) | **GET** /user/{user} | Retrieve information for a user
[**user_user_put**](UsersApi.md#user_user_put) | **PUT** /user/{user} | Update a user


# **user_get**
> ListUserResponse user_get(x_vo_api_id, x_vo_api_key)

List users

Get a list of users for your organization.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UsersApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key

try: 
    # List users
    api_response = api_instance.user_get(x_vo_api_id, x_vo_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> AddUserResponse user_post(x_vo_api_id, x_vo_api_key, body)

Add a user

Add a user to your organization.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UsersApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.AddUserPayload() # AddUserPayload | 

try: 
    # Add a user
    api_response = api_instance.user_post(x_vo_api_id, x_vo_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**AddUserPayload**](AddUserPayload.md)|  | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_delete**
> user_user_delete(x_vo_api_id, x_vo_api_key, user, body)

Remove a user

Remove a user from your organization.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UsersApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user to be deleted
body = victorops_client.DeleteUserPayload() # DeleteUserPayload | 

try: 
    # Remove a user
    api_instance.user_user_delete(x_vo_api_id, x_vo_api_key, user, body)
except ApiException as e:
    print("Exception when calling UsersApi->user_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user to be deleted | 
 **body** | [**DeleteUserPayload**](DeleteUserPayload.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_get**
> AddUserResponse user_user_get(x_vo_api_id, x_vo_api_key, user)

Retrieve information for a user

Get the information for the specified user.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UsersApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user to fetch

try: 
    # Retrieve information for a user
    api_response = api_instance.user_user_get(x_vo_api_id, x_vo_api_key, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user to fetch | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_put**
> AddUserResponse user_user_put(x_vo_api_id, x_vo_api_key, user, body)

Update a user

Update the designated user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UsersApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user to be updated
body = victorops_client.AddUserPayload() # AddUserPayload | 

try: 
    # Update a user
    api_response = api_instance.user_user_put(x_vo_api_id, x_vo_api_key, user, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_user_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user to be updated | 
 **body** | [**AddUserPayload**](AddUserPayload.md)|  | 

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

