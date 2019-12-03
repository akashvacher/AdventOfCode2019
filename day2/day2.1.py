#!/usr/bin/env python


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
a[1], a[2] = 12, 2

print(compute(a))
