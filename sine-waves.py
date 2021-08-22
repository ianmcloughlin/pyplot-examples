#! /usr/bin/env python

import matplotlib.pyplot as pl
import numpy as np

x = np.arange(-8 * np.pi, 8 * np.pi, 0.01)
y = np.sin(x)

pl.plot(x, y, "b-")
pl.show()
