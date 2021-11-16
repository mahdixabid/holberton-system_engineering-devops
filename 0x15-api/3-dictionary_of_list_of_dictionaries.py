#!/usr/bin/python3
""" Exporting to json."""
import json
import requests

if __name__ == "__main__":

    employee = requests.get("https://jsonplaceholder.typicode.com/users")\
        .json()
    all = {}
    for user in employee:
        id = user['id']
        emp = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(
                               id)).json()
        tasks = requests.get(
                "https://jsonplaceholder.typicode.com/users/{}/todos"
                .format(
                    id)).json()
        data = []

        all[id] = data
        for task in tasks:
            dic = {}
            dic["username"] = emp['username']
            dic["task"] = task['title']
            dic["completed"] = task['completed']
            data.append(dic)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all, file)
