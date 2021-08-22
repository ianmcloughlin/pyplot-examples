#! /usr/bin/env python

# This script shows you how to plot the exponential function for certain values
# of x. The exponential function is f(x) = e^x, or the number e to the power
# of x. e is a number like pi in mathematics, and has a value of approximately 
# 2.718. So f(2) = exp(2) = e^2 = e * e = (approx) 2.718 * 2.718 = (approx) 7.4.

# We need numpy for the arange and exp functions.
import numpy as np
# We need pyplot for plotting.
import matplotlib.pyplot as mp

# Create our x values.
x = np.arange(0., 10., 0.1)

# Create our y values.
y = np.exp(x)

# Keep the previous plots made on the same axes.
mp.hold(True)

# Create a plot of the values, twice.
# The first as a red line, the second as blue dots.
mp.plot(x, y, "r-", label="exp(x)")
mp.plot(x, y, "b.", label="Also exp(x)")

# Add an x label.
mp.xlabel("x")

# Add a y label.
mp.ylabel("exp(x)")

# Add a grid.
mp.grid(True)

# Add a legend.
mp.legend()

# Show the plot.
mp.show()