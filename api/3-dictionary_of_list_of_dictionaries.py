#!/usr/bin/python3
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    tasks = response.json()

    # Create a dictionary to store tasks for each user
    user_tasks = {}
    for task in tasks:
        user_id = task["userId"]
        task_info = {
            "username": task["title"],
            "task": task["title"],
            "completed": task["completed"]
        }

        # If user_id already exists in the dictionary, append the task, else create a new user entry
        if user_id in user_tasks:
            user_tasks[user_id].append(task_info)
        else:
            user_tasks[user_id] = [task_info]

    # Convert the dictionary to JSON format
    json_data = json.dumps(user_tasks, indent=4)

    # Write JSON data to a file
    with open("todo_all_employees.json", "w") as outfile:
        outfile.write(json_data)

