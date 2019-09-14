import urllib.request,json
from requests import get

# Getting the api key
api_key = None

# Getting the base url
base_url = None

# Getting the headers
headers = None

def configure_request(app):
    global api_key, base_url, headers
    api_key = app.config['API_TOKEN']
    base_url = app.config['PIVOTAL_BASE_URL']
    headers =  { 'X-TrackerToken': api_key }

def get_projects():
    url = base_url.format('projects')
    response = get(url, headers = headers)
    project_ids = map_project_ids(response.json())
    project_names = map_project_names(response.json())
    return [{'project_ids': project_ids}, {'project_names': project_names}]

# TODO: Refactor
def map_project_ids(projects):
    return [project['id'] for project in projects if 'id' in project]

def map_project_names(projects):
    return [project['name'] for project in projects if 'name' in project]
