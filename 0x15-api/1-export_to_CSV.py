#!/usr/bin/python3
""" Export api to csv"""
import csv
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user)
    res = requests.get(user_url)
    """Whatever's gotten"""
    username = res.json().get("username")
    task = user_url + "/todos"
    res = requests.get(task)
    """Whatever's gotten"""
    tasks = res.json()

    with open("{}.csv".format(user), "w") as csvfile:
        for task in tasks:
            completed = task.get("completed")
            """Complete"""
            task_title = task.get("title")
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, username, completed, task_title))
