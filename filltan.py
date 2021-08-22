#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as pl

x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)

y1 = np.tan(x)
y2 = np.tan(2.0 * x)

y0 = np.zeros(x.size)

pl.plot(x, y1, "k-")
pl.plot(x, y2, "k-")
pl.fill_between(x, y0, y1, facecolor=(1.0, 0.0, 0.0, 0.5))
pl.fill_between(x, y0, y2, facecolor=(0.0, 0.0, 1.0, 0.5))

pl.show()
