#!/usr/bin/python3
""" Exporting"""
import csv
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    url = ('https://jsonplaceholder.typicode.com/users/')
    employee = requests.get(url + '{}'.format(id)).json()
    tasks = requests.get(url + '{}/todos'.format(id)).json()

    with open("{}.csv".format(id), 'w') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow([id, employee['username'],
                                task['completed'],
                                task['title']])
