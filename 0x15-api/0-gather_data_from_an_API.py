#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def fetch_data(url, path, params=None):
    try:
        response = requests.get(url + path, params=params, verify=False)
        response.raise_for_status()  # Raise an HTTPError on bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = fetch_data(url, "users/{}".format(user_id)).json()

    # Fetch to-do list
    todos = fetch_data(url, "todos", params={"userId": user_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))
