import copy
from collections import defaultdict
from random import choices
from string import *

import numpy as np

n = 6
c = np.array(choices(digits, k=n * n)).astype(int).reshape((n, n))
for i in range(n):
    for j in range(n):
        if i >= j:
            c[i][j] = c[j][i]

f = np.zeros((n, n))
h = [0] * n
h[0] = n

e = [0] * n

N = defaultdict(list)
for i in range(n):
    for j in range(n):
        if c[i][j]:
            N[i].append(j)


def init_pre_flow():
    e[0] = e[0] - sum(c[0])
    for i in range(1, n):
        f[0][i] = c[0][i]
        f[i][0] = 0
        e[i] = f[0][i]


def push(u, v):
    # flow from u to v
    # e[u] exceed
    delta = min(c[u][v] - f[u][v], e[u])
    f[u][v] += delta
    f[v][u] -= delta
    e[u] -= delta
    e[v] += delta


def discharge(u):
    while e[u]:
        sum_to = sum(map(lambda x: f[x][u], N[u]))
        if sum_to > e[u]:
            pass
        else:
            pass


init_pre_flow()
print(e)
print(f)
