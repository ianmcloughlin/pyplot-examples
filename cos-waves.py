#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as pl

x = np.arange(-4.0 * np.pi, 4.0 * np.pi, 0.1)

y1 = np.cos(x)
y2 = np.cos(3.0 * x)
y3 = np.cos((3.0 * x) + 5.0)
y4 = y1 + y2 + y3



pl.plot(x, y1, "b.", x, y2, "r.",x, y3, "g.", x, y4, "k-")


pl.show()