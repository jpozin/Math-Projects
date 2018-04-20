from random import choice
from string import printable
from sys import argv

characters = list(printable)

def UnboundedBogoGenerateText(desiredstr, showstrings=False):
	"""Unbounded bogo text generation procedure
	
	Randomly generate a string of characters until it matches the input characters
	At each iteration, characters that are correct letter is kept
	It is possible that the same incorrect character may be tried in a specific position, hence the unboundedness of this procedure"""
	assert all([(x in printable) for x in desiredstr]), "Characters in input must be printable ASCII characters"
	mylist = list(desiredstr)
	newlist = [choice(characters) for x in range(len(desiredstr))]
	count = 1
	while newlist != mylist:
		count += 1
		if showstrings:
			print(ListToString(newlist))
		for i in range(len(newlist)):
			if newlist[i] != mylist[i]:
				newlist[i] = choice(characters)
	if showstrings:
		print(ListToString(newlist))
	return count


def ListToString(alist, useAssert=False):
	"""Convert a list of strings into a single string
	alist is the list to be converted into a string
	if useAssert is True, then the function checks whether all elements of alist are strings before proceeding"""
	if useAssert:
		assert all([isinstance(x, str) for x in alist]), "All elements of input list must be strings"
	return ''.join(alist)

if __name__ == '__main__':
	desiredstr = argv[1]
	showstrings = False
	if len(argv) >= 2:
		showstrings = bool(argv[2].lower() in ('1', 'true', 't'))
	x = UnboundedBogoGenerateText(desiredstr, showstrings)
	print(f"It took {x} iterations to generate '{desiredstr}'")