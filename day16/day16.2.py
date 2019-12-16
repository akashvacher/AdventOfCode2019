#!/usr/bin/env python
from itertools import cycle


def fast_run_phase(a):
    sum_so_far, aggregate = 0, []
    for i in a[::-1]:
        sum_so_far = (sum_so_far + i) % 10
        aggregate.append(sum_so_far)
    return aggregate[::-1]


a = list(map(int, list(open('in.txt').read().strip())))
a = a * 10000
offset = int(''.join(map(str, a[:7])))

# We can use a faster run_phase function here since
# the index 'offset' is more than half the length of
# original array
assert offset > len(a) // 2

# We will only focus on generating the new arrays 'offset' index onwards
# since we don't care about the items before that index
a = a[offset:]

for phase in range(100):
    a = fast_run_phase(a)

print(''.join(map(str, a[:8])))
