#!/usr/bin/env python
from collections import defaultdict

# Dictionary mapping a planet to all the moons/parents orbiting around
child = defaultdict(list)
cache = {}


def total_orbits():
    '''
    Return total number of orbits in given system
    '''
    total = 0
    for i in child:
        total += total_satellites(i)
    return total


def total_satellites(planet):
    '''
    Given a planet, return the number of planets/moons
    orbiting around it
    '''
    if planet in cache:
        return cache[planet]

    # This planet has no planet orbiting it
    if planet not in child:
        cache[planet] = 0
        return cache[planet]

    total = 0
    for i in child[planet]:
        total += 1 + total_satellites(i)
    cache[planet] = total
    return cache[planet]


def load_input():
    global not_root
    with open("in.txt") as f:
        for line in f:
            x, y = line.strip().split(')')
            child[x].append(y)


load_input()
print(total_orbits())
