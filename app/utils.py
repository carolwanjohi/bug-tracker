from .models import BugCard
import json

def map_key_values(list_of_dictionary, key_wanted):
    return [project[key_wanted] for project in list_of_dictionary if key_wanted in project]

def filter_bugs_states(list_of_dictionary, bugs_state):
    return convert_to_bug_card_object([bug for bug in list_of_dictionary if bug['current_state'] in bugs_state])

def convert_to_bug_card_object(list_of_dictionary):
    bug_card_list = []

    for bug_card in list_of_dictionary:

        title = bug_card.get('id')
        title_link = bug_card.get('url')
        text = bug_card.get('name')

        bug_card_list.append(BugCard(title, title_link, text))
    
    return bug_card_list