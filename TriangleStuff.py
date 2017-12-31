import sys
from math import sqrt

class TriangleException(Exception):
	pass

def isValidTriangle(a, b, c):
	return (a + b > c) and (a + c > b) and (b + c > a)

def Perimeter(a, b, c):
	return a + b + c

def Area(a, b, c):
	s = Perimeter(a, b, c) / 2
	return sqrt(s*(s-a)*(s-b)*(s-c))

if __name__ == '__main__':
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
	if not isValidTriangle(a, b, c):
		raise TriangleException("Your triangle is invalid; please check your side lengths.")
	ShowThis = f"""The perimeter off your triangle is {Perimeter(a, b, c)}.
	The area of your triangle is {Area(a, b, c)}."""
