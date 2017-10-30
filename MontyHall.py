from random import randrange

door_choice = int(input("Will you pick door 1, 2, or 3 every time? "))
switch_strategy = int(input("Will you stay (0) or switch(1) every time? "))
runs = int(input("How many times do you want to run this simulation? "))
wins = 0
losses = 0
for i in range(runs):
	real_door = randrange(1,4)
	if door_choice == real_door and switch_strategy == 0:
		wins += 1
	elif door_choice != real_door and switch_strategy == 1:
		wins += 1
	else:
		losses += 1
win_prob = wins / (wins + losses)
result = f"""You played this game {runs} times. The results are as follows:
You won {wins} times.
You lost {losses} times.
Your probability of winning with your strategy is {round(100*win_prob, 5)}%."""
print(result)