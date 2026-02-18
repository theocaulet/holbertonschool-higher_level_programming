#!/usr/bin/python3
import requests
import csv
"""
This module contains functions to interact with a RESTful API and
save the data to a CSV file.
"""


def fetch_and_print_posts():
    """Defines a function that fetches posts from a RESTful API
      and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Defines a function that fetches posts from a RESTful API
      and saves them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    if r.status_code == 200:
        post = r.json()
        with open("posts.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["id", "title", "body"])
            for p in post:
                writer.writerow([p.get("id"), p.get("title"), p.get("body")])
