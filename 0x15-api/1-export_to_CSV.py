#!/usr/bin/python3
"""Exports data to csv"""


if __name__ == "__main__":
    """Formats and displays data from an API request
    """
    import csv
    import json
    import requests
    import sys

    U_ID = int(sys.argv[1])
    filename = sys.argv[1] + ".csv"
    my_request = requests.get("https://jsonplaceholder.typicode.com/todos/")
    request_decoded = json.loads(my_request.content.decode("UTF-8"))

    name_request = requests.get("https://jsonplaceholder.typicode.com/users/")
    name_decoded = name_request.content.decode("UTF-8")
    EMPLOYEE_USERNAME = json.loads(name_decoded)[U_ID - 1].get("username")

    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter=',')
        for task in request_decoded:
            if U_ID == task.get("userId"):
                writer.writerow([U_ID,
                                EMPLOYEE_USERNAME,
                                task.get("completed"),
                                task.get("title")])
