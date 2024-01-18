#module math function

# MATH.CEIL(X)
# Return the celling of x, the smallest integer grater than or equal to x. If x is not a float,
# delegates to x.__ceil__(),
# which return an integeral value.

import math
x=11.8
print(math.ceil(x))

# MATH.FABS(X) : return the absolute value of x
x= -10
print(math.fabs(x))

#MATH.FACTORIAL(X) : Return x factorial as an integer. Raises Value error if x is not integral of is negative.
x=5
print(math.factorial(x))

# MATH>FLOOR(X) : Return the floor of x, the largest integer less than of equal to x. if x is not a float, delegates to
# x.__floor__(), which should return an integral value.

x=10.5
print(math.floor(x))

# MATH.FSUM(ITERABLE) : return an accurate floating point sum of values in the iterable.

l=[10,20,30,40,50,60]
print(math.fsum(l))

# MATH.SQRT(X)  : Return the square root of x.

x=81
print(math.sqrt(x))


