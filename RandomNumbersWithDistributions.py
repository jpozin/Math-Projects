# This module is intended to generate random numbers with specific distributions using only a uniform (0, 1) random number
# This module is not intended to provide a better alternative to pre-existing functions of similar scope
# It is intended to be instructional and provide a glimpse at random number generation using inverse transform sampling

from random import random
from math import log1p, floor

def UnifNum(a, b):
	"""Generate a uniformly distributed random number in the interval (a, b)"""
	assert a < b, "a must be less than b"
	return a + (b-a)*random()

def ExpoNum(rate):
	"""Generate an exponentially distributed random number with positive rate lambda"""
	assert rate > 0, "lambda (rate) must be positive"
	return (-1/rate)*log1p(random()-1)

def BernoulliNum(p):
	"""Generate a Bernoulli random number with parameter p"""
	assert 0 < p < 1, "Probability parameter p must be between 0 an 1, exclusive"
	return 1 if 0 < random() <= p else 0

def DiscUnifNum(a, b):
	"""Generate a discrete uniformly distributed number in the interval [a, b]"""
	assert a < b, "a must be less than b"
	return round(UnifNum(a-.5, b+.5))

def DiscUnifNum2(a, b):
	"""Another way to generate a discrete uniformly distributed number in the interval [a, b]"""
	assert a < b, "a must be less than b"
	return floor(UnifNum(a, b+1))

def DiscreteDistNum(pmf_dict):
	"""Generate a random number with a given pmf
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
