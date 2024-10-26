#!/usr/bin/python3
"""
This script reads stdin line by line and displays statistics based on
accumulated metrics.

Functions:
    print_stats: Prints metrics from stdin read session
    interrupt_handler: Prints metrics upon receival of SIGINT
"""
import re
import signal
import sys

# Initialize counters and data storage
total_file_size = 0
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
line_count = 0


# Function to print accumulated metrics
def print_stats(stats: dict) -> None:
    """Prints the accumulated metrics
    Args:
        stats(dict): Accumulated metrics.
            key - status code
            value - number of occurences of status code
    Return:
        None
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(stats.keys()):
        # Only print status code that appeared
        if stats[status_code] > 0:
            print(f"{status_code}: {stats[status_code]}")


# Signal handler for keyboard interruption (Ctrl + C)
def interrupt_handler(signum, frame):
    """ Handles the SIGINT signal """
    print_stats(stats)


# Register the signal handler
signal.signal(signal.SIGINT, interrupt_handler)


# Read lines from standard input
for line in sys.stdin:
    pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)"

    # Update metrics if input data matches required format
    try:
        match = re.match(pattern, line)
        if match:
            ip_address, timestamp, status_code, file_size = match.groups()
            total_file_size += int(file_size)

            # Update metrics if status code is recognized
            status_code = int(status_code)
            if status_code in stats:
                stats[status_code] += 1

            line_count += 1

    except (ValueError, ImportError):
        pass  # Skip lines with incorrect file size or status code format

    # Display stats after every 10 lines read
    if line_count % 10 == 0:
        print_stats(stats)

# Strict regex pattern for input validation
# FORMAT: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

# IP = r"(25[0-5]|2[0-4]\d|1\d{2}|[0-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[0-9]?\d"
# DATE = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
# TIME = r"(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\.\d{6}"
# STATUS = r"200|301|400|401|403|404|405|500"
# SIZE = r"\d{1,}"

# regex = rf'^({IP}) \- (\[{DATE} {TIME}\]) ("GET /projects/260 HTTP/1.1") ({STATUS}) ({SIZE})$'
