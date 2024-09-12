#!/usr/bin/python3
import sys

def print_arguments():
    argc = len(sys.argv) - 1
    
    if argc == 1:
        print("1 argument:")
    elif argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} arguments:")
    
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
