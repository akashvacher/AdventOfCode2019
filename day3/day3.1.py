#!/usr/bin/env python


def trace(s):
    '''
    Accept a path string, and return a set of
    points which fall on said path
    '''
    trail, x, y = set(), 0, 0
    s = s.split(',')
    for i in s:
        d = i[0]
        n = int(i[1:])
        if d == 'U':
            while n > 0:
                y += 1
                n -= 1
                trail.add((x, y))
        if d == 'D':
            while n > 0:
                y -= 1
                n -= 1
                trail.add((x, y))
        if d == 'R':
            while n > 0:
                x += 1
                n -= 1
                trail.add((x, y))
        if d == 'L':
            while n > 0:
                x -= 1
                n -= 1
                trail.add((x, y))
    return trail


p1, p2 = open('in.txt').readlines()

# Find all common points in these 2 trails
x = trace(p1) & trace(p2)

ans = min(abs(i) + abs(j) for i, j in x)
print(ans)
