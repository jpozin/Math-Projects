from random import random
from math import log1p

def UnifNum(a, b):
	"""Generate a uniformly distributed random number in the interval (a, b)"""
	assert a < b, "a must be less than b"
	return a + (b-a)*random()

def ExpoNum(rate):
	"""Generate an exponentially distributed random number with rate (lambda)"""
	return (-1/rate)*log1p(random()-1)

