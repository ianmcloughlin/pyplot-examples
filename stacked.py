#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as pl

x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)

y1 = np.sin(x)**2
y2 = np.cos(x)**2

y0 = np.zeros(x.size)

pl.subplot(3, 1, 1)
pl.fill_between(x, y0, y1, facecolor=(1.0, 0.0, 0.0, 0.5))

pl.subplot(3, 1, 2)
pl.fill_between(x, y0, y2, facecolor=(0.0, 0.0, 1.0, 0.5))

pl.subplot(3, 1, 3)
pl.fill_between(x, y0, y1, facecolor=(1.0, 0.0, 0.0, 0.5))
pl.fill_between(x, y1, y1 + y2, facecolor=(0.0, 0.0, 1.0, 0.5))

pl.show()
