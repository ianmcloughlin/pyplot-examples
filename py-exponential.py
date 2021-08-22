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

# Create a plot of the values.
mp.plot(x, y, "r", x, y, "b.")

# Add an x label.
mp.xlabel("x")

# Add a y label.
mp.ylabel("exp(x)")

# Add a grid.
mp.grid(True)

# Show the plot.
mp.show()