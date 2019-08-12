import math
from collections import namedtuple

import matplotlib.pyplot as plt
import networkx as nx

GE = nx.DiGraph()
e = [
    ('s', 'u', 32),
    ('s', 'v', 45),
    ('u', 'v', 1),
    ('v', 't', 21),
    ('u', 't', 24),
]
GE.add_edge('s', 'v1', capacity=16)
GE.add_edge('s', 'v2', capacity=13)
GE.add_edge('v1', 'v3', capacity=12)
GE.add_edge('v2', 'v1', capacity=4)
GE.add_edge('v2', 'v4', capacity=14)
GE.add_edge('v3', 'v2', capacity=9)
GE.add_edge('v3', 't', capacity=20)
GE.add_edge('v4', 'v3', capacity=7)
GE.add_edge('v4', 't', capacity=4)
print(nx.maximum_flow(GE, 's', 't'))
print(nx.minimum_cut(GE, 's', 't'))
