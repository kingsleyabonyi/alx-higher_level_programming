#!/usr/bin/python3
"""
Implements the function print_status
"""
import sys


def print_status():
    """
        Printing the status of the request
    """
    counter = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for l in sys.stdin:
            line = l.split()
            if len(line) >= 2:
                c = counter
                if line[-2] in status_codes:
                    status_codes[line[-2]] += 1
                    counter += 1
                try:
                    file_size += int(line[-1])
                    if c == counter:
                        counter += 1
                except:
                    if c == counter:
                        continue
            if counter % 10 == 0:
                print("File size: {}".format(file_size))
                for key, val in sorted(status_codes.items()):
                    if val:
                        print("{}: {}".format(key, val))
        print("File size: {}".format(file_size))
        for key, val in sorted(status_codes.items()):
            if val:
                print("{}: {}".format(key, val))

    except KeyboardInterrupt:
        print("File size: {}".format(file_size))
        for key, val in sorted(status_codes.items()):
            if val:
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    print_status()
