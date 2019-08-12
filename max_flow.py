import math
import sys

import matplotlib as plt
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

n = 5
w = np.array((
    [0, 3, 8, np.inf, 4],
    [np.inf, 0, np.inf, 1, 7],
    [np.inf, 4, 0, np.inf, np.inf],
    [2, np.inf, 5, 0, np.inf],
    [np.inf, np.inf, np.inf, 6, 0],
))
f = np.ones((0, 0))

pi = np.ones((n, n)) * np.inf


class graph():
    def __init__(self, weight, pi=[None] * 5, d=[np.inf] * 5):
        self._w = weight
        self._pi = pi
        self._d = d
        self._d[0] = 0

    def dijkstra_path(self, u, v):
        d = self._d
        w = self._w
        pi = self._pi
        w[u], w[0] = w[0], w[u]

        for i in range(5):
            for j in range(5):
                if d[j] > d[i] + w[i][j]:
                    d[j] = d[i] + w[i][j]
                    pi[j] = i
        t = v
        q = list()
        while t is not None:
            q.append(t)
            t = pi[t]

        return q, d[v]

    def exist_p(self, u, v):
        w = self._w
        if w[u][v] > 0 and w[u][v] < 1000:
            return True
        else:
            for i in range(n):
                if w[u][i] > 0 and w[u][i] < 1000:
                    self.exist_p(i, v)
            return False


class max_flow():
    def __init__(self, C, Cf, f=np.zeros((5, 5))):
        self.C = self.C
        self.Cf = self.Cf
        self.f = self.f


GE = nx.DiGraph()
e = [
    ('s', 'u', 100),
    ('s', 'v', 100),
    ('u', 'v', 1),
    ('v', 't', 100),
    ('u', 't', 100),
]
GE.add_weighted_edges_from(e)
Gf = GE
for _ in range(40):
    if nx.has_path(Gf, 's', 't'):
        p = nx.dijkstra_path(Gf, 's', 't')
        p_pairs = [(i, j) for i, j in zip(p[:-1], p[1:])]
        p_weight = [Gf.edges.get(i)['weight'] for i in p_pairs]
        for i, j in zip(p_pairs, p_weight):
            Gf.add_edge(i[0], i[1], weight=j - min(p_weight))
            if Gf.edges.get(i)['weight'] == 0:
                Gf.remove_edge(i[0], i[1])
