#! /usr/bin/env Python

# This Python script creates an animation where a sine wave is drawn (appears
# from left to right.)


# Import the necessary libraries.
import matplotlib.pyplot as pl
import numpy as np
import matplotlib.animation as an

# Create a figure and a set of axes to draw on.
fig = pl.figure()
ax = fig.gca()

# Get all of the x-values and the y-values that we need.
full_x = np.linspace(0, 2.0 * np.pi, 1000)
full_y = np.sin(full_x)

# Set x and y to be empty at first.
x = full_x[:0]
y = full_y[:0]

# Plot x and y to start.
line, = ax.plot(x, y)

# Set the limits of the axes so that we can see the full sine wave.
pl.xlim(0, 2.0 * np.pi)
pl.ylim(-1.0, 1.0)

# Te update function is called repeatedly with successive values for i.
def update(i):
    # Add a few more values to x and y.
    no_vals = 10 * (i + 1)
    x = full_x[:no_vals]
    y = full_y[:no_vals]
    # Change the line to plot the new x and y.
    line.set_xdata(x)
    line.set_ydata(y)

# Do the animation.
ani = an.FuncAnimation(fig, update, 100, interval=10)

# ani.save('sine.mp4')
pl.show()