#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    if not username:
        sys.exit(1)
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    json_filename = "{}.json".format(user_id)
    try:
        with open(json_filename, "w") as jsonfile:
            json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
    except IOError as e:
        sys.exit(1)
