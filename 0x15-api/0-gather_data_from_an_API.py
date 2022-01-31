#!/usr/bin/python3
'''0-gather_data_from_an_API module'''
import json
import requests
import sys


if __name__ == '__main__':
    given_id = int(sys.argv[1])
    todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(todos_data.text)
    employee_data = requests.get('https://jsonplaceholder.typicode.com/users')
    employees = json.loads(employee_data.text)
    '''Getting employee name'''
    for empl in employees:
        if empl['id'] == given_id:
            employee_name = empl['name']
    '''Getting completed tasks, total tasks'''
    done_tasks = 0
    total_tasks = 0
    for todo in todos:
        if todo['userId'] == given_id:
            total_tasks += 1
            if todo['completed'] == True:
                done_tasks += 1
    '''Print first line'''
    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name, done_tasks, total_tasks
    ))
    '''Print second line'''
    for todo in todos:
        if todo['userId'] == given_id:
            if todo['completed']:
                print('\t {}'.format(todo['title']))
