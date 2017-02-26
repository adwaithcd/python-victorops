# victorops_client.UserContactMethodsApi

All URIs are relative to *https://api.victorops.com/api-public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_user_contact_methods_devices_contact_id_delete**](UserContactMethodsApi.md#user_user_contact_methods_devices_contact_id_delete) | **DELETE** /user/{user}/contact-methods/devices/{contactId} | Delete a contact device for a user
[**user_user_contact_methods_devices_contact_id_get**](UserContactMethodsApi.md#user_user_contact_methods_devices_contact_id_get) | **GET** /user/{user}/contact-methods/devices/{contactId} | Get the indicated contact device for a user
[**user_user_contact_methods_devices_contact_id_put**](UserContactMethodsApi.md#user_user_contact_methods_devices_contact_id_put) | **PUT** /user/{user}/contact-methods/devices/{contactId} | Update a contact device for a user
[**user_user_contact_methods_devices_get**](UserContactMethodsApi.md#user_user_contact_methods_devices_get) | **GET** /user/{user}/contact-methods/devices | Get a list of all contact devices for a user
[**user_user_contact_methods_emails_contact_id_delete**](UserContactMethodsApi.md#user_user_contact_methods_emails_contact_id_delete) | **DELETE** /user/{user}/contact-methods/emails/{contactId} | Delete a contact email for a user
[**user_user_contact_methods_emails_contact_id_get**](UserContactMethodsApi.md#user_user_contact_methods_emails_contact_id_get) | **GET** /user/{user}/contact-methods/emails/{contactId} | Get the indicate contact email for a user
[**user_user_contact_methods_emails_contact_id_put**](UserContactMethodsApi.md#user_user_contact_methods_emails_contact_id_put) | **PUT** /user/{user}/contact-methods/emails/{contactId} | Update a contact email for a user
[**user_user_contact_methods_emails_get**](UserContactMethodsApi.md#user_user_contact_methods_emails_get) | **GET** /user/{user}/contact-methods/emails | Get a list of all contact emails for a user
[**user_user_contact_methods_emails_post**](UserContactMethodsApi.md#user_user_contact_methods_emails_post) | **POST** /user/{user}/contact-methods/emails | Create a contact emails for a user
[**user_user_contact_methods_get**](UserContactMethodsApi.md#user_user_contact_methods_get) | **GET** /user/{user}/contact-methods | Get a list of all contact methods for a user
[**user_user_contact_methods_phones_contact_id_delete**](UserContactMethodsApi.md#user_user_contact_methods_phones_contact_id_delete) | **DELETE** /user/{user}/contact-methods/phones/{contactId} | Delete a contact phone for a user
[**user_user_contact_methods_phones_contact_id_get**](UserContactMethodsApi.md#user_user_contact_methods_phones_contact_id_get) | **GET** /user/{user}/contact-methods/phones/{contactId} | Get the indicate contact phone for a user
[**user_user_contact_methods_phones_contact_id_put**](UserContactMethodsApi.md#user_user_contact_methods_phones_contact_id_put) | **PUT** /user/{user}/contact-methods/phones/{contactId} | Update a contact phone for a user
[**user_user_contact_methods_phones_get**](UserContactMethodsApi.md#user_user_contact_methods_phones_get) | **GET** /user/{user}/contact-methods/phones | Get a list of all contact phones for a user
[**user_user_contact_methods_phones_post**](UserContactMethodsApi.md#user_user_contact_methods_phones_post) | **POST** /user/{user}/contact-methods/phones | Create a contact phones for a user


# **user_user_contact_methods_devices_contact_id_delete**
> ContactDevice user_user_contact_methods_devices_contact_id_delete(x_vo_api_id, x_vo_api_key, user, contact_id)

Delete a contact device for a user

Delete a contact device for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier

try: 
    # Delete a contact device for a user
    api_response = api_instance.user_user_contact_methods_devices_contact_id_delete(x_vo_api_id, x_vo_api_key, user, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_devices_contact_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 

### Return type

[**ContactDevice**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_devices_contact_id_get**
> list[ContactDevice] user_user_contact_methods_devices_contact_id_get(x_vo_api_id, x_vo_api_key, user, contact_id)

Get the indicated contact device for a user

Get the indicated contact device for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier

try: 
    # Get the indicated contact device for a user
    api_response = api_instance.user_user_contact_methods_devices_contact_id_get(x_vo_api_id, x_vo_api_key, user, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_devices_contact_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 

### Return type

[**list[ContactDevice]**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_devices_contact_id_put**
> ContactDevice user_user_contact_methods_devices_contact_id_put(x_vo_api_id, x_vo_api_key, user, contact_id, body)

Update a contact device for a user

Update a contact device for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier
body = victorops_client.ContactDeviceAdd() # ContactDeviceAdd | The contact device

try: 
    # Update a contact device for a user
    api_response = api_instance.user_user_contact_methods_devices_contact_id_put(x_vo_api_id, x_vo_api_key, user, contact_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_devices_contact_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 
 **body** | [**ContactDeviceAdd**](ContactDeviceAdd.md)| The contact device | 

### Return type

[**ContactDevice**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_devices_get**
> list[ContactDevice] user_user_contact_methods_devices_get(x_vo_api_id, x_vo_api_key, user)

Get a list of all contact devices for a user

Get the contact methods for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID

try: 
    # Get a list of all contact devices for a user
    api_response = api_instance.user_user_contact_methods_devices_get(x_vo_api_id, x_vo_api_key, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 

### Return type

[**list[ContactDevice]**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_emails_contact_id_delete**
> UserContact user_user_contact_methods_emails_contact_id_delete(x_vo_api_id, x_vo_api_key, user, contact_id)

Delete a contact email for a user

Delete the indicated contact email for the user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier

try: 
    # Delete a contact email for a user
    api_response = api_instance.user_user_contact_methods_emails_contact_id_delete(x_vo_api_id, x_vo_api_key, user, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_emails_contact_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_emails_contact_id_get**
> list[UserContact] user_user_contact_methods_emails_contact_id_get(x_vo_api_id, x_vo_api_key, user, contact_id)

Get the indicate contact email for a user

Get the indicated contact email for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier

try: 
    # Get the indicate contact email for a user
    api_response = api_instance.user_user_contact_methods_emails_contact_id_get(x_vo_api_id, x_vo_api_key, user, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_emails_contact_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 

### Return type

[**list[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_emails_contact_id_put**
> UserContact user_user_contact_methods_emails_contact_id_put(x_vo_api_id, x_vo_api_key, user, contact_id, body)

Update a contact email for a user

Update the indicated contact email for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier
body = victorops_client.ContactEmailAdd() # ContactEmailAdd | The contact email

try: 
    # Update a contact email for a user
    api_response = api_instance.user_user_contact_methods_emails_contact_id_put(x_vo_api_id, x_vo_api_key, user, contact_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_emails_contact_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 
 **body** | [**ContactEmailAdd**](ContactEmailAdd.md)| The contact email | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_emails_get**
> list[UserContact] user_user_contact_methods_emails_get(x_vo_api_id, x_vo_api_key, user)

Get a list of all contact emails for a user

Get the contact emails for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID

try: 
    # Get a list of all contact emails for a user
    api_response = api_instance.user_user_contact_methods_emails_get(x_vo_api_id, x_vo_api_key, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_emails_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 

### Return type

[**list[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_emails_post**
> UserContact user_user_contact_methods_emails_post(x_vo_api_id, x_vo_api_key, user, body)

Create a contact emails for a user

Create a contact email for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
body = victorops_client.ContactEmailAdd() # ContactEmailAdd | The contact email

try: 
    # Create a contact emails for a user
    api_response = api_instance.user_user_contact_methods_emails_post(x_vo_api_id, x_vo_api_key, user, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_emails_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **body** | [**ContactEmailAdd**](ContactEmailAdd.md)| The contact email | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_get**
> InlineResponse200 user_user_contact_methods_get(x_vo_api_id, x_vo_api_key, user)

Get a list of all contact methods for a user

Get the contact methods for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID

try: 
    # Get a list of all contact methods for a user
    api_response = api_instance.user_user_contact_methods_get(x_vo_api_id, x_vo_api_key, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_phones_contact_id_delete**
> UserContact user_user_contact_methods_phones_contact_id_delete(x_vo_api_id, x_vo_api_key, user, contact_id)

Delete a contact phone for a user

Delete the indicated contact phone for the user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier

try: 
    # Delete a contact phone for a user
    api_response = api_instance.user_user_contact_methods_phones_contact_id_delete(x_vo_api_id, x_vo_api_key, user, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_phones_contact_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_phones_contact_id_get**
> list[UserContact] user_user_contact_methods_phones_contact_id_get(x_vo_api_id, x_vo_api_key, user, contact_id)

Get the indicate contact phone for a user

Get the indicated contact phone for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier

try: 
    # Get the indicate contact phone for a user
    api_response = api_instance.user_user_contact_methods_phones_contact_id_get(x_vo_api_id, x_vo_api_key, user, contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_phones_contact_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 

### Return type

[**list[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_phones_contact_id_put**
> UserContact user_user_contact_methods_phones_contact_id_put(x_vo_api_id, x_vo_api_key, user, contact_id, body)

Update a contact phone for a user

Update the indicated contact phone for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
contact_id = 'contact_id_example' # str | The unique contact identifier
body = victorops_client.ContactPhoneAdd() # ContactPhoneAdd | The contact phone

try: 
    # Update a contact phone for a user
    api_response = api_instance.user_user_contact_methods_phones_contact_id_put(x_vo_api_id, x_vo_api_key, user, contact_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_phones_contact_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **contact_id** | **str**| The unique contact identifier | 
 **body** | [**ContactPhoneAdd**](ContactPhoneAdd.md)| The contact phone | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_phones_get**
> list[UserContact] user_user_contact_methods_phones_get(x_vo_api_id, x_vo_api_key, user)

Get a list of all contact phones for a user

Get the contact phones for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID

try: 
    # Get a list of all contact phones for a user
    api_response = api_instance.user_user_contact_methods_phones_get(x_vo_api_id, x_vo_api_key, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_phones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 

### Return type

[**list[UserContact]**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_contact_methods_phones_post**
> UserContact user_user_contact_methods_phones_post(x_vo_api_id, x_vo_api_key, user, body)

Create a contact phones for a user

Create a contact phone for a user  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.UserContactMethodsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
body = victorops_client.ContactPhoneAdd() # ContactPhoneAdd | The contact phone

try: 
    # Create a contact phones for a user
    api_response = api_instance.user_user_contact_methods_phones_post(x_vo_api_id, x_vo_api_key, user, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserContactMethodsApi->user_user_contact_methods_phones_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **body** | [**ContactPhoneAdd**](ContactPhoneAdd.md)| The contact phone | 

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

