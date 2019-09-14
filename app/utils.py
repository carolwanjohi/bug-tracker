# TODO: Refactor
def map_key_values(list_of_dictionary, key_wanted):
    return [project[key_wanted] for project in list_of_dictionary if key_wanted in project]

def filter_bugs_states(list_of_dictionary, bugs_state):
    return [bug for bug in list_of_dictionary if bug['current_state'] in bugs_state]