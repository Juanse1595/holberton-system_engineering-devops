#!/usr/bin/python3
'''0-gather_data_from_an_API module'''
import csv
import json
import requests
import sys


if __name__ == '__main__':
    given_id = int(sys.argv[1])
    todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(todos_data.text)
    employee_data = requests.get('https://jsonplaceholder.typicode.com/users')
    employees = json.loads(employee_data.text)
    '''Creating row'''
    row = []
    '''Getting employee name'''
    for empl in employees:
        if empl['id'] == given_id:
            employee_username = empl['username']
    with open('{}.csv'.format(given_id), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo['userId'] == given_id:
                row.append(given_id)
                row.append(employee_username)
                row.append(todo['completed'])
                row.append(todo['title'])
                writer.writerow(row)
                row = []
