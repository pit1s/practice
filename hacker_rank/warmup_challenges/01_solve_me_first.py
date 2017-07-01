#!/usr/bin/env python3

def solveMeFirst(a,b):
    return a + b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1, num2)
print(res)

# OR

# def solve_me_first(a = input(), b = input()):
#     try:
#         return int(a) + int(b)
#     except ValueError:
#         return "Expecting an integer"
#
# print(solve_me_first())

#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
