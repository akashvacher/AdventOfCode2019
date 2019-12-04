#!/usr/bin/env python
from collections import Counter

MIN = 153517
MAX = 630395


def possibilities(s='', l=6):
    # Base case
    if l == 0:
        if MIN <= int(s) <= MAX and any(i == 2 for i in Counter(s).values()):

            return 1
        return 0

    last = 0 if len(s) == 0 else int(s[-1])
    ans = sum(possibilities(s+str(digit), l-1) for digit in range(last, 10))
    return ans


print(possibilities())
