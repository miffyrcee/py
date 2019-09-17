import time

import matplotlib.pyplot as plt
import numpy as np

x = list()
y = list()
for i in range(-7, 8):
    for j in range(-7, 8):
        if abs(i) + abs(j) <= 7:
            x.append(i)
            y.append(j)

fig, ax = plt.subplots()
ax.plot(x, y, '--o')
plt.pause(1)
time.sleep(2)
ax.plot(-3, 2, '--o')
plt.pause(1)
plt.show()
