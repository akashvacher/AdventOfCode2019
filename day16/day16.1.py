#!/usr/bin/env python
from itertools import cycle


def run_phase(a):
    out = []
    for out_index in range(1, len(a) + 1):
        pattern = cycle(i for i in [0, 1, 0, -1] for j in range(out_index))
        next(pattern)
        out_val = 0
        for i in a:
            out_val += i * next(pattern)
        out_val = abs(out_val) % 10
        out.append(out_val)
    return out


a = list(map(int, list(open('in.txt').read().strip())))

for phase in range(100):
    a = run_phase(a)

print(''.join(map(str, a[:8])))
