"""
A single line containing the complex number Z .
Note: complex() function can be used in python to convert
the input as a complex number.

"""
import cmath
import math

eq = input()
pa = cmath.phase(complex(eq))
r = abs(complex(eq))

print ("{0}\n{1}".format(r,pa))