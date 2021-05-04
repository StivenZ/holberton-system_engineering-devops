#!/usr/bin/python3
"""Exports data to JSON"""


if __name__ == "__main__":
    """Formats and displays data from an API request to JSON format
    """
    import json
    import requests
    import sys

    U_ID = int(sys.argv[1])
    filename = sys.argv[1] + ".json"

    my_request = requests.get("https://jsonplaceholder.typicode.com/todos/")
    request_decoded = json.loads(my_request.content.decode("UTF-8"))

    name_request = requests.get("https://jsonplaceholder.typicode.com/users/")
    name_decoded = name_request.content.decode("UTF-8")
    EMPLOYEE_USERNAME = json.loads(name_decoded)[U_ID - 1].get("username")

    task_list = []
    user_dict = {}
    task_dict = {}

    for task in request_decoded:
        if U_ID == task.get("userId"):
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": EMPLOYEE_USERNAME
            }
            task_list.append(task_dict)

    user_dict[sys.argv[1]] = task_list

    with open(filename, "w") as file:
        json.dump(user_dict, file)
