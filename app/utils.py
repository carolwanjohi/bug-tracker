# TODO: Refactor
def map_ids(list_of_dictionary):
    return [project['id'] for project in list_of_dictionary if 'id' in project]

def map_names(list_of_dictionary):
    return [project['name'] for project in list_of_dictionary if 'name' in project]

def filter_unstarted_bugs(list_of_dictionary):
    unstarted_bugs = ['unscheduled', 'unstarted', 'planned', 'rejected']
    return [bug for bug in list_of_dictionary if bug['current_state'] in unstarted_bugs]