from collections import namedtuple

import numpy as np

w = np.array((
    [0, 2, 1, 1],
    [2, 0, 0, 4],
    [1, 0, 0, 5],
    [1, 4, 5, 0],
))


class g_node():
    def __init__(self, d=np.inf, pi=None):
        self.d = d
        self.pi = pi


d = [-np.inf] * len(w)
d[0] = 0
for i in range(len(w)):
    for j, k in zip(w[i], range(4)):
        if j and d[k] < d[i] + j:
            d[k] = d[i] + j

print(d)
for j, k in zip(w[0], range(4)):
    if j and d[0] < d[k] + j:
        d[0] = d[k] + j
print(d)
