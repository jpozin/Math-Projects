from numpy.random import rand
from statistics import mean

def MonteCarloIntegrate(lambda_exp=lambda x: x, interval=(0, 1), n=10000):
	"""Use Monte Carlo integration to estimate the area under the curve of a function
	lambda_exp (lambda function) is a lambda expression; it is the function to be integrated
	interval (tuple(num, num)) is a tuple of int and/or float values; it is the interval over which the function is being integrated
	n (int) is the number of iterations used in the Monte Carlo integration"""
	assert type(n) == int, "n must be an integer"
	a, b = interval[0], interval[1]
	assert a < b, "The lower bound of the interval must be less than the upper bound of the interval"
	random_nums = ((a + (b-a)*num) for num in rand(n))
	my_map = map(lambda_exp, random_nums)
	return (b-a)*mean(my_map)