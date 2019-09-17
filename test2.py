import collections
from random import choice

import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots()

r = 20

points = list()
c = list()
for i in range(-7, 8):
    y_min = -abs(abs(i) - 7) * np.cos(np.pi / 6)
    y_max = abs(abs(i) - 7) * np.cos(np.pi / 6)
    for j in np.linspace(y_min, y_max, abs(abs(i) - 7) + 1):
        points.append(i)
        points.append(j)

axs.plot(points[::2], points[1::2])

plt.show()
