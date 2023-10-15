# 使用mplcyberpunk库绘制赛博朋克风图片

import mplcyberpunk
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)

plt.style.use('cyberpunk')
plt.figure()

plt.plot(x, y)
# mplcyberpunk.make_lines_glow()
# mplcyberpunk.add_glow_effects()
mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.5, gradient_start='zero')

plt.scatter(x, y2, c=y2, )
mplcyberpunk.make_scatter_glow()

plt.show()