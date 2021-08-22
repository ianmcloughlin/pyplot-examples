from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as pl


fig = pl.figure()
axes = fig.gca(projection='3d')

x = np.arange(-4.0 * np.pi, 4.0 * np.pi, 0.1)
y = np.sin(x)
z = np.zeros(x.size)

pl.hold(True)

axes.plot(x, y, z)
axes.plot(x, z, y)

pl.show()

