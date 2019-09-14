from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_projects, get_unscheduled_bug_cards
from ..utils import map_key_values, filter_bugs_states
from datetime import datetime

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    
    projects_found = get_projects()
    
    project_ids = map_key_values(projects_found, 'id')
    
    bugs_found = get_unscheduled_bug_cards(project_ids)

    unstarted_bugs_states = ['unscheduled', 'unstarted', 'planned', 'rejected']

    unstarted_bugs = filter_bugs_states(bugs_found, unstarted_bugs_states)

    inporgess_bugs_states = ['started', 'finished']

    inporgess_bugs = filter_bugs_states(bugs_found, inporgess_bugs_states)

    done_bugs_states = ['delivered', 'accepted']

    done_bugs = filter_bugs_states(bugs_found, done_bugs_states)

    current_year = datetime.now().year
    
    return render_template('index.html', title = title, unstarted = unstarted_bugs, inporgess = inporgess_bugs, done = done_bugs, year = current_year )
