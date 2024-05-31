#!/usr/bin/python3
'''
Script to get data from API and convert to JSON
'''

import json
import csv
import requests
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
    res = requests.get(user_url)
    """Docs"""
    username = res.json().get("username")
    """Docs"""
    task_url = user_url + "/todos"
    res = requests.get(task_url)
    tasks = res.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        task_completed_stat = task.get("completed")
        task_title = task.get("title")
        dict_data[USER_ID].append({
            "task": task_title,
            "completed": task_completed_stat,
            "username": username
        })
        """Print dictionary data"""
    with open("{}.json".format(USER_ID), "w") as jsonfile:
        json.dump(dict_data, jsonfile)
        """Print json file"""
