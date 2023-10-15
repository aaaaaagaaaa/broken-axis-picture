# 实用qbstyles库进行绘图美化
from qbstyles import mpl_style
import numpy as np
import matplotlib.pyplot as plt

mpl_style(dark=False)

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.scatter(x, y, c=y)
plt.plot(x, y, c='g')
plt.colorbar(label='Y')
plt.show()

