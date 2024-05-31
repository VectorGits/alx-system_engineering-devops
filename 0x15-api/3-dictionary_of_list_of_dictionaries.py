#!/usr/bin/python3
"""
Script to fetch REST API data for todo lists of employees
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    users = res.json()

    users_dict = {}
    for user in users:
        userId = user.get("id")
        username = user.get("username")

        url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
               .format(userId))
        url += "/todos"
        res = requests.get(url)

        tasks = res.json()
        users_dict[userId] = []
        for task in tasks:
            task_completed_stat = task.get("completed")
            task_title = task.get("title")
            users_dict[userId].append({
                "task": task_title,
                "completed": task_completed_stat,
                "username": username
            })
            """A lil sth"""
            with open("todo_all_employees.json", "w") as jsonfile:
                json.dump(users_dict, jsonfile)
