# TODO: Refactor
def map_ids(list_of_dictionary):
    return [project['id'] for project in list_of_dictionary if 'id' in project]

def map_names(list_of_dictionary):
    return [project['name'] for project in list_of_dictionary if 'name' in project]