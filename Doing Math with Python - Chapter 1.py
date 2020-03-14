# Introduction
print('Hello IDLE')

print(1 + 2)

print(1 + 3.5)

print(-1 + 2.5)

print(100 - 45)

print(-1.1 + 5)

# Making Fractions

from fractions import Fraction
f = Fraction(3,4)
print(f)

print( f + 1 + 1.5)

# complex numbers
# use j or J instead of i

a = 2 + 3j
print(type(a))

# we can also use complex() to specify complex numbers
a = complex(2,3)
print(a)

b = 3 + 3j
print(a + b)
print(a - b)

# get the real parts of imaginary numbers
print(a.real)
# get the imaginary parts of imaginary numbers
print(a.imag)

# get the conjugate of imaginary numbers
print(a.conjugate())

# to get the magnitude of imaginary numbers, we can use 
# the equation (real number ** 2 + imaginary ** 2) ** 0.5 or use the abs() function
print(abs(a))

# There is also a standard library 'cmath' that can 
# do specialized, complex math

### Getting User Input
a = input()
# returns always as a string
# use int() or float() to convert to a number
print(int(a) + 1)

## Handling Exceptions and Invalid Input

try:
    a = float(input('Enter a number: '))
except ValueError:
    print('You entered an invalid number')