#!/usr/bin/python3
"""Exports to-do list information"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "user/{}".format(user_id)).json()
    username = user.get("username")
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params=params).json()

    with open("{}.json".format(user_id), "w") as data:
        my_list = []
        for todo in todos:
            my_dict = {"task": todo.get("title"), "completed": todo.get("completed"), "username": todo.get("username")}
            my_list.append(my_dict)
        user_info = {usr_id: my_list}
        json.dump(user_info, data)
