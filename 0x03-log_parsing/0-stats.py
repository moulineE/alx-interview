#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import re


if __name__ == '__main__':
    codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    total_size = 0
    pattern = (r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} -'
               r' \[.*] "GET /projects/260 HTTP/1.1" (.*) \d{1,}')
    count = 0

    def print_logs_stats(codes: dict, total_size: int) -> None:
        """print the logs stats
        Args:
            codes (dict): the status codes and frequency
            total_size (int): the total size of the logs
        """
        print("File size: {:d}".format(total_size))
        for code in codes:
            if codes[code] != 0:
                print("{:d}: {:d}".format(code, codes[code]))

    try:
        for line in sys.stdin:
            if re.match(pattern, line):
                count += 1
                data = line.split()
                try:
                    code = int(data[-2])
                    if code in codes:
                        codes[code] += 1
                except Exception:
                    pass
                total_size += int(data[-1])

            if count % 10 == 0 and count != 0:
                print_logs_stats(codes, total_size)
        print_logs_stats(codes, total_size)
    except KeyboardInterrupt:
        print_logs_stats(codes, total_size)
        raise
