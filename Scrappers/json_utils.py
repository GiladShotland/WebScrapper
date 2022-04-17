import json


def get_from_json(file_name):
    with open(file_name) as fn:
        return json.load(fn)

    return none


def initialize_files(articles_list, articles_content):
    with open(articles_list, 'w') as fw:
        json.dump([], fw)

    with open(articles_content, 'w') as fw:
        json.dump({}, fw)


def write_files(articles_set,articles_dict,articles_list, articles_content):
    with open(articles_list, 'w') as fw:
        json.dump(articles_set, fw)

    with open(articles_content, 'w') as fw:
        json.dump(articles_dict, fw)