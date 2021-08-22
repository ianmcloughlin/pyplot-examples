#! /usr/bin/env python

# This script plots a 2D sine wave on 3D axes.

# We need to import this to use 3D axes.
from mpl_toolkits.mplot3d import Axes3D

# For creating arrays.
import numpy as np
# For plotting.
import matplotlib.pyplot as pl

# Set up our figure and our axes.
fig = pl.figure()
axes = fig.gca(projection='3d')

# Create our x, y and z coordinates.
x = np.arange(-4.0 * np.pi, 4.0 * np.pi, 0.1)
y = np.sin(x)
z = np.zeros(x.size)

# Create and show the plot.
axes.plot(x, y, z)
pl.show()

