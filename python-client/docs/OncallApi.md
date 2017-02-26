# victorops_client.OncallApi

All URIs are relative to *https://api.victorops.com/api-public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_team_oncall_schedule_get**](OncallApi.md#team_team_oncall_schedule_get) | **GET** /team/{team}/oncall/schedule | Get a team&#39;s on-call schedule
[**team_team_oncall_user_patch**](OncallApi.md#team_team_oncall_user_patch) | **PATCH** /team/{team}/oncall/user | Create an on-call override (take on-call)
[**user_user_oncall_schedule_get**](OncallApi.md#user_user_oncall_schedule_get) | **GET** /user/{user}/oncall/schedule | Get a user&#39;s on-call schedule


# **team_team_oncall_schedule_get**
> OnCallAndOverrides team_team_oncall_schedule_get(x_vo_api_id, x_vo_api_key, team, days_forward=days_forward, days_skip=days_skip, step=step)

Get a team's on-call schedule

Get the on-call schedule for a user for all teams, including on-call overrides.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.OncallApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
team = 'team_example' # str | The VictorOps team 'slug'
days_forward = 14 # float | Days to include in returned schedule (30 max) (optional) (default to 14)
days_skip = 0 # float | Days to skip before computing schedule to return (90 max) (optional) (default to 0)
step = 0 # float | Step of escalation policy (3 max) (optional) (default to 0)

try: 
    # Get a team's on-call schedule
    api_response = api_instance.team_team_oncall_schedule_get(x_vo_api_id, x_vo_api_key, team, days_forward=days_forward, days_skip=days_skip, step=step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OncallApi->team_team_oncall_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **team** | **str**| The VictorOps team &#39;slug&#39; | 
 **days_forward** | **float**| Days to include in returned schedule (30 max) | [optional] [default to 14]
 **days_skip** | **float**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0]
 **step** | **float**| Step of escalation policy (3 max) | [optional] [default to 0]

### Return type

[**OnCallAndOverrides**](OnCallAndOverrides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_oncall_user_patch**
> TakeResult team_team_oncall_user_patch(x_vo_api_id, x_vo_api_key, body, team)

Create an on-call override (take on-call)

Replaces a currently on-call user on the team with another.  This API may be called a maximum of 6 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.OncallApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.TakeRequest() # TakeRequest | The take on-call payload
team = 'team_example' # str | The VictorOps team 'slug'

try: 
    # Create an on-call override (take on-call)
    api_response = api_instance.team_team_oncall_user_patch(x_vo_api_id, x_vo_api_key, body, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OncallApi->team_team_oncall_user_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**TakeRequest**](TakeRequest.md)| The take on-call payload | 
 **team** | **str**| The VictorOps team &#39;slug&#39; | 

### Return type

[**TakeResult**](TakeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_user_oncall_schedule_get**
> list[OnCallAndOverrides] user_user_oncall_schedule_get(x_vo_api_id, x_vo_api_key, user, days_forward=days_forward, days_skip=days_skip, step=step)

Get a user's on-call schedule

Get the on-call schedule for a user for all teams, including on-call overrides.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.OncallApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
user = 'user_example' # str | The VictorOps user ID
days_forward = 14 # float | Days to include in returned schedule (30 max) (optional) (default to 14)
days_skip = 0 # float | Days to skip before computing schedule to return (90 max) (optional) (default to 0)
step = 0 # float | Step of escalation policy (3 max) (optional) (default to 0)

try: 
    # Get a user's on-call schedule
    api_response = api_instance.user_user_oncall_schedule_get(x_vo_api_id, x_vo_api_key, user, days_forward=days_forward, days_skip=days_skip, step=step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OncallApi->user_user_oncall_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **user** | **str**| The VictorOps user ID | 
 **days_forward** | **float**| Days to include in returned schedule (30 max) | [optional] [default to 14]
 **days_skip** | **float**| Days to skip before computing schedule to return (90 max) | [optional] [default to 0]
 **step** | **float**| Step of escalation policy (3 max) | [optional] [default to 0]

### Return type

[**list[OnCallAndOverrides]**](OnCallAndOverrides.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

