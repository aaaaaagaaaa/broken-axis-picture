# import brokenaxes to realize a broken axis
from brokenaxes import brokenaxes
import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from qbstyles import mpl_style
import matplotx

x = np.linspace(0, 1, 100)
y = np.sin(10*x)

with plt.style.context(matplotx.styles.dracula):
    # mpl_style(dark=False)
    # plt.style.use('cyberpunk')
    fig = plt.figure()
    bax = brokenaxes(xlims=((0, 0.4), (0.6, 1)), hspace=0.05)
    bax.plot(x, y)
    # mplcyberpunk.make_lines_glow()
    bax.legend(loc=3)

    plt.show()
