#!/usr/bin/python3
"""
Export data to JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    try:
        user_response = requests.get(users_url)
        users_data = user_response.json()

        data_to_export = {}

        for user in users_data:
            user_id = user["id"]
            username = user["username"]

            tasks_url = f"{base_url}/todos?userId={user_id}"
            tasks_response = requests.get(tasks_url)
            tasks_data = tasks_response.json()

            tasks_list = []
            for task in tasks_data:
                task_dict = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                tasks_list.append(task_dict)

            data_to_export[str(user_id)] = tasks_list

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(data_to_export, json_file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
