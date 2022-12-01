#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
with open(filename) as f:
    data = f.read().splitlines()

def create_data_structure(data) -> dict:
    """
       creates the data structure
    """
    res = {}
    count = 0
    for line in data:
        if count not in res:
            res[count] = {}
            res[count]['sum'] = 0
            res[count]['data'] = []
        if not line:
            count += 1
        else:
            line = int(line)
            res[count]['data'].append(line)
            res[count]['sum'] += line
    return res

def solve1(data) -> None:
    """
       solution1
    """

    res = create_data_structure(data)
    max = 0
    for count in res:
        if res[count]['sum'] > max:
            max = res[count]['sum']
    print(f"Solution1: {max}")

def solve2(data) -> None:
    """
      solution2
    """

    res = create_data_structure(data)
    sums = []
    for count in res:
        sums.append(res[count]['sum'])

    print(f"Solution2: {sum(sorted(sums)[-3:])}")

solve1(data)
solve2(data)
