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
import itertools
import string

import numpy as np

p = [100, 60, 120]
w = [20, 10, 30]


def add(x):
    return 2 * x


def mul(x):
    return x * x


def selector(W, n):
    result = []
    for i in range(3):
        W = W - w[i]
        if W > 0:
            result.append(w[i])
        else:
            result.append(w[i] + W)
    print(result)
selector(50, 3)
