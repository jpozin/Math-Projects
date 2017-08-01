#Estimate the Apery Constant using a Monte Carlo method

#Created by Joel Pozin on 5/5/2017

from math import gcd
from random import randrange

def gcd3(alist):
    return gcd(alist[0],gcd(alist[1],alist[2]))

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
