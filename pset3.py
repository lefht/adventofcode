#!/usr/bin/python3

import re
import fileinput

def calculate_mul_from_input():
    result = 0
    outer_pattern = r'mul\(\d+\s*,\s*\d+\)'  # Correct regex for "mul(x, y)"
    inner_pattern = r'\d+\s*,\s*\d+'         # Correct regex for "x, y"

    for line in fileinput.input():
        matches_outer = re.findall(outer_pattern, line)
        for match in matches_outer:
            # Extract numbers inside the parentheses
            numbers = re.findall(inner_pattern, match)
            if numbers:
                num1, num2 = map(int, numbers[0].split(','))
                result += num1 * num2  # Add the product to the result

    return result


if __name__ == '__main__':
    scan = calculate_mul_from_input()
    print(scan)
