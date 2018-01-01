from time import sleep
from sys import argv
import pydealer

def sumCardList(alist):
	"""Return the value of a blackjack hand.
	alist is an iterable with pydealer.card.Card elements."""
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

def dealerActions(dealer_stack, main_deck):
	"""A dealer hits when his/her hand is less than 17 and stay when hand is >= 17.
	Returns the value of the dealer's hand once the dealer stays.
	dealer_stack is a pydealer.stack.Stack object.
	main_deck is a pydealer.stack.Stack object."""
	while sumCardList(dealer_stack) < 17:
		dealer_stack.add(main_deck.deal(1)[0])
	return sumCardList(dealer_stack)

if __name__ == '__main__':
	numdecks = int(argv[1]) if len(argv) >= 2 else 6
	stack = pydealer.Stack()
	for i in range(numdecks):
		deck = pydealer.Deck()
		stack.add(deck)
	stack.shuffle()
	while cardnum < len(stack) - 10: # The -10 is in case there are many hits
		dealer_total = 0
		player_total = 0
		cardnum = 0
		x = stack.deal(4)
		dealer_stack = pydealer.Stack()
		dealer_stack.add((x[0], x[2]))
		player_stack = pydealer.Stack()
		player_stack.add((x[1], x[3]))
		player_string = 'Your cards are:\n'
		for card in player_deck:
			player_string += f'\t{card.value} of {card.suit}\n'
		player_string += f'Your current total is {sumCardList(player_stack)}'
		print(player_string + '\n')
		if sumCardList(player_stack) == 21:
			print("Blackjack! You win") # Account for whether dealer also has blackjack
			continue
		action = input("Will you hit ('h') or stand ('s')?  ").lower()
		while action not in ('h', 's'):
			action = input("Could not understand input. Will you hit ('h') or stand ('s')?  ").lower()
		if action == 's':
			player_value = sumCardList(player_stack)
			dealer_value = dealerActions(dealer_stack, stack)
			if dealer_value > 21:
				message = f"The dealer's value is {dealer_value}. The dealer busts. You win!"
				print(message)
			elif player_value > dealer_value:
				message = f"The dealer's value is {dealer_value}. Your value is {player_value}. You win!"
				print(message)
			elif player_value < dealer_value:
				message = f"The dealer's value is {dealer_value}. Your value is {player_value}. You lose."
				print(message)
			else:
				message = f"The dealer's value is {dealer_value}. Your value is {player_value}. The result is a push."
				print(message)
		elif action == 'h':
			# Write code for when the player hits