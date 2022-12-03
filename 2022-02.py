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
        res.append((line.split(" ")))
    return res

def solve1(data) -> None:
    """
       solution1
    """

    res = create_data_structure(data)
    score = 0
    for game in res:
       if game[1] == 'Y':
           game[1] = 'B'
       if game[1] == 'X':
           game[1] = 'A'
       if game[1] == 'Z':
           game[1] = 'C'


       if game[0] == 'A' and game[1] == 'A':
           score += 3
           score += 1
       if game[0] == 'A' and game[1] == 'B':
           score += 6
           score += 2
       if game[0] == 'A' and game[1] == 'C':
           score += 0
           score += 3

       if game[0] == 'B' and game[1] == 'A':
           score += 0
           score += 1
       if game[0] == 'B' and game[1] == 'B':
           score += 3
           score += 2
       if game[0] == 'B' and game[1] == 'C':
           score += 6
           score += 3

       if game[0] == 'C' and game[1] == 'A':
           score += 6
           score += 1
       if game[0] == 'C' and game[1] == 'B':
           score += 0
           score += 2
       if game[0] == 'C' and game[1] == 'C':
           score += 3
           score += 3

    print(f"Solution1: {score}")

def get_score(game) -> int:
    """
       X-> loose 0
       Y -> draw 1
       Z -> win 6
       score:
       A -> 1
       B -> 2
       C -> 3
    """

    if game[0] == 'A':
       if game[1] == 'Y':
        return 1
       if game[1] == 'X':
           return 3
       if game[1] == 'Z':
           return 2

    if game[0] == 'B':
        if game[1] == 'Y':
            return 2
        if game[1] == 'X':
            return 1
        if game[1] == 'Z':
            return 3

    if game[0] == 'C':
        if game[1] == 'Y':
            return 3
        if game[1] == 'X':
            return 2
        if game[1] == 'Z':
            return 1

def solve2(data) -> None:
    """
       solution2
    """
    res = create_data_structure(data)
    score = 0

    for game in res:
       if game[0] == 'A' and game[1] == 'X':
           score += 0
           score += get_score(game)
       if game[0] == 'A' and game[1] == 'Y':
           score += 3
           score += get_score(game)
       if game[0] == 'A' and game[1] == 'Z':
           score += 6
           score += get_score(game)

       if game[0] == 'B' and game[1] == 'X':
           score += 0
           score += get_score(game)
       if game[0] == 'B' and game[1] == 'Y':
           score += 3
           score += get_score(game)
       if game[0] == 'B' and game[1] == 'Z':
           score += 6
           score += get_score(game)

       if game[0] == 'C' and game[1] == 'X':
           score += 0
           score += get_score(game)
       if game[0] == 'C' and game[1] == 'Y':
           score += 3
           score += get_score(game)
       if game[0] == 'C' and game[1] == 'Z':
           score += 6
           score += get_score(game)
    print(f"Solution2: {score}")

solve1(data)
solve2(data)
