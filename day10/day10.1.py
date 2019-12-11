#!/usr/bin/env python

from pprint import pprint


def gcd(a, b):
    if a == 0:
        return b
    if b % a == 0:
        return a
    return gcd(b % a, a)


def input_load():
    x = []
    with open('in.txt') as f:
        for line in f:
            x.append([1 if i == '#' else 0 for i in line.strip()])
    return x


x = input_load()
points = set()
rows = len(x)
columns = len(x[0])
for i in range(rows):
    for j in range(columns):
        if x[i][j]:
            points.add((i, j))

best_score, best_location = 0, None
for i, j in sorted(list(points)):
    d = set()
    for u, v in points:
        if (i, j) == (u, v):
            continue
        dy, dx = v - j, u - i
        g = gcd(abs(dy), abs(dx))
        d.add((dy / g, dx / g))
    if best_score < len(d):
        best_score = len(d)
        best_location = (j, i)
# print(best_score)
print(best_location)
