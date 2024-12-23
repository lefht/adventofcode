#!/usr/bin/python3

import fileinput

# Check if a report is safe (increasing)
def is_increasing_safe(report):
    return all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))

# Check if a report is safe (decreasing)
def is_decreasing_safe(report):
    return all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))

if __name__ == '__main__':
    safe_reports_count = 0
    for line in fileinput.input():
        report = list(map(int, line.split()))
        if is_increasing_safe(report) or is_decreasing_safe(report):
            safe_reports_count += 1
    print(safe_reports_count)
