from time import sleep
from sys import argv
import pydealer

def sumCardList(alist):
	current_sum = 0
	num_aces = 0
	used_aces = 0
	for card in alist:
		if card.value not in ('Jack', 'Queen', 'King', 'Ace'):
			current_sum += int(card.value)
		elif card.value in ('Jack', 'Queen', 'King'):
			current_sum += 10
		else:
			num_aces += 1
			current_sum += 11
	while current_sum > 21 and used_aces < num_aces:
		current_sum -= 10
		used_aces += 1
	return current_sum

if __name__ == '__main__':
	numdecks = int(argv[1]) if len(argv) >= 2 else 6
	stack = pydealer.Stack()
	for i in range(numdecks):
		deck = pydealer.Deck()
		stack.add(deck)
	stack.shuffle()
	while cardnum < len(stack):
		dealer_total = 0
		player_total = 0
		cardnum = 0
		stack.deal(4)
