#!/usr/bin/python3

import re
import fileinput

def calculate_enabled_mul_sum():
    outer_pattern = r"(don't\(\)|do\(\)|mul\(\d+\s*,\s*\d+\))"
    inner_pattern = r"\d+\s*,\s*\d+"
    
    result = 0
    enabled = True  

    for line in fileinput.input():
    
        instructions = re.findall(outer_pattern, line)
        
        for instruction in instructions:
            if instruction == "don't()":
                enabled = False
            elif instruction == "do()":
                enabled = True
            elif instruction.startswith("mul") and enabled:
                numbers = re.findall(inner_pattern, instruction)
                if numbers:
                    num1, num2 = map(int, numbers[0].split(','))
                    result += num1 * num2

    return result


if __name__ == "__main__":
    scan = calculate_enabled_mul_sum()
    print(scan)
