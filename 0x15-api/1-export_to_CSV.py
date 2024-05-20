#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

def fetch_data(url, path, params=None):
    try:
        response = requests.get(url + path, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = fetch_data(url, "users/{}".format(user_id))
    username = user.get("username")
    if not username:
        print(f"No user found with ID {user_id}")
        sys.exit(1)

    # Fetch to-do list
    todos = fetch_data(url, "todos", params={"userId": user_id})

    # Write to CSV
    csv_filename = "{}.csv".format(user_id)
    try:
        with open(csv_filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for t in todos:
                writer.writerow([user_id, username, t.get("completed"), t.get("title")])
        print(f"Data successfully written to {csv_filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)
