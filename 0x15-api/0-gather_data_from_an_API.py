#!/usr/bin/python3
"""
This is the api python script
"""

from requests import get
import sys

if __name__ == "__main__":
    load1 = get('https://jsonplaceholder.typicode.com/todos/')
    data = load1.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks = []
    load_users = get('https://jsonplaceholder.typicode.com/users')
    data2 = load_users.json()

    for i in data2:
        if i.get("id") == int(sys.argv[1]):
            user = i.get('name')

    for element in data:
        if element.get('userId') == int(sys.argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

        if element.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            tasks.append(element.get('title'))
    
    print("Employee {} is done with tasks({}/{}):".format(user, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for e in tasks:
        print("\t {}".format(e))

    
