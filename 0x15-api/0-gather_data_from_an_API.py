#!/usr/bin/python3
"""Request data from an API"""


if __name__ == "__main__":
    """Formats and displays data from an API request
    """
    import json
    import requests
    import sys

    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    EMPLOYEE_ID = int(sys.argv[1])
    my_request = requests.get("https://jsonplaceholder.typicode.com/todos/")
    request_decoded = json.loads(my_request.content.decode("UTF-8"))

    name_request = requests.get("https://jsonplaceholder.typicode.com/users/")
    name_decoded = name_request.content.decode("UTF-8")
    EMPLOYEE_NAME = json.loads(name_decoded)[EMPLOYEE_ID - 1].get("name")

    for task in request_decoded:
        if EMPLOYEE_ID == task.get("userId"):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get("completed"):
                NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with\
 tasks({}/{}):".format(EMPLOYEE_NAME,
                       NUMBER_OF_DONE_TASKS,
                       TOTAL_NUMBER_OF_TASKS))
    for task in request_decoded:
        if EMPLOYEE_ID == task.get("userId"):
            if task.get("completed"):
                print("\t {}".format(task.get("title")))
