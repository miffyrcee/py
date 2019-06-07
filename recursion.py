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

na = np.array(((0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 1, 0, 0, 0),
               (0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 1, 1, 1, 1, 1, 0),
               (0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 1, 1, 1),
               (0, 0, 1, 0, 0, 1, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0)))

f = [(i, j) for i, j in zip(np.where(na == 1)[0], np.where(na == 1)[1])]

r = []


def road(rel=0, im=0):
    if rel == im == 7:
        print(r)
        return 0
    elif rel == 7:
        r.append((rel, im))
        if f.count((rel, im + 1)):
            return 0
        else:
            road(rel, im + 1)
    elif im == 7:
        r.append((rel, im))
        if f.count((rel + 1, im)):
            return 0
        else:
            road(rel + 1, im)
    else:
        r.append((rel, im))
        if f.count((rel, im + 1)) and f.count((rel + 1, im)):
            road(rel, im - 1)

        elif f.count((rel + 1, im)):
            road(rel, im + 1)
        elif f.count((rel, im + 1)):
            road(rel + 1, im)
        else:
            #  road(rel, im + 1)
            road(rel + 1, im)

road()
