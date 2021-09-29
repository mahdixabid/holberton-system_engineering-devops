#!/usr/bin/python3
"""
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    url = ('https://jsonplaceholder.typicode.com/users/')
    employee = requests.get(url + '{}'.format(
        id)).json()
    tasks = requests.get(url + '{}/todos'.format(id)).json()
    complited = 0
    for task in tasks:
        if task['completed']:
            complited += 1
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee['name'], complited, len(tasks)))
    for task in tasks:
        if task['completed']:
            print("\t {}".format(task['title']))
