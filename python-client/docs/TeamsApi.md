# victorops_client.TeamsApi

All URIs are relative to *https://api.victorops.com/api-public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_get**](TeamsApi.md#team_get) | **GET** /team | List teams
[**team_post**](TeamsApi.md#team_post) | **POST** /team | Add a team
[**team_team_delete**](TeamsApi.md#team_team_delete) | **DELETE** /team/{team} | Remove a team
[**team_team_get**](TeamsApi.md#team_team_get) | **GET** /team/{team} | Retrieve information for a team
[**team_team_members_get**](TeamsApi.md#team_team_members_get) | **GET** /team/{team}/members | Retrieve a list of members for a team
[**team_team_members_post**](TeamsApi.md#team_team_members_post) | **POST** /team/{team}/members | Add a team member
[**team_team_members_user_delete**](TeamsApi.md#team_team_members_user_delete) | **DELETE** /team/{team}/members/{user} | Remove a team member
[**team_team_put**](TeamsApi.md#team_team_put) | **PUT** /team/{team} | Update a team


# **team_get**
> ListTeamResponse team_get(x_vo_api_id, x_vo_api_key)

List teams

Get a list of teams for your organization.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key

try: 
    # List teams
    api_response = api_instance.team_get(x_vo_api_id, x_vo_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 

### Return type

[**ListTeamResponse**](ListTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_post**
> AddTeamResponse team_post(x_vo_api_id, x_vo_api_key, body)

Add a team

Add a team to your organization.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
body = victorops_client.AddTeamPayload() # AddTeamPayload | The team information

try: 
    # Add a team
    api_response = api_instance.team_post(x_vo_api_id, x_vo_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->team_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **body** | [**AddTeamPayload**](AddTeamPayload.md)| The team information | 

### Return type

[**AddTeamResponse**](AddTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_delete**
> team_team_delete(x_vo_api_id, x_vo_api_key, team)

Remove a team

Remove a team from your organization.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
team = 'team_example' # str | The VictorOps team to be deleted

try: 
    # Remove a team
    api_instance.team_team_delete(x_vo_api_id, x_vo_api_key, team)
except ApiException as e:
    print("Exception when calling TeamsApi->team_team_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **team** | **str**| The VictorOps team to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_get**
> AddTeamResponse team_team_get(x_vo_api_id, x_vo_api_key, team)

Retrieve information for a team

Get the information for the specified team.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
team = 'team_example' # str | The VictorOps team to fetch

try: 
    # Retrieve information for a team
    api_response = api_instance.team_team_get(x_vo_api_id, x_vo_api_key, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->team_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **team** | **str**| The VictorOps team to fetch | 

### Return type

[**AddTeamResponse**](AddTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_members_get**
> ListTeamMembersResponse team_team_members_get(x_vo_api_id, x_vo_api_key, team)

Retrieve a list of members for a team

Get the members for the specified team.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
team = 'team_example' # str | The VictorOps team to fetch

try: 
    # Retrieve a list of members for a team
    api_response = api_instance.team_team_members_get(x_vo_api_id, x_vo_api_key, team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->team_team_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **team** | **str**| The VictorOps team to fetch | 

### Return type

[**ListTeamMembersResponse**](ListTeamMembersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_members_post**
> ListTeamMembersResponse team_team_members_post(x_vo_api_id, x_vo_api_key, team, body)

Add a team member

Add a team member to your team.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
team = 'team_example' # str | The VictorOps team to fetch
body = victorops_client.AddTeamMemberPayload() # AddTeamMemberPayload | 

try: 
    # Add a team member
    api_response = api_instance.team_team_members_post(x_vo_api_id, x_vo_api_key, team, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->team_team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **team** | **str**| The VictorOps team to fetch | 
 **body** | [**AddTeamMemberPayload**](AddTeamMemberPayload.md)|  | 

### Return type

[**ListTeamMembersResponse**](ListTeamMembersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_members_user_delete**
> team_team_members_user_delete(x_vo_api_id, x_vo_api_key, team, user, body)

Remove a team member

Remove a team from your organization.  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
team = 'team_example' # str | The VictorOps team to be deleted
user = 'user_example' # str | The team member username
body = victorops_client.RemoveTeamMemberPayload() # RemoveTeamMemberPayload | The user information

try: 
    # Remove a team member
    api_instance.team_team_members_user_delete(x_vo_api_id, x_vo_api_key, team, user, body)
except ApiException as e:
    print("Exception when calling TeamsApi->team_team_members_user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **team** | **str**| The VictorOps team to be deleted | 
 **user** | **str**| The team member username | 
 **body** | [**RemoveTeamMemberPayload**](RemoveTeamMemberPayload.md)| The user information | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_team_put**
> AddTeamResponse team_team_put(x_vo_api_id, x_vo_api_key, team, body)

Update a team

Update the designated team  This API may be called a maximum of 15 times per minute. 

### Example 
```python
from __future__ import print_statement
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = victorops_client.TeamsApi()
x_vo_api_id = 'x_vo_api_id_example' # str | Your API ID
x_vo_api_key = 'x_vo_api_key_example' # str | Your API Key
team = 'team_example' # str | The VictorOps team to be updated
body = victorops_client.AddTeamPayload() # AddTeamPayload | The team information

try: 
    # Update a team
    api_response = api_instance.team_team_put(x_vo_api_id, x_vo_api_key, team, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->team_team_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_vo_api_id** | **str**| Your API ID | 
 **x_vo_api_key** | **str**| Your API Key | 
 **team** | **str**| The VictorOps team to be updated | 
 **body** | [**AddTeamPayload**](AddTeamPayload.md)| The team information | 

### Return type

[**AddTeamResponse**](AddTeamResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

