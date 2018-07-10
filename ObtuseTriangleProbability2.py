# This module is intended to determine the probability a triangle is obtuse
# Given that its vertices are determined uniformly in the unit circle

from numpy.random import rand
from numpy import mean, std
from scipy.stats import sem, t
import matplotlib.pyplot as plt
from math import sqrt, acos, pi, cos, sin
from itertools import combinations
from sys import argv

def CreateTriangle():
	"""Creates a random triangle in the unit square
	Returns a list with three points of the form (x, y)
	These coordinates are generated uniformly in the unit circle"""
	vertices = []
	for i in range(3):
		theta = 2*pi*rand()
		u = rand() + rand()
		r = 2-u if u > 1 else u
		vertices.append((r*cos(theta), r*sin(theta)))
	return vertices

def DistPoints(p1, p2):
	"""Calculate the distance between two points of the form (x, y)"""
	return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

def TriangleAngles(alist):
	"""Determine the angles of a triangle given a list of its vertices
	The list must contain three tuples of the form (x, y)
	This function does not check to ensure this requirement is met"""
	a, b, c = (DistPoints(tup[0], tup[1]) for tup in combinations(alist, 2))
	angles = [acos((a**2 + b**2 - c**2) / (2*a*b)),
			  acos((a**2 + c**2 - b**2) / (2*a*c)),
			  acos((b**2 + c**2 - a**2) / (2*b*c))]
	return angles

def isObtuse(alist):
	"""Determine whether a triangle is an obtuse triangle given a list of its vertices
	The list must contain three tuples of the form (x, y)
	This function does not check to ensure this requirement is met"""
	for angle in TriangleAngles(alist):
		if angle > pi/2:
			return True
	return False

def isRight(alist):
	"""Determine whether a triangle is a right triangle given a list of its vertices
	The list must contain three tuples of the form (x, y)
	This function does not check to ensure this requirement is met
	This function is supplementary and is not used in this module"""
	return any(not (x - pi/2) for x in TriangleAngles(alist))

def isAcute(alist):
	"""Determine whether a triangle is an acute triangle given a list of its vertices
	The list must contain three tuples of the form (x, y)
	This function does not check to ensure this requirement is met
	This function is supplementary and is not used in this module"""
	for angle in TriangleAngles(alist):
		if angle == pi/2 or angle > pi/2:
			return False
	return True

def CI_mean(alist, alpha=.95, round_num=False):
	"""Generate a confidence interval about the mean of a list of numbers with confidence alpha"""
	mu, s = mean(alist), sem(alist)
	n = len(alist)
	HL = s * t.ppf((1+alpha)/2, n-1)
	return tuple(round(x, 2) for x in (mu - HL, mu + HL)) if type(round_num) is int else (mu - HL, mu + HL)

if __name__ == '__main__':
	iterations = int(argv[2]) if len(argv) >= 3 else 1
	trials_per_iteration = int(argv[1]) if len(argv) >= 2 else 50
	alpha = float(argv[3]) if len(argv) >= 4 else .95
	totalProbs = [mean([isObtuse(CreateTriangle()) for x in range(trials_per_iteration)]) for i in range(iterations)]

	mystr =\
f"""The mean probability of a triangle being obtuse is:  {round(mean(totalProbs), 2)}
The standard deviation is:  {round(std(totalProbs), 2)}
A {100*alpha}% confidence interval for the mean of this probability is:  {CI_mean(totalProbs, alpha, 2)}"""
	print(mystr)

	plt.hist(totalProbs)
	plt.show()