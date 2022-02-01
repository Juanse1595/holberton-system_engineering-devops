#!/usr/bin/python3
'''0-gather_data_from_an_API module'''
import json
from re import sub
import requests
import sys


if __name__ == '__main__':
    given_id = int(sys.argv[1])
    todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(todos_data.text)
    employee_data = requests.get('https://jsonplaceholder.typicode.com/users')
    employees = json.loads(employee_data.text)
    '''Creating the subdictionaries, list and dictionary to export'''
    subdict = {}
    dict_list = []
    dict_export = {}
    '''Getting employee username'''
    for empl in employees:
        if empl['id'] == given_id:
            employee_username = empl['username']
    '''Write to json file'''
    with open("{}.json".format(given_id), "w") as f:
        for todo in todos:
            if todo['userId'] == given_id:
                subdict['task'] = todo['title']
                subdict['completed'] = todo['completed']
                subdict['username'] = employee_username
                dict_list.append(subdict)
        dict_export['{}'.format(given_id)] = dict_list
        json.dump(dict_export, f)
