#!/usr/bin/python3
"""Get data from API"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users{}/'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={"userId": sys.argv[1]}).json()
    complete = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(complete), len(todos)))
    for title in complete:
        print("\t " + title.get("title"))
