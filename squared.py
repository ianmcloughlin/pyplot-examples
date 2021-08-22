#! /usr/bin/env python

# This PyPlot example shows sine squared and cosine squared stacked on top of
# each other. It is a graphical representation of the fact that the sum of the
# the two values is always equal to one.

# The script also demonstrates how to place multiple plots in a single figure.

import numpy as np
import matplotlib.pyplot as pl

x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)

# Set y1 to sine squared, and y2 to cosine squared.
y1 = np.sin(x)**2
y2 = np.cos(x)**2

pl.subplot(3, 1, 1)
pl.fill_between(x, 0, y1, facecolor=(1.0, 0.0, 0.0, 0.5))

pl.subplot(3, 1, 2)
pl.fill_between(x, 0, y2, facecolor=(0.0, 0.0, 1.0, 0.5))

pl.subplot(3, 1, 3)
pl.fill_between(x, 0, y1, facecolor=(1.0, 0.0, 0.0, 0.5))
pl.fill_between(x, y1, y1 + y2, facecolor=(0.0, 0.0, 1.0, 0.5))

pl.show()
