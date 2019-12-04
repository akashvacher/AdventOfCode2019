#!/usr/bin/env python


def fuel_correction(fuel):
    if fuel <= 0:
        return 0
    x = fuel
    correction = 0
    while ((x // 3) - 2) > 0:
        correction += ((x // 3) - 2)
        x = ((x // 3) - 2)
    return fuel + correction


total_fuel = 0
with open("in.txt") as f:
    for line in f:
        x = int(line)
        total_fuel += fuel_correction((x // 3) - 2)
print(total_fuel)
