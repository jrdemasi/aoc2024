#!/usr/bin/env python3

import re

def parse_input():
    inputs = []
    with open("input", 'r') as f:
        for line in f:
            inputs.append(line.strip())
    return inputs

def main():
    inputs = parse_input()
    sum = 0 
    # part 1
    for line in inputs:
        results = re.findall(r"mul\(([0-9]*,[0-9]*)\)", line)
        for result in results:
            pairs = list(map(int, result.split(',')))
            sum = sum + (pairs[0] * pairs[1])
    print(sum)

    # part 2 
    sum = 0 
    do = True
    for line in inputs:
        results = re.split(r'(do\(\)|don\'t\(\))', line)
        for result in results:
            if result == "don't()":
                do = False
            elif result == "do()":
                do = True
            else:
                find_mul = re.findall(r"mul\(([0-9]*,[0-9]*)\)", result)
                for mul in find_mul:
                    if do:
                        pairs = list(map(int, mul.split(',')))
                        sum = sum + (pairs[0] * pairs[1])
    print(sum)

if __name__ == "__main__":
    main()
