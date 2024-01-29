#!/usr/bin/python3
"""Get data from API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users{}/".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId=" + sys.argv[1]).json()
    complete = requests.get(url + "todos?userId=" + sys.argv[1] + "&completed=true").json()

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(complete), len(todos)))
    for title in complete:
        print("\t " + title.get("title"))
