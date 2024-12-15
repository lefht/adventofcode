#!/usr/bin/python3

import fileinput

def calculate_absolute_difference_sum():
    column1 = []
    column2 = []

    for line in fileinput.input():
        line = line.strip().split()

        column1.append(int(line[0]))
        column2.append(int(line[1]))

    column1.sort()
    column2.sort()

    result = [abs(column1[i] - column2[i]) for i in range(len(column1))]
    return sum(result)

if __name__ == "__main__":
    result = calculate_absolute_difference_sum()
    print(result)