#!/usr/bin/python3
""" Export_to_JSON.py"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    url = ('https://jsonplaceholder.typicode.com/users/')
    employee = requests.get(url + '{}'.format(id)).json()
    tasks = requests.get(url + '{}/todos'.format(id)).json()
    data = []
    all = {}
    all[id] = data
    with open("{}.json".format(id), 'w') as file:
        for task in tasks:
            dic = {}
            dic["task"] = task['title']
            dic["completed"] = task['completed']
            dic["username"] = employee['username']
            data.append(dic)
        json.dump(all, file)
