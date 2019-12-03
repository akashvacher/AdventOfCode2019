#!/usr/bin/env python

total_fuel = 0
with open("in.txt") as f:
    for line in f:
        x = int(line)
        total_fuel += (x//3) - 2
print(total_fuel)
