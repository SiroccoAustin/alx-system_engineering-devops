#!/usr/bin/python3
"""Get data from API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employ_id = sys.argv[1]
    user = requests.get(url + "users{}/".format(employ_id)).json()
    params = {"userId": employ_id}
    todos = requests.get(url + "todos", params=params).json()
    complete = []
    for todo in todos:
        if todo.get("completed") is True:
            complete.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(complete), len(todos)))
    for title in complete:
        print("\t {}".format(title))
