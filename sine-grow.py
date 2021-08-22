#! /usr/bin/env python

# This script creates a PyPlot animation of a sine wave.
# The sine wave grows in amplitude from 0 to 1.

# Import the necessary libraries.
import matplotlib.pyplot as pl
import numpy as np
import matplotlib.animation as an

# Create the figure and the axes.
fig = pl.figure()
ax = fig.gca()

# Plot some initial x and y values.
# This has the happy side effect of setting the y limits correctly.
x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
y = np.sin(x)

# Create the line.
line, = ax.plot(x, y)


# This function is called every frame, with i as the frame number (starts at 0.)
def update(i):
    s = i / 50.0
    line.set_ydata(s * np.sin(x))
        
ani = an.FuncAnimation(fig, update, 50, interval=10)

#ani.save('sine.mp4')
pl.show()