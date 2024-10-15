#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.
"""

import sys
from os import path
from importlib import import_module

# Import the required functions
save_to_json_file = import_module('5-save_to_json_file').save_to_json_file
load_from_json_file = import_module('6-load_from_json_file').load_from_json_file

# Define the filename
filename = "add_item.json"

# Initialize the list
my_list = []

# If the file exists, load its content
if path.exists(filename):
    my_list = load_from_json_file(filename)

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
