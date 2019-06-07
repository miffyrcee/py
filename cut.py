#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
"""

"""
import functools

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut(p, n):
    r = [0] * 10
    for i in range(1, 11):
        q = 0
        for j in range(1, i + 1):
            q = max(q, p[j - 1] + r[i - j - 1])
        r[i - 1] = q

    return int(n / 10) * r[9] + r[(n % 10) - 1]


def cut2(p, n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut2(p, n - i))
    return q

print(cut(p, 11))
