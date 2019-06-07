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

p = [5, 10, 3, 12, 5, 50, 6]


def mo(p):
    n = len(p) - 1
    m = np.ones((n, n)) * float('inf')
    for i in range(n):
        j = i
        m[i][j] = 0

    for l in range(1, n):
        for i in range(l):
            j = l - i
            for k in range(i, j + 1):
                m[i][j] = min(m[i][j],
                              m[i][k] + m[k + 1][j] + p[i] * p[k] * p[j])
    return m


print('asdsf' [1:2])
print(mo(p))
