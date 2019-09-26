from .models import BugCard
import json

def map_key_values(list_of_dictionary, key_wanted):
    return [project[key_wanted] for project in list_of_dictionary if key_wanted in project]

def filter_bugs_states(list_of_dictionary, bugs_state):
    return convert_to_bug_card_object([bug for bug in list_of_dictionary if bug['current_state'] in bugs_state])

def convert_to_bug_card_object(list_of_dictionary):
    bug_card_list = []

    for bug_card in list_of_dictionary:

        id = bug_card.get('id')
        name = bug_card.get('name')
        url = bug_card.get('url')

        bug_card_list.append(BugCard(id, name, url))
    
    return bug_card_list