from random import randrange
import sys

def RandomChoice(alist):
	randnum = randrange(len(alist))
	return alist[randnum]

if __name__ == '__main__':
	print(RandomChoice(sys.argv[1:]))