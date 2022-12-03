#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
with open(filename) as f:
    data = f.read().splitlines()

def solve1(data) -> None:
    """
       solution1
       8039
    """
    score = '.abcdefghijklmnopqrstuvwxyz'
    score += score[1:].upper()

    result = 0
    for line in data:
        half = int(len(line) / 2)
        list1 = line[:half]
        list2 = line[half:]
        common = list(set.intersection(*map(set, [list1, list2] )))[0]
        result += score.index(common)
    print(f"Solution1: {result}")


def solve2(data) -> None:
    """
       solution2
       2510
    """
    score = '.abcdefghijklmnopqrstuvwxyz'
    score += score[1:].upper()
    result = 0
    count = 0
    while count < len(data):
        common = list(set.intersection(*map(set, data[count:count+3])))[0]
        result += score.index(common)
        count += 3
    print(f"Solution2: {result}")

solve1(data)
solve2(data)
