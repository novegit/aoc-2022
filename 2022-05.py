#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
with open(filename) as f:
    data = f.read().splitlines()

def create_data_structure(data) -> dict:
    """
       creates the data structure
    """
    stack = {}
    stack[1] = ["H", "T", "Z", "D"]
    stack[2] = ["Q", "R", "W", "T", "G", "C", "S"]
    stack[3] = ["P", "B", "F", "Q", "N", "R", "C", "H"]
    stack[4] = ["L", "C", "N", "F", "H", "Z"]
    stack[5] = ["G", "L", "F", "Q", "S"]
    stack[6] = ["V", "P", "W", "Z", "B", "R", "C", "S"]
    stack[7] = ["Z", "F", "J"]
    stack[8] = ["D", "L", "V", "Z", "R", "H", "Q"]
    stack[9] = ["B", "H", "G", "N", "F", "Z", "L", "D"]

    instructions = []
    for line in data:
        if line.startswith("move"):
            line = line.replace("move ", "")
            line = line.replace("from ", "")
            line = line.replace("to ", "")

            mod = map(int, line.split(' '))
            instructions.append((next(mod), next(mod), next(mod)))
    return (stack, instructions)


def solve1(data) -> None:
    """
       solution1
    """

    stack, instructions = create_data_structure(data)

    for i in instructions:
        count = i[0]
        while count > 0:
            stack[i[2]].append(stack[i[1]].pop())
            count -= 1

    res = ""
    for i in range (1,10):
        try:
            res = res + stack[i][-1]
        except:
            continue

    print(f"Solution1: {res}")


def solve2(data) -> None:
    """
       solution2
    """

    stack, instructions = create_data_structure(data)

    for i in instructions:
        count = i[0]
        tmp = stack[i[1]][-count:]
        stack[i[1]] = stack[i[1]][:-count]
        stack[i[2]].extend(tmp)

    res = ""
    for i in range (1,10):
        try:
            res = res + stack[i][-1]
        except:
            continue

    print(f"Solution2: {res}")


d = (create_data_structure(data))
solve1(data)
solve2(data)
