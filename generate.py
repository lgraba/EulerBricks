# test.py
# A simple program to find primitive Euler Bricks and, if it exists, a perfect cuboid among those Euler Bricks,
# then insert found Euler Bricks into database.
# Note: This is very inefficient - Object orientation, clean up, and convention compliance necessary in the future

import math
from fractions import gcd
import time
import insert

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

# Test for number-theoretical constraints for Perfect Cuboid
def constrain(x, y, z):
    # One side must be odd
    if ((x % 2) - 1) == 0 or ((y % 2) - 1) == 0 or ((z % 2) - 1) == 0:
        # One side must have length divisible by 5
        if x % 5 == 0 or y % 5 == 0 or z % 5 == 0:
            # One side must have length divisible by 7
            if x % 7 == 0 or y % 7 == 0 or z % 7 == 0:
                # One side must have length divisible by 11
                if x % 11 == 0 or y % 11 == 0 or z % 11 == 0:
                    # One side must have length divisible by 19
                    if x % 19 == 0 or y % 19 == 0 or z % 19 == 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
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
                # Calculate diagonal lengths
                ab = diagonal(a, b)
                ac = diagonal(a, c)
                bc = diagonal(b, c)
                # Test integer-ness of each diagonal length
                if isInteger(ab) and isInteger(ac) and isInteger(bc):
                    # Make sure GCD(a,b,c) = 1 (primitive)
                    if GCD(a, b, c) == 1:
                        # Insert brick into database
                        insert.addBrick(a, b, c, ab, ac, bc)
                        # Check for perfect cuboid if number theory constraints are satisfied
                        if constrain(a, b, c):
                            if isInteger(diagonal(diagonal(a, b), c)):
                                insert.addPerfect(a, b, c, abc)
                                print ('PERFECT CUBOID FOUND: ')
                        # Print the side lengths and diagonal lengths if so
                        print (str(a) + '   ' + str(b) + '   ' + str(c) + '    :   ' + str(ab) + '   ' + str(ac) + '   ' + str(bc))

minimum = 1
maximum = 1000000

print ('Calculating Euler Bricks from ' + str(minimum) + ' to ' + str(maximum) + ':\n')

t0 = time.clock()

# Execute search from minimum to maximum
search(minimum, maximum)

# Record and calculate time elapsed
t1 = time.clock()
total = t1 - t0

# Add stats to database
insert.addStats(total, maximum)

print ('\nEfficiency:')
print ('%.2e' % number + ' triplets examined over ' + str(total) + ' seconds.')
print ('%.3e' % (number/total) + ' triplets examined per second.')