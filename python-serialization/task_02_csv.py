#!/usr/bin/python3
import csv
import json
"""This module provides functions to convert CSV files to JSON format."""


def convert_csv_to_json(csv_file, json_file='data.json'):
    """Define a function that converts a CSV file to JSON format."""
    try:
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        with open(json_file, 'w') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
