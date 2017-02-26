from decouple import config
import time
import victorops_client
from victorops_client.rest import ApiException
from pprint import pprint

# victorops_client.Configuration().debug = True

VO_API_ID=config('VO_API_ID')
VO_API_KEY=config('VO_API_KEY')

incidents_api=victorops_client.IncidentsApi()

# oncall_api=victorops_client.OncallApi()
# team="ops"
# user='so0k'
# days_forward=14
# days_skip=0
# step=0
#
try:
    api_response=incidents_api.incidents_get(VO_API_ID,VO_API_KEY)
#     api_response=oncall_api.team_team_oncall_schedule_get(
#             x_vo_api_id=VO_API_ID,
#             x_vo_api_key=VO_API_KEY,
#             team=team,
#             days_forward=days_forward,
#             days_skip=days_skip,
#             step=step)
#     pprint(api_response)
#     api_response=oncall_api.user_user_oncall_schedule_get(
#             x_vo_api_id=VO_API_ID,
#             x_vo_api_key=VO_API_KEY,
#             user=user,
#             days_forward=days_forward,
#             days_skip=days_skip,
#             step=step)
    pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" %e)
