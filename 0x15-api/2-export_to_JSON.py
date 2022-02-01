#!/usr/bin/python3
'''2-export_to_JSON module'''
import json
import requests
import sys


if __name__ == '__main__':
    given_id = int(sys.argv[1])
    '''List of tasks done by userId user'''
    todos = requests.get('https://jsonplaceholder.typicode.com/\
todos?userId={}'.format(given_id)).json()
    employees = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(given_id)).json()
    '''Creating the subdictionaries, list and dictionary to export'''
    subdict = {}
    dict_list = []
    dict_export = {}
    '''Getting employee username'''
    employee_username = employees.get('username')
    '''Making the export dictionary'''
    for todo in todos:
        subdict['task'] = todo.get('title')
        subdict['completed'] = todo.get('completed')
        subdict['username'] = employee_username
        dict_list.append(subdict)
        subdict = {}
    dict_export[given_id] = dict_list
    '''Write to json file'''
    with open("{}.json".format(given_id), "w") as f:
        json.dump(dict_export, f)
