#! /usr/bin/env python

# This example came from an answer on Stack Exchange, which was found by
# Googling "plot sine wave python". The answer is available here:
# http://stackoverflow.com/questions/22566692/python-how-to-plot-graph-sine-wave

# The original solution was:
# 
# import matplotlib.pyplot as plt
# import numpy as np
#
# Fs = 8000
# f = 5
# sample = 16
# x = np.arange(sample)
# y = np.sin(2 * np.pi * f * x / Fs)
# plt.plot(x, y)
# plt.xlabel('voltage(V)')
# plt.ylabel('sample(n)')
# plt.show()
# 

# In class, we went through this answer trying to figure out what each command
# does. We kept changing and deleting parts, and re-running the script to see
# the effect.

# This makes the plotting functions in pyplot available to us.
import matplotlib.pyplot as plt
# This makes the numerical functions of numpy available to us.
import numpy as np

# We decided to delete the following variables in the original solution.
# That meant we had to replace any place they were used with the actual values.
# Fs = 8000
# f = 5
# sample = 16

# Original: x = np.arange(sample)
# We changed "sample" to "16", which was sample's value.
# x = np.arange(16)
# We then figured out, by copying and pasting np.arange(16) into the iPython
# console, that np.arange gives us a list of (in this case, 16) numbers back.
# We had a look at the numpy arange documentation online, and figured out
# we could change the step value, and add a starting value.
# Since we had been talking about values between -4pi and 4pi, which are approx.
# -12 and 12, we stuck those in as start and end points, and set the step to
# 0.1 (try changing the step to 0.5 or 1 or 2 and see what happens).
x = np.arange(-12.0, 12.0, 0.1)

# Original: y = np.sin(2 * np.pi * f * x / Fs)
# Again, here we replaced variables with their values, and it became this:
# y = np.sin(2 * np.pi * 5 * x / 8000)
# Then we just deleted the uninteresting number out (2, 5 and 8000) and the
# graph changed a bit, but it still looked okay.
# y = np.sin(np.pi * x)
# We then realised that np.pi represented the number pi, which is about 3.14.
# We decided to remove it from here (since we were already dealing with pi)
# in the arange function.
y = np.sin(x)

# We knew this just creates a 2D plot of x versus y.
plt.plot(x, y)

# And we deleted/commented out these two lines, since all they did was add
# labels to the axes.
# plt.xlabel('voltage(V)')
# plt.ylabel('sample(n)')

# This just tells Python to show a window with the plot we just created.
plt.show()

# We had a few observations about the graph:
# 1. The maximum value of sin(x) is 1.
# 2. The minimum value is -1.
# 3. These max/min values were related to te sin function itself, being the
#    "opposite" divided by the "hypotenuse" in a right-angled triangle. The
#    hypotenuse is always at least as long as the opposite, dividing one by
#    the other always gives at most 1.
# 4. You might wonder how you could have a negative value for sin, as defined.
#    This is related to the unit circle, which you can Google.