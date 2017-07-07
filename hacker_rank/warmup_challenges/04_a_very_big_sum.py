#!/usr/bin/env python3

import sys

def aVeryBigNum(n, ar):
    # Complete this function
    return sum(ar)  # Convert to long automatically

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

# OR

# Ignore first input and take sum of float array
# input()
# print(sum([float(x) for x in input().strip().split()]))

#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
