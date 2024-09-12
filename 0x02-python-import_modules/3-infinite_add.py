#!/usr/bin/python3
import sys

total = 0
for args in sys.argv[1:]:
    total += args

print(total)
