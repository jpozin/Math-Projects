# This module is intended to generate random numbers with specific distributions using only a uniform (0, 1) random number
# This module is not intended to provide a better alternative to pre-existing functions of similar scope
# It is intended to be instructional and provide a glimpse at random number simulation

from random import random
from math import log1p

def UnifNum(a, b):
	"""Generate a uniformly distributed random number in the interval (a, b)"""
	assert a < b, "a must be less than b"
	return a + (b-a)*random()

def ExpoNum(rate):
	"""Generate an exponentially distributed random number with rate (lambda)"""
	assert rate > 0, "lambda (rate) must be positive"
	return (-1/rate)*log1p(random()-1)

