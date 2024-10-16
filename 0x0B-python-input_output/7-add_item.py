#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list():
    """
    Adds all arguments to a Python list and saves them to a file.
    
    The list is saved as a JSON representation in a file named add_item.json.
    If the file doesn't exist, it is created.
    """
    filename = "add_item.json"
    
    try:
        # Try to load existing list from file
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        # If file doesn't exist, start with an empty list
        my_list = []
    
    # Add all arguments to the list
    my_list.extend(sys.argv[1:])
    
    # Save the updated list to the file
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    add_items_to_list()
