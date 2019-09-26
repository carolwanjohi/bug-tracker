import urllib.request,json
from requests import get, post

# Getting the api key
api_key = None

# Getting the base url
base_url = None

# Getting the headers
headers = None

# Getting the slack webhook
webhook = None

def configure_request(app):
    global api_key, base_url, headers, webhook
    api_key = app.config['API_TOKEN']
    base_url = app.config['PIVOTAL_BASE_URL']
    headers =  { 'X-TrackerToken': api_key }
    webhook = app.config['WEBHOOK_URL']

def get_projects():
    url = base_url.format('projects')
    response = get(url, headers = headers)
    return response.json()

def get_unscheduled_bug_cards(project_ids):
    combined_list = []
    for project_id in project_ids:
        url = base_url.format('projects/'+str(project_id)+'/stories?with_story_type=bug')
        response = get(url, headers = headers)
        combined_list.extend(response.json())
        len(combined_list)
    return combined_list

def post_to_bug_tracker_channel(list_of_bugs, state_of_bugs):
    slack_acctachments = { "text": state_of_bugs, "attachments": list_of_bugs}
    payload = json.dumps(slack_acctachments, default=obj_dict)
    post(webhook, data=payload)
    return "send to slack"

def obj_dict(obj):
    '''
    Map object to a python dictionary
    '''
    return obj.__dict__