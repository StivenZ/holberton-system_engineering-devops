#!/usr/bin/python3
"""Exports all data to JSON"""


if __name__ == "__main__":
    """Formats and displays data from an API request to JSON format
    """
    import json
    import requests
    import sys

    filename = "todo_all_employees.json"

    my_request = requests.get("https://jsonplaceholder.typicode.com/todos/")
    request_decoded = json.loads(my_request.content.decode("UTF-8"))

    name_request = requests.get("https://jsonplaceholder.typicode.com/users/")
    name_decoded = name_request.content.decode("UTF-8")

    u_dict_decoded = json.loads(name_decoded)

    user_dict = {}

    for user in u_dict_decoded:
        task_list = []
        U_ID = user.get("id")
        for task in request_decoded:
            task_dict = {}
            if U_ID == task.get("userId"):
                task_dict = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")
                }
                task_list.append(task_dict)
        user_dict[U_ID] = task_list

    with open(filename, "w") as file:
        json.dump(user_dict, file)
