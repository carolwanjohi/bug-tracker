from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_projects, get_unscheduled_bug_cards
from ..utils import map_ids, map_names, filter_unstarted_bugs

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    
    projects_found = get_projects()
    
    project_ids = map_ids(projects_found)
    
    bugs_found = get_unscheduled_bug_cards(project_ids)

    unstarted_bugs = filter_unstarted_bugs(bugs_found)
    
    return render_template('index.html', title = title, projects = unstarted_bugs )
