#!/usr/bin/env python


def trace(s):
    '''
    Accept a path string, and return a dict of
    points which fall on said path, and the shortest
    distance from origin to reach per point on the trail
    '''

    trail, x, y = dict(), 0, 0
    length = 0
    s = s.split(',')
    for i in s:
        d = i[0]
        n = int(i[1:])
        if d == 'U':
            while n > 0:
                length += 1
                y += 1
                n -= 1
                trail[(x, y)] = trail.get((x, y), length)
        if d == 'D':
            while n > 0:
                length += 1
                y -= 1
                n -= 1
                trail[(x, y)] = trail.get((x, y), length)
        if d == 'R':
            while n > 0:
                length += 1
                x += 1
                n -= 1
                trail[(x, y)] = trail.get((x, y), length)
        if d == 'L':
            while n > 0:
                length += 1
                x -= 1
                n -= 1
                trail[(x, y)] = trail.get((x, y), length)
    return trail


p1, p2 = open('in.txt').readlines()
t1, t2 = trace(p1), trace(p2)

# Find all common points in these 2 trails
x = t1.keys() & t2.keys()

ans = min(t1[p] + t2[p] for p in x)
print(ans)
