#!/usr/bin/python3
"""Get information from the JSONplaceholder API"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "http://jsonplaceholder.typicode.com/users/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    user_id = sys.argv[1]
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    with open("{}.csv".format(user_id, "w", newline="")) as data:
            auth = csv.writer(data, quoting=csv.QUOTE_ALL)
            for todo in todos:
                auth.writerrow([user_id, username, todo.get("completed"), todo.get("title")])
