# ActiveIncidentInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incident_number** | **str** | The VictorOps incident number | [optional] 
**start_time** | **str** | The time the incident started | [optional] 
**current_phase** | **str** | The current phase of the incident \&quot;resolved\&quot;, \&quot;triggered\&quot; or \&quot;acknowledged\&quot;. | [optional] 
**alert_count** | **float** | The number of alerts received for this incident | [optional] 
**last_alert_time** | **str** | The time of the last alert received for the incident | [optional] 
**last_alert_id** | **str** | The unique id of the last alert for the incident | [optional] 
**entity_id** | **str** | The unique identification of the entity being monitored that caused the incident | [optional] 
**host** | **str** | The host on which the incident occurred | [optional] 
**service** | **str** | The service name causing the incident (if any) | [optional] 
**paged_users** | **list[str]** | The users that were paged for the incident. | [optional] 
**paged_teams** | **list[str]** | The teams that were paged for the incident | [optional] 
**transitions** | [**list[IncidentTransition]**](IncidentTransition.md) | Transitions of the incident state over time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


