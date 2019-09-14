from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_projects, get_unscheduled_bug_cards

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    projects_found = get_projects()
    project_ids = map_ids(projects_found)
    unscheduled_bugs_found = get_unscheduled_bug_cards(project_ids)
    unscheduled_bugs_names = map_names(unscheduled_bugs_found)
    return render_template('index.html', title = title, projects = unscheduled_bugs_names )

# TODO: Refactor
def map_ids(list_of_dictionary):
    return [project['id'] for project in list_of_dictionary if 'id' in project]

def map_names(list_of_dictionary):
    return [project['name'] for project in list_of_dictionary if 'name' in project]
   
