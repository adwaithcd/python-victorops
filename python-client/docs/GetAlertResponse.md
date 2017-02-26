# GetAlertResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** | The type of alert; INFO, WARNING, ACKNOWLEDGEMENT, CRITICAL, RECOVERY  | [optional] 
**entity_id** | **str** | Identifies the entity (host, service, etc.) this alert was about.  | [optional] 
**timestamp** | **float** | Timestamp of the alert in seconds since epoch. | [optional] 
**state_start_time** | **float** | The time this entity entered its current state (seconds since epoch). | [optional] 
**state_message** | **str** | Any additional status information from the alert item. | [optional] 
**monitoring_tool** | **str** | The name of the monitoring system software (eg. nagios, icinga, sensu, etc.) | [optional] 
**entity_display_name** | **str** | Used within VictorOps to display a human-readable name for the entity. | [optional] 
**ack_msg** | **str** | A user entered comment for the acknowledgment. | [optional] 
**ack_author** | **str** | The user that acknowledged the incident. | [optional] 
**raw** | **str** | The full, raw alert details JSON string (i.e. parse the string into a JSON object)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


