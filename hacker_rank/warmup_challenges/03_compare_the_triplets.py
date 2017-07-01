#!/usr/bin/env python3

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = [a0, a1, a2]
    b = [b0, b1, b2]
    for i in range(len(a)):
        if a[i] > b[i]:
            a[i] = 1
        elif a[i] < b[i]:
            a[i] = -1
        else:
            a[i] = 0
    return [sum(x > 0 for x in a), sum(x < 0 for x in a)]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))

# OR

# def solve(a, b):
#     return [len([x for x, y in zip(a, b) if x > y]),
#             len([x for x, y in zip(a, b) if x < y])]
#
#
#
# a = [int(x) for x in input().strip().split()]
# b = [int(y) for y in input().strip().split()]
# print(" ".join(map(str, solve(a, b))))


#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
