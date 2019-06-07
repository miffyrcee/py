#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
"""

"""
import numpy as np

X = list('ABCBDAB')
Y = list('BDCABA')


def lcs(x, y):
    m = len(x) + 1
    n = len(y) + 1
    b = np.zeros((m, n))
    c = np.zeros((m, n))
    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c

print(lcs(X, Y))
