#!/usr/bin/python3
"""
task_02_csv.py
This module provides a function to convert CSV data into JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The CSV file to read from.

    Returns:
        bool: True if conversion is successful, False if an error occurs.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
