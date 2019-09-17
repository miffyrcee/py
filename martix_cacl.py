import os

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

t = np.arange(0, np.pi * 2 + 0.01, step=np.pi / 3)
x = np.cos(t)
y = np.sin(t)

ax.plot(x, y, '-o')
plt.show()
