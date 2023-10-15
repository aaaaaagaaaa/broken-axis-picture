# 添加横轴截断效果

from qbstyles import mpl_style
import mplcyberpunk
import numpy as np
import matplotlib.pyplot as plt

x = np.r_[0:1:0.1, 9:10:0.1]
y = np.sin(x)

# mpl_style(dark=True)
# plt.style.use('cyberpunk')
fig,(ax1, ax2) = plt.subplots(1, 2, sharey=True)

ax1.plot(x, y, 'bo')
ax2.plot(x, y, 'bo')
# mplcyberpunk.make_lines_glow()

ax1.set_xlim(0, 1)
ax2.set_xlim(9, 10)

#隐藏边界线
ax1.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax1.yaxis.tick_left()
ax1.tick_params(labeltop='off')
ax2.yaxis.tick_right()

plt.subplots_adjust(wspace=0.15)#让两个图像更靠近

d = .015 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
ax1.plot((1-d,1+d),(-d,+d), **kwargs) # top-left diagonal
ax1.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-left diagonal

kwargs.update(transform=ax2.transAxes) # switch to the bottom axes
ax2.plot((-d,d),(-d,+d), **kwargs) # top-right diagonal
ax2.plot((-d,d),(1-d,1+d), **kwargs) # bottom-right diagonal

plt.show()
