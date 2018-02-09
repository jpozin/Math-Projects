# This module is intended to generate random numbers with specific distributions using only a uniform (0, 1) random number
# This module is not intended to provide a better alternative to pre-existing functions of similar scope
# It is intended to be instructional and provide a glimpse at random number generation using inverse transform sampling

from random import random
from math import log1p, exp, floor
# log1p is imported because it is more accurate for small values
# log1p(x) == log(1+x)

def log(x):
	"""Call the natural logarithm function using the log1p function in order to maintain high accuracy for near-zero values of x (real)"""
	return log1p(x-1)

def UnifNum(a, b):
	"""Generate a uniformly distributed random number in the interval (a, b)"""
	assert a < b, "a must be less than b"
	return a + (b-a)*random()

def ExpoNum(rate):
	"""Generate an exponentially distributed random number with positive rate lambda"""
	assert rate > 0, "lambda (rate) must be positive"
	return (-1/rate)*log(random())

def BernoulliNum(p):
	"""Generate a Bernoulli distributed random number with parameter p (float)"""
	assert 0 < p < 1, "Probability parameter p must be between 0 an 1, exclusive"
	return 1 if 0 < random() <= p else 0

def BinomialNum(n, p):
	"""Generate a binomially distributed random number with parameters n (int) and p (float)"""
	assert type(n) == int, "n must be an integer"
	assert n >= 1, "n must be greater than or equal to 1"
	assert 0 < p < 1, "p must be between 0 and 1, exclusive"
	return sum([BernoulliNum(p) for x in range(n)])

def GeometricNum(p):
	"""Generate a geometrically distributed number given parameter p (float)
	p is strictly between 0 and 1
	Support is {1, 2, 3, ...}"""
	assert 0 < p < 1, "p must be between 0 and 1, exclusive"
	return floor(log(random()) / log(1-p))

def DiscUnifNum(a, b):
	"""Generate a discrete uniformly distributed number in the interval [a, b]"""
	assert a < b, "a must be less than b"
	return round(UnifNum(a-.5, b+.5))

def DiscUnifNum2(a, b):
	"""Another way to generate a discrete uniformly distributed number in the interval [a, b]"""
	assert a < b, "a must be less than b"
	return floor(UnifNum(a, b+1))

def WeibullNum(alpha, lambd):
	"""Generate a Weibull-distributed number with shape parameter alpha > 0 (float) and scale parameter lambd > 0 (float)"""
	assert alpha > 0, "alpha (shape parameter) must be greater than zero"
	assert lambd > 0, "lambda (scale parameter) must be greater than zero"
	return exp((1/alpha)*log((-1/lambd**alpha)*log(random())))

def DiscreteDistNum(pmf_dict):
	"""Generate a random number from a discrete distribution with a given pmf
	pmf_dict (dict) is a dictionary of the form {x:Pr(x)}, where x is a real numeric type and 0 <= Pr(x) <= 1
	Sum of probabilities in pmf_dict must equal 1 for the pmf to be valid"""
	assert sum(pmf_dict.values()) == 1, "Probabilities of pmf must sum to 1"
	for probability in pmf_dict.values():
		assert 0 <= probability <= 1, "Probabilities must be in the interval [0, 1]"
	for num in pmf_dict.keys():
		assert type(num) in (int, float), "Values of the random variable must be of a real numeric type (int or float)"
	cum_prob = 0
	cmf_list = []
	for num in pmf_dict:
		cum_prob += pmf_dict[num]
		cmf_list.append((num, cum_prob))
	cmf_list.sort(key=lambda x: x[1])
	rand = random()
	if 0 <= rand <= cmf_list[0][1]:
		return cmf_list[0][0]
	for i in range(len(cmf_list) - 1):
		if cmf_list[i][1] <= rand <= cmf_list[i+1][1]:
			return cmf_list[i+1][0]
