#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""

import sys

def print_stats(total_size, status_counts):
    """
    Prints the computed statistics.

    Args:
        total_size (int): Total file size.
        status_counts (dict): Dictionary holding counts of status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        try:
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_size += file_size

            # Update status code count if it's one of the expected codes
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (IndexError, ValueError):
            # Handle lines that don't conform to expected format
            continue

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    # Print statistics on keyboard interrupt (CTRL + C)
    print_stats(total_size, status_counts)
    raise

# Print final statistics after EOF
print_stats(total_size, status_counts)
