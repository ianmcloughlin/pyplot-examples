#! /usr/bin/env python

# This script shows you how to plot a few different sine waves on one plot.
# We first plot sin(x) in blue, for values of x ranging from -4pi to 4pi,
# which is about -12 to 12 (since 4pi = 4 * 3.14 = 12 approx.).

# Then we plot sin(2x) in red. Sin(2x) just means, before calculating the sin
# value, multiply x by 2. In the plot you can see this means that the red line
# has twice the "frequency" of the blue, or in other words it goes up and down
# at twice the rate of the the blue line.

# In green then we plot sin(x + 4), which just means add the number 4 to x
# before calculating the sin value. This has the effect of shifting the wave
# over to the right. The green wave is now out of "phase" with the other waves.

# Finally, in yellow, we plot the sum of these three waves and we get something
# that doesn't quite seem to have the pattern of a sine wave. Sometimes the
# values in y1, y2 and y3 are all positive or all negative so y4 has a big value
# or small value (you might say y1, y2 and y3 are constructive with each other).
# Other times some of y1, y2 and y3 are negative and the other(s) are positive,
# so y4 has a "middle of the road" value closer to zero. (You might say they
# are destructive of each other.)

import numpy as np
import matplotlib.pyplot as pl

# Create a list or set of x values. There will be about 240 of them, since 
# the distance on the number line between -4pi and 4pi is about 24, and each
# of those 24 intervals are split in 10 (since the step is 0.1).
x = np.arange(-4.0 * np.pi, 4.0 * np.pi, 0.1)

# y1 is just the values in x with the sin function applied.
# e.g. The third value of x is approximately -12.37 and the third value of y1 is
#      sin(-12.37), which is approximately 0.1987. 
y1 = np.sin(x)

# y2 is just the values in x multiplied by 2, and then sin is applied.
# So the third value of y2 is sin(2 * -12.37) = sin(-24.74) which is 0.389.
y2 = np.sin(2.0 * x)

# y2 is just the vaules of x with 4 added, then sin applied.
# So the third value of y3 is sin(-12.37 + 4.0) = sin(-8.37) = -0.87.
y3 = np.sin(x + 4.0)

# y4 is jsut the sum of the values in y1, y2 and y3. So the third value of y4
# is approximately 0.1987 + 0.389 -0.87 = -0.283.
y4 = y1 + y2 + y3

# This plots the four lists of y values on one plot. y1, y2 and y3 are plotted
# using dots, hence the ".", and y4 is printed as a line, hence the "-".
pl.plot(x, y1, "b.", x, y2, "r.", x, y3, "g.", x, y4, "y-")
pl.show()
