# test.py
# A simple program to find primitive Euler Bricks

import math
from fractions import gcd

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

min = 1
max = 1000

print 'Calculating Euler Bricks from ' + str(min) + ' to ' + str(max) + ':\n'

# Iterate over all combinations a <= b <= c
for a in range(min, max):
    for b in range(a, max):
        for c in range(b, max):
            # At least one side must be odd
            if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
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

