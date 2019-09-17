from random import choice

import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

n = 7
point = list()
fig, ax = plt.subplots()

for i in range(-7, 8):
    for j in range(-7, 8):
        if abs(i) + abs(j) <= 7:
            point.append((i + 7, j + 7))
