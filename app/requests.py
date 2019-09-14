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

def projects():
    url = base_url.format('projects')
    response = get(url, headers = headers)

    return response.json()