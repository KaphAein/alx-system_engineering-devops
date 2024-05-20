#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    if not username:
        sys.exit(1)
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    csv_filename = "{}.csv".format(user_id)
    try:
        with open(csv_filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for t in todos:
                writer.writerow([user_id, username,
                                 t.get("completed"), t.get("title")])
    except IOError as e:
        sys.exit(1)
