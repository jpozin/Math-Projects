from numpy.random import rand
from math import sqrt
from sys import argv

def distance(array1, array2):
	assert len(array1) == len(array2), "Arrays must be of the same dimension"
	return sqrt(sum([(array2[i] - array1[i])**2 for i in range(len(array1))]))

if __name__ == '__main__':
	dim = int(argv[1])
	assert dim >= 2, "Dimension must be greater than or equal to two"
	iterations = int(argv[2]) if len(argv) >= 3 else 10000
	assert iterations >= 10, "Iterations must be greater than or equal to 10"
	sum_dist = 0
	for i in range(iterations):
		array1 = rand(dim)
		array2 = rand(dim)
		sum_dist += distance(array1, array2)
	estimate = round(sum_dist / iterations, 5)
	print(f"With {iterations} iterations, the estimated distance between two points in a(n) {dim}-dimensional cube is {estimate}")