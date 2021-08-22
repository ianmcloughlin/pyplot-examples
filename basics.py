#! /usr/bin/env python
# Author: Ian McLoughlin
# Date: 23/01/2015

# 1. Printing to the screen.
print "Hello, world!"
print 123
print 123.4
print "The number after", 1, "is", 2

print

# 2. Using variables.
x = 123
y = 123.4
a = "Hello, world"
print x, y, a

# 3. If statements.
if 1 < 2:
	print "1 is less than 2"
elif 1 > 2:
	print "1 is greater than 2"
else:
	print "1 is neither less than or equal to 2"

print

# 4. Lists
li = [1,2,3]
print "The list is", li
print "The third element of the list is", li[2]
li = ["xyz", "def"]
print li
li[0] = "abc"
print li
li.append("ghi")
print "li is", li
print "The length of li is", len(li)

print

# 5. For loops.
cars = ["Skoda", "Merc", "Porsche", "VW", "Nissan"]
for car in cars:
	print "car is", car
for i in range(len(cars)):
	print i, cars[i]

# 6. While loops.
i = 10
while i > 0:
	print "i is", i
	i -= 2
	
print

# 6. Functions
def f(x):
	y = x * x
	return y
print f(3)
print f(10)

print

# 7. Strings
s = "Hello, world!"
print s
print s[2]
print s[2:5]
print s[7:11]

print