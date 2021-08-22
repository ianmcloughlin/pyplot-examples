#! /usr/bin/env python
# Author: Ian McLoughlin
# Date: 23/01/2015

# How the fibonacci function works:
# Start with a=1 and b=1.
# On each pass through loop, set a to be the old b, and set b to be
# the sum of the old a and the old b.
# Initially: a=1, b=1
# Loop pass 1: a=b=1 and b=a+b=1+1=2
# Loop pass 2: a=b=2 and b=a+b=1+2=3
# Loop pass 3: a=b=3 and b=a+b=2+3=3
# etc.
# If you imagine the fibonacci numbers in a list: [0,1,1,2,3,5...]
# then basically a and b slide along the list each time you loop:
# [0,1,1,2,3,5,...]
# [a,b]
#   [a,b]
#     [a,b]
#        etc.

# This function returns the n^th fibonacci number.
def fibonacci(n):
	if n < 1:
		return "not defined"
	
	a = 0, b = 1
	for i in range(1, n):
		# Below, think of the a and b to the left of the equals to
		# be the new values of a and b, and the a and b's on the right
		# to be the old values (created in the last pass of the loop.)
		a, b = b, a + b
	return a

# This just shows how to use the function.
test = 60
print "Fibonacci number", test, "is", fibonacci(test)

# Uncomment the following lines to create a plot of
# the first 100 fibonacci numbers.
# fibs = []
# for i in range(1, 101):
# 	x = fibonacci(i)
# 	fibs.append(x)
# import matplotlib.pyplot as mp
# mp.plot(fibs, ".")
# mp.show()