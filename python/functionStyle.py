#!/usr/bin/env python
# -*- coding: utf-8 -*-


def add(x, y):
    return x + y


def reduce_(function, lst, initial=0):
    result = initial
    for item in lst:
        result = function(result, item)
    return result


def map_(function, lst):
    return [function(item) for item in lst]


def add_to_(n):
    return lambda x: add(n, x)


multiply = lambda x, y: x * y
find_max = lambda x, y: x if x > y else y


if __name__ == '__main__':
    print add('三角形的树', '北极')

    L = [9, 3, 10, 4, 2, 6]
    print reduce_(multiply, L, initial=1)
    print reduce_(find_max, L)
    print map_(add_to_(10), L)
