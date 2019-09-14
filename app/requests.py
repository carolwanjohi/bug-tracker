import urllib.request,json
from requests import get

# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['API_TOKEN']
    base_url = app.config['PIVOTAL_BASE_URL']

def projects():
    url = base_url.format('projects')
    headers =  { 'X-TrackerToken': api_key }
    response = get(url, headers = headers)

    return response.json()