#!/usr/bin/python3
'''
A Python script that, using this REST API,
for a given employee ID, returns information 
about his/her TODO list progress.
'''

import requests
import sys
# import re

def get_employee_todo_progress(employee_id):
	"""Fetches and prints the todo list progress of an employee by id."""
	user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
	todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

	user = requests.get(user_url).json()['name']
	todo_list = requests.get(todo_url).json()

	total_tasks = len(todo_list)
	done_tasks = len([task for task in todo_list if task['completed']])
	done_tasks_titles = [task['title'] for task in todo_list if task['completed']]

	print(f"Employee {user} is done with tasks({done_tasks}/{total_tasks}):")
	for title in done_tasks_titles:
		print(f"\t {title}")
		
	if __name__ == "__main__":
		employee_id = sys.argv[1]
		get_employee_todo_progress(employee_id)
