#!/usr/bin/env python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)

#OR

# def simple_array_sum(n = input(), ar = [int(x) for x in input().strip().split()]):
#     return sum(ar)
#
# print(simple_array_sum())

#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
