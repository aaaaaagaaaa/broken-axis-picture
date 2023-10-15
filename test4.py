# 使用axs进行绘制多个子图

import mplcyberpunk
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10 ,100)
y = np.sin(x)

plt.style.use('cyberpunk')
fig,axs = plt.subplots(2, 2, sharex=True, sharey=False)

for i in range(2):
    for j in range(2):
        axs[i][j].plot(x, y, linestyle=':')

mplcyberpunk.make_lines_glow()
plt.show()