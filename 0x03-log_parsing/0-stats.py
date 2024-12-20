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
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


# Function to print accumulated metrics
def print_stats() -> None:
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


# Handle broken pipe signal
def broken_pipe_handler(signum, frame):
    """ Handle broken pipe signal silently."""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGPIPE, broken_pipe_handler)


# Read lines from standard input
try:
    for line in sys.stdin:
        pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)$"

        # Update metrics if input data matches required format
        try:
            match = re.match(pattern, line)
            if match:
                ip_address, timestamp, status_code, file_size = match.groups()
                total_file_size += int(file_size)

                # Update status code count if status code is recognized
                status_code = int(status_code)
                if status_code in stats:
                    stats[status_code] += 1

                    line_count += 1

        except (ValueError, ImportError):
            continue  # Skip lines with incorrect file size or status code FMT

        # Display stats after every 10 lines read
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise


# Print accumulated metrics after loop ends
print_stats()
