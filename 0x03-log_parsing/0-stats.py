#!/usr/bin/python3
"""Reads standard-in line by line and computes metrics"""

import re
import signal
import sys


total_size = 0
line_count = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

log_patterns = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>[^\]]+)\] '
    r'"(?P<request>[^"]+)" (?P<status_code>\d{3}) '
    r'(?P<file_size>\d+)'
)


def print_status(status_codes: dict, total_size: int) -> None:
    """Prints the status codes and total file size"""
    print("File size:", total_size)
    for code in status_codes.keys():
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles SIGINT signal"""
    print_status(status_codes, total_size)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_patterns.match(line)
        if match:
            file_size = int(match.group('file_size'))
            code = match.group('status_code')
            total_size += file_size
            if code in status_codes:
                status_codes[code] += 1

            line_count += 1
            if line_count == 10:
                print_status(status_codes, total_size)
                line_count = 0
except (KeyboardInterrupt, EOFError):
    print_status(status_codes, total_size)
    sys.exit(0)

print_status(status_codes, total_size)
