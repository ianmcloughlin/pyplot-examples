#! /usr/bin/env python

# This script shows how to create a basic filled-in plot in PyPlot.
import numpy as np
import matplotlib.pyplot as pl

x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 1000)
y = np.sin(x)

y0 = np.zeros(x.size)

pl.plot(x, y, "k-")
pl.fill_between(x, y0, y, facecolor=(1.0, 0.0, 0.0, 0.5))

pl.show()
