#!/usr/bin/python3
"""
This script reads stdin line by line and compute metrics based on read.

Functions:
    print_stats: Prints metrics from stdin read session
    interrupt_handler: Prints metrics upon receival of SIGINT
"""
import json
import re
import signal
import sys

# Regex pattern for input validation
IP = "(25[0-5]|2[0-4]\d|1\d{2}|[0-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[0-9]?\d"
DATE = "[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
TIME = "(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\.\d{6}"
STATUS = "200|301|400|401|403|404|405|500"
SIZE = "\d{1,}"

regex = f'^({IP}) \- (\[{DATE} {TIME}\]) ("GET /projects/260 HTTP/1.1") ({STATUS}) ({SIZE})$'

# Metrics storage
stats = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_size = 0
line_count = 0

def print_stats(stats: dict) -> None:
    """Prints the stats of a network session
    Args:
        stats(dict): Statistics of session.
            key - status code
            value - number of occurences of status code
    Return:
        None
    """
    print(f"File size: {total_size}")
    for code, no_of_occurence in stats.items():
        # Only print status code that appeared
        if no_of_occurence > 0:
            print(f"{code}: {no_of_occurence}")

# Interrupt signal handler
def interrupt_handler(signum, frame):
    """ Handles the SIGINT signal """
    print_stats(stats)

signal.signal(signal.SIGINT, interrupt_handler)


# Read from stdin line by line
for line in sys.stdin:
    # Update metrics if input data matches required format
    match = re.search(regex, line)
    if match:
        line_count += 1  # Update line count
        status_code = json.loads(match.group(11))  # Get status code
        data_size = json.loads(match.group(12))  # Get size of data

        total_size += data_size

        if status_code:
            stats[status_code] = stats.get(status_code) + 1

    # Display stats every 10 lines read
    if line_count % 10 == 0:
        print_stats(stats)
