# API
This project is aimed to understand and work with APIs.
---

0. Gather data from an API:

&nbsp;&nbsp;Using a specific REST API, returns information about a TODO list progress given a certain employee ID.

&nbsp;&nbsp;USAGE: ```$ python3 0-gather_data_from_an_API.py USER_ID```



1. Export to CSV:

&nbsp;&nbsp;Extended script to export information about certain employee to the file "USER_ID.csv" with this format:
&nbsp;"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

&nbsp;&nbsp;USAGE: ```$ python3 1-export_to_CSV.py USER_ID```



2. Export to JSON:

&nbsp;&nbsp;Extended script to export information about certain employee to the file "USER_ID.json" with this format:
&nbsp;{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

&nbsp;&nbsp;USAGE: ```$ python3 2-export_to_JSON.py USER_ID```



3.  Dictionary of list of dictionaries:

&nbsp;&nbsp;Extended script to export information about all employees to the file "todo_all_employees.json" with this format:
&nbsp;{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

&nbsp;&nbsp;USAGE: ```$ python3 3-dictionary_of_list_of_dictionaries.py```
