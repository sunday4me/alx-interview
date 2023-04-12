#!/usr/bin/python3
import sys

codes_count = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        data = line.split()
        if len(data) >= 7:
            if data[-2] in codes_count:
                codes_count[data[-2]] += 1
            file_size += int(data[-1])
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for key, value in sorted(codes_count.items()):
                if value > 0:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass

print("File size: {}".format(file_size))
for key, value in sorted(codes_count.items()):
    if value > 0:
        print("{}: {}".format(key, value))
