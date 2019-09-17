import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

t = np.arange(np.pi / 3, np.pi * 2 / 3, step=np.pi / 6)
x = np.ma.cos(t)

y = np.ma.sin(t)
ax.plot(x, y)
ax.show()
