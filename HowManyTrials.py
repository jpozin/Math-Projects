"""This module is to recreationally count the number of Bernoulli(p) trials until a string of successful events occurs.
An example is calculating how many trials it takes before one gets 20 heads in a row
In this module, a Bernoulli(p) distribution is a Bernoulli distribution with success probability p"""

from random import random

def isSuccess(p=0.5):
	"""Determine whether a single Bernoulli(p) trial is a success
	Parameter p must be a number between 0 and 1 (inclusive)
	Returns True if successful, False otherwise"""
	assert 0 <= p <= 1, "p must be a number between 0 and 1 (inclusive)"
	return True if random() <= p else False

def countTrials(n=20, p=0.5, fails=0):
	"""Count the number of trials until a trial of length n occurs with exactly (n - fails) successes
	Here, a trial is a sequence of n (int) independent Bernoulli events
	n (int) is a positive integer specifying the length of each trial
	p (float) is a number between 0 and 1 (exclusive)
	fails (int) is a nonnegative integer less than or equal to n specifying the number of failures in a trial
	This function, when iterated several times and results are averaged, approximates
	the mean number of trials required before a trial occurs with exactly (n - fails) successes
	This is closely related to the binomial distribution"""
	assert type(n) is int and n > 0, "n must be a positive int"
	assert type(p) is float and 0 < p < 1, "p must be a float between 0 and 1, exclusive"
	assert type(fails) is int and 0 <= fails <= n, "fails must be an int between 0 and n, inclusive"
	numTrials = 0
	while True:
		numTrials += 1
		mylist = [random() <= p for x in range(n)]
		if mylist.count(False) == fails:
			return numTrials
