# Return a Collatz chain for a given integer input
# Output returned as a list

# Created by Joel Pozin on March 7, 2017

import sys

def collatz(num):
    """
        if n is even, n/2
        if n is odd, 3n+1
    """
    newlist = [num]
    while num != 1:
        if num%2 == 0:
            num //= 2
        elif num%2 == 1:
            num = 3*num + 1
        newlist.append(num)
    return newlist

if __name__ == "__main__":
    try:
        collatz(int(sys.argv[1]))
    except ValueError:
        print("Incompatible input, please try again")
