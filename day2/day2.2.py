#!/usr/bin/env python
import sys


def compute(a):
    '''
    Accept an intcode program as a list of integers
    and return the final output of running the program
    '''
    it = iter(a)
    while True:
        op = next(it)

        # Invalid opcode check
        if op not in (1, 2, 99):
            raise ValueError

        # Halt opcode
        if op == 99:
            break

        x, y, z = next(it), next(it), next(it)
        if op == 1:
            a[z] = a[x] + a[y]
        else:
            a[z] = a[x] * a[y]

    return a[0]


def load_input():
    return list(map(int, open('in.txt').read().split(',')))


a = load_input()
done = False
for noun in range(100):
    for verb in range(100):
        # print(f"Checking {noun} {verb}")
        a[1], a[2] = noun, verb
        try:
            # Need to pass a copy of list otherwise
            # the original list will get mutated
            if compute(a[:]) == 19690720:
                print(100 * noun + verb)
                sys.exit(0)
        except Exception:
            pass
