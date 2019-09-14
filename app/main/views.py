from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_projects

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    projects_found = get_projects()

    return render_template('index.html', title = title, projects = projects_found )
   

