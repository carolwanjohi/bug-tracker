import urllib.request,json

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
    request = urllib.request.Request(url, headers)
    response = urllib.request.urlopen(request)
    # with urllib.request.urlopen(request) as response:
        # project_data = response.read()
        # print('project_data', project_data)
        # project_data_response = json.loads(project_data)

    # print('project_data_response', project_data_response)

    return 'more to come'