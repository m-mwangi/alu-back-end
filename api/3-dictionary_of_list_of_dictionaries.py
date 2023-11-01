#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    tasks_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        tasks_response = requests.get(tasks_url)

        user_data = user_response.json()
        tasks_data = tasks_response.json()

        username = user_data["username"]

        task_list = []
        for task in tasks_data:
            task_dict = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            task_list.append(task_dict)

        result = {employee_id: task_list}

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(result, json_file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


