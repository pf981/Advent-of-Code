from aocd import get_data, submit
import re

inp = get_data(day=19, year=2024)
patterns, _, *designs = inp.splitlines()
patterns = patterns.split(', ')

regex = re.compile('^(' + '|'.join(pattern for pattern in patterns) + ')+$')

answer1 = 0
for design in designs:
    if regex.match(design):
        answer1 += 1
print(answer1)

submit(answer1, part='a', day=19, year=2024)


# Part 2


import functools


@functools.cache
def count_ways(design):
    if not design:
        return 1
    ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            ways += count_ways(design[len(pattern):])
    return ways


answer2 = 0
for design in designs:
    if regex.match(design):
        answer2 += count_ways(design)
print(answer2)

submit(answer2, part='b', day=19, year=2024)
