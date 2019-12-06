#!/usr/bin/env python
from collections import defaultdict

# Dictionary mapping a moon/planet to the parent planet it is orbiting around
parent = dict()


def get_lineage(planet):
    '''
    Given a planet, returns a list of all planet parents in order
    '''
    while planet in parent:
        yield planet
        planet = parent[planet]


def load_input():
    global not_root
    with open("in.txt") as f:
        for line in f:
            x, y = line.strip().split(')')
            parent[y] = x


load_input()

l1 = list(get_lineage("SAN"))
l2 = list(get_lineage("YOU"))

# Remove all common ancestors
while l1[-1] == l2[-1]:
    l1.pop()
    l2.pop()

print(len(l1) + len(l2) - 2)
