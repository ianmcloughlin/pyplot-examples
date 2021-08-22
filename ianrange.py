#! /usr/bin/env python

# This example just shows you how you might re-create numpy's arange function
# yourself. The function doesn't return a list of numbers like arange, but
# merely prints the values to the screen instead.
# You might, in your own time, try to get the function to return the list of
# numbers like arange does.

# We define a function called "ianrange" that takes three parameters, a
# starting point, and ending point, and an amount to increase by at each
# step.
# numpy's arange function allows you to omit start and step, which this function
# doesn't. It's easy to change it to - Google "python optional parameters."
def ianrange(start, stop, step):
	# These lines are tabbed in once, to show they are part of the function.
	# We'll create a variable called i and set it to start.
	i = start
	# Then we loop while i is less than stop.
	while i < stop:
		# These lines are tabbed in again, to show they are part of the while
		# loop (which is in the function ianrange, so we're tabbed in twice.)
		# This prints the value of i to the screen.
		print i
		# This increases i by step. Note we'd usually write this as:
		# i += step
		i = i + step

# This line is not tabbed in at all. That means it's not part of the while
# loop (if it was tabbed in twice, it would be), and it's not part of the
# function ianrange (if it was tabbed in once or twice, it would be.)
# It's a statement all by itself, and just shows how to use the function.
# This is the only part of this script that actually does anything visual
# on screen. If you delete it, the above function is just created silently
# when you run the script, and then the script exits.
ianrange(2.0, 10.0, 0.5)

