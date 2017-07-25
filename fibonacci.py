#!/usr/bin/env python3
# coding: utf-8


def fib(n):
    # Figure out min-sub-problem. Then the whole problem.
    # time: O(n) space: O(n)
    dic = {}

    for k in range(1, n + 1):
        if k <= 2:
            dic[k] = 1
        else:
            dic[k] = dic[k - 1] + dic[k - 2]
    return dic[n]


def fib_2_space(n):
    # Figure out min-sub-problem. Then the whole problem.
    # time: O(n) space: O(1) i.e. 2
    dic = {1: 1, 2: 1}

    for k in range(1, n + 1):
        if k <= 2:
            dic[k] = 1
        else:
            ans = dic[1] + dic[2]
            dic[1] = dic[2]
            dic[2] = ans
    return dic[2]


def fib_recursive(n):
    # Figure out sub of sub of sub ...
    # n, n-1, n-2... height = n, spawn n times.
    # time: O(2**n) space: O(2**n) 1+2+4+8+...+2**n upper bound...
    if n <= 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

print('1: n n')
print(fib(36))
print('2: n 2')
print(fib_2_space(36))
print(
'''
3: log(n): math:
|F(n+1), F(n)|   --  |1, 1|^n
|F(n), F(n-1)|   --  |1, 0|
'''
)
print('4: 2**n 2**n')
print(fib_recursive(36))
