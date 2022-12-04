#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
with open(filename) as f:
    data = f.read().splitlines()

def create_data_structure(data) -> dict:
    """
       creates the data structure
    """
    res = []
    count = 0
    for line in data:
        first, sec = line.split(",")
        first = first.split("-")
        sec = sec.split("-")
        first[0] = int(first[0])
        first[-1] = int(first[-1])
        sec[0] = int(sec[0])
        sec[-1] = int(sec[-1])

        l1 = []
        l2 = []
        for i in range(first[0], first[-1] + 1):
            l1.append(i)
        for i in range(sec[0], sec[-1] + 1):
            l2.append(i)

        res.append((l1, l2))
    return res

def solve1(data) -> None:
    """
       solution1
    """

    data = create_data_structure(data)
    score = 0
    for pair in data:
        if set(pair[0]).intersection(set(pair[1])) == set(pair[0]):
            score += 1
        elif set(pair[1]).intersection(set(pair[0])) == set(pair[1]):
            score += 1
    print(f"Solution1: {score}")


def solve2(data) -> None:
    """
       solution2
    """

    data = create_data_structure(data)
    score = 0
    for pair in data:
        if len(set(pair[0]) & set(pair[1])) > 0:
            score += 1

    print(f"Solution2: {score}")


solve1(data)
solve2(data)
