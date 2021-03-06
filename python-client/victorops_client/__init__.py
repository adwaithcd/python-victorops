# coding: utf-8

"""
    VictorOps API

    This API allows you to interact with the VictorOps platform in various ways. Your account may be limited to a total number of API calls per month. Also, some of these API calls have rate limits.  NOTE: In this documentation when creating a sample curl request (clicking the TRY IT OUT! button), in some API viewing interfaces, the '@' in an email address may be encoded. Please note that the REST endpoints will not process the encoded version. Make sure that the encoded character '%40' is changed to its unencoded form before submitting the curl request. 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.ack_or_resolve_by_user_request import AckOrResolveByUserRequest
from .models.ack_or_resolve_request import AckOrResolveRequest
from .models.ack_or_resolve_response import AckOrResolveResponse
from .models.ack_or_resolve_result import AckOrResolveResult
from .models.ack_user import AckUser
from .models.active_incident_info import ActiveIncidentInfo
from .models.active_incident_list import ActiveIncidentList
from .models.add_team_member_payload import AddTeamMemberPayload
from .models.add_team_payload import AddTeamPayload
from .models.add_team_response import AddTeamResponse
from .models.add_user_payload import AddUserPayload
from .models.add_user_response import AddUserResponse
from .models.contact_device import ContactDevice
from .models.contact_device_add import ContactDeviceAdd
from .models.contact_email_add import ContactEmailAdd
from .models.contact_phone_add import ContactPhoneAdd
from .models.create_incident_request import CreateIncidentRequest
from .models.created_incident import CreatedIncident
from .models.delete_user_payload import DeleteUserPayload
from .models.get_alert_response import GetAlertResponse
from .models.incident_info import IncidentInfo
from .models.incident_list import IncidentList
from .models.incident_target import IncidentTarget
from .models.incident_transition import IncidentTransition
from .models.inline_response_200 import InlineResponse200
from .models.list_team_members_response import ListTeamMembersResponse
from .models.list_team_response import ListTeamResponse
from .models.list_user_response import ListUserResponse
from .models.on_call_and_overrides import OnCallAndOverrides
from .models.on_call_interval import OnCallInterval
from .models.on_call_log import OnCallLog
from .models.rel_link import RelLink
from .models.remove_team_member_payload import RemoveTeamMemberPayload
from .models.take_request import TakeRequest
from .models.take_result import TakeResult
from .models.team_member import TeamMember
from .models.team_schedule_overlay_resource import TeamScheduleOverlayResource
from .models.team_schedule_resource import TeamScheduleResource
from .models.team_schedule_roll_resource import TeamScheduleRollResource
from .models.user_contact import UserContact
from .models.user_log import UserLog
from .models.user_log_total import UserLogTotal
from .models.v1_user import V1User

# import apis into sdk package
from .apis.alerts_api import AlertsApi
from .apis.incidents_api import IncidentsApi
from .apis.oncall_api import OncallApi
from .apis.reporting_api import ReportingApi
from .apis.teams_api import TeamsApi
from .apis.user_contact_methods_api import UserContactMethodsApi
from .apis.users_api import UsersApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
