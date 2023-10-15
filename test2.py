# 使用matplotx进行绘图美化
import matplotx
import matplotlib.pyplot as plt
import numpy as np

with plt.style.context(matplotx.styles.dracula):
    plt.figure()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.scatter(x, y, c=y)
    plt.colorbar(label='Y')
    plt.show()