#!/usr/bin/python3
"""This module parse log data passed through stdin and prints stats"""
import sys


def print_stats(size, codes, codes_count):
    """Prints stats"""
    sys.stdout.write("File size: {:d}\n".format(size))
    for code in codes:
        code_count = codes_count[code]
        if code_count > 0:
            sys.stdout.write("{:d}: {:d}\n".format(code, code_count))
    sys.stdout.flush()
    pass


def main():
    """Main function"""
    size = 0
    count = 0
    codes = [200, 301, 400, 401, 403, 404, 405, 500]
    codes_count = {code: 0 for code in codes}
    try:
        for line in sys.stdin:
            info = line.strip().split(" ")
            if type(info) is list and len(info) > 1:
                try:
                    size += int(info[-1])
                    code = int(info[-2])
                    if code in codes_count:
                        codes_count[code] += 1
                    count += 1
                except Exception:
                    pass
            if count % 10 == 0:
                print_stats(size, codes, codes_count)
    except KeyboardInterrupt:
        print_stats(size, codes, codes_count)
        raise
    print_stats(size, codes, codes_count)
    pass


if __name__ == "__main__":
    main()
