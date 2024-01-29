#!/usr/bin/python3
"""Get information from the JSONplaceholder API"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "http://jsonplaceholder.typicode.com/users/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    with open("{}.csv".format(user_id) "w", newline="") as data:
            auth = csv.writer(data, quoting=csv.QUOTE_ALL)
            for todo in todos:
                auth.writerow([user_id, username, todo.get("completed"), todo.get("title")])
