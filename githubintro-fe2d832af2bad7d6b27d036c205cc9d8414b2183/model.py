# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
import random
# Set up variables.
y0 = 50
x0 = 50
my_random = random.random()
# Select random number boundaries
if my_random < 0.5:
   y0 = y0 + 1
else:
   y0 = y0 - 1
print (y0)
my_random = random.random()
if my_random < 0.5:
   x0 = x0 + 1
else:
   x0 = x0 - 1 
print (y0, x0)






y1 = 40
x1 = 40
# Select random number boundaries
my_random = random.random()
if my_random < 0.5:
   y1 = y1 + 1
else:
   y1 = y1 - 1
my_random = random.random()   
if my_random < 0.5:
   x1 = x1 + 1
else:
   x1 = x1 - 1 
print (y1, x1)

answer =  (((y1-y0)**2+(x1-x0)**2)**0.5)

print (answer)

