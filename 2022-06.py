#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
with open(filename) as f:
    data = f.read().splitlines()


def solve1(data) -> None:
    """
       solution1
    """

    res = 0
    for line in data:
        counter = 0
        tmp = []
        for c in line:
            tmp.append(c)
            mark = set(tmp)
            if len(mark) == 4:
                res += counter + 1
                break
            if len(tmp) == 4:
                tmp.pop(0)
            counter += 1

    print(f"Solution1: {res}")


def solve2(data) -> None:
    """
       solution2
    """

    res = 0
    for line in data:
        counter = 0
        tmp = []
        for c in line:
            tmp.append(c)
            mark = set(tmp)
            if len(mark) == 14:
                res += counter + 1
                break
            if len(tmp) == 14:
                tmp.pop(0)
            counter += 1

    print(f"Solution2: {res}")


solve1(data)
solve2(data)
