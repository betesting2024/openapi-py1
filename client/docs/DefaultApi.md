# openapi_client.DefaultApi

All URIs are relative to *http://localhost:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_app**](DefaultApi.md#add_app) | **POST** /Apps | 
[**delete_app**](DefaultApi.md#delete_app) | **DELETE** /Apps/{id} | 
[**find_app_by_id**](DefaultApi.md#find_app_by_id) | **GET** /Apps/{id} | 
[**find_apps**](DefaultApi.md#find_apps) | **GET** /Apps | 


# **add_app**
> App add_app(new_app)



Creates a new App in the store. Duplicates are allowed

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.app import App
from openapi_client.models.new_app import NewApp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    new_app = openapi_client.NewApp() # NewApp | App to add to the store

    try:
        api_response = api_instance.add_app(new_app)
        print("The response of DefaultApi->add_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_app** | [**NewApp**](NewApp.md)| App to add to the store | 

### Return type

[**App**](App.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> delete_app(id)



deletes a single App based on the ID supplied

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | ID of App to delete

    try:
        api_instance.delete_app(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_app: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of App to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | App deleted |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_app_by_id**
> App find_app_by_id(id)



Returns a user based on a single ID, if the user does not have access to the App

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.app import App
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | ID of App to fetch

    try:
        api_response = api_instance.find_app_by_id(id)
        print("The response of DefaultApi->find_app_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->find_app_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of App to fetch | 

### Return type

[**App**](App.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_apps**
> List[App] find_apps(tags=tags, limit=limit)



Returns all Apps from the system that the user has access to Write more documentation here And here! 

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.app import App
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    tags = ['tags_example'] # List[str] | tags to filter by (optional)
    limit = 56 # int | maximum number of results to return (optional)

    try:
        api_response = api_instance.find_apps(tags=tags, limit=limit)
        print("The response of DefaultApi->find_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->find_apps: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**List[str]**](str.md)| tags to filter by | [optional] 
 **limit** | **int**| maximum number of results to return | [optional] 

### Return type

[**List[App]**](App.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App response |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

