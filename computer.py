# from player import Player
from random import randint

# class Computer(Player):
#     def __init__(self):
#         super().__init__()
#     pass


# will randomly generate choice
player = input("Player choose your move!").lower()
rand_number = randint(0, 4)

if rand_number == 0:
    computer = "rock"
elif rand_number == 1:
     computer = "paper"
elif rand_number == 2:
     computer = "scissors"
elif rand_number == 3:
     computer = "lizard"
elif rand_number == 4:
    computer = "spock"

print(f" Computer chose {computer}")
        

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors" or computer == "lizard":
		print("player wins!")
	elif computer == "paper" or computer == "spock":
		print("computer wins!")
elif player == "paper":
	if computer == "rock" or computer == "spock":
		print("player wins!")
	elif computer == "scissors" or computer == "lizard":
		print("computer wins!")
elif player == "scissors":
	if computer == "paper" or computer == "lizard":
		print("player wins!")
	elif computer == "rock" or computer == "spock":
		print("computer wins!")	
elif player == "lizard":
	if computer == "paper" or computer == "spock":
		print("player wins!")
	elif computer == "rock" or computer == "scissors":
		print("computer wins!")	
elif player == "spock":
	if computer == "rock" or computer == "scissors":
		print("player wins!")
	elif computer == "paper" or computer == "lizard":
		print("computer wins!")	
else:
	print("something went wrong")

