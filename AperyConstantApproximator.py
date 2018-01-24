#Estimate the Apery Constant using a Monte Carlo method

from math import gcd
from random import randrange
from sys import getrecusionlimit

def gcd3(alist):
    """Returns the gcd of a list of 3 integers"""
    assert len(alist) == 3, "There must 3 integers in the list"
    return gcd(alist[0], gcd(alist[1],alist[2]))

def gcd_many(alist):
	"""Returns the gcd of a list of several (at least 2) ints.
	The sie of the list must be less than or equal to the system's recursion limit to avoid recursion depth exceptions.
	This function serves no prupose in this module, but may be used freely in other programs."""
	assert len(alist) >= 1, "The size of the input list must be at least 2"
	assert len(alist) <= getrecursionlimit(), f"The size of the list must be less than {getrecursionlimit()} in order to avoid maximum recusrion depth exceptions"
	if len(alist) == 2:
		return gcd(alist[0], alist[1])
	else:
		return gcd(alist[0], gcd_many(alist[1:]))

def aperyEstimate(num):
    count = 0
    for i in range(num):
        mylist = []
        for j in range(3):
            x = randrange(int(1e6))
            mylist.append(x)
        if gcd3(mylist) == 1:
            count += 1
    return num / count

def main(num):
    print(aperyEstimate(num))

if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))
