# test.py
# A simple program to find primitive Euler Bricks

import math
from fractions import gcd
import time

# Find the diagonal length given each side
def diagonal(side1, side2):
    return math.sqrt( pow(side1, 2) + pow(side2, 2) )

# Test integer-ness of a given diagonal length
def isInteger(number):
    if number % 1 == 0:
        return True
    else:
        return False
        
# Greatest Common Divisor of three integers
def GCD(x, y, z):
    return gcd(gcd(x, y), z)

# Test for number-theoretical constraints
def constrain(x, y, z):
    # One side must be odd
    if x % 2 == 0 or y % 2 == 0 or z % 2 == 0:
        return True
    else:
        return False

# Number of triplets examined (before constraints)
number = 0
    
# Iterate over all combinations a <= b <= c
def search(min, max):
    global number
    for a in range(min, max):
        for b in range(a, max):
            for c in range(b, max):
                number += 1
                # Constraints
                if constrain(a, b, c):
                    # Calculate diagonal lengths
                    ab = diagonal(a, b)
                    ac = diagonal(a, c)
                    bc = diagonal(b, c)
                    # Test integer-ness of each diagonal length
                    if isInteger(ab) and isInteger(ac) and isInteger(bc):
                        # Make sure GCD(a,b,c) = 1 (primitive)
                        if GCD(a, b, c) == 1:
                            # Print the side lengths and diagonal lengths if so
                            print str(a) + '   ' + str(b) + '   ' + str(c) + '    :   ' + str(ab) + '   ' + str(ac) + '   ' + str(bc)

minimum = 1
maximum = 1000

print 'Calculating Euler Bricks from ' + str(minimum) + ' to ' + str(maximum) + ':\n'
t0 = time.clock()
search(minimum, maximum)
t1 = time.clock()
total = t1 - t0
print '\nEfficiency:'
print str(number) + ' triplets examined over ' + str(total) + ' seconds.'
print str(number/total) + ' triplets examined per second.'