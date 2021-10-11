from player import Player
from random import randint

class Computer(Player):
    def __init__(self):
        super().__init__()
    pass


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
        


