from player import Player
import random


class Computer(Player):
    def __init__(self, name):

        super().__init__(name)
        pass

    def gesture_choice(self):
        self.choice = random.choice(self.gestures)
        return self.choice
        # will randomly generate choice
        # player = input("Player choose your move!").lower()
        # rand_number = randint(0, 4)
        # if rand_number == 0:
        #     computer = "rock"
        # elif rand_number == 1:
        #     computer = "paper"
        # elif rand_number == 2:
        #     computer = "scissors"
        # elif rand_number == 3:
        #     computer = "lizard"
        # elif rand_number == 4:
        #     computer = "spock"

        # print(f" Computer chose {computer}")

        # if player == computer:
        #     print("It's a tie!")
        # elif player one == "rock":
        #     if computer == "scissors" or computer == "lizard":
        #         print("player wins!")
                    # self.player_one.score += 1
                    # self.best_of_three()
        #     elif computer == "paper" or computer == "spock":
        #         print("computer wins!")
        # elif player == "paper":
        #     if computer == "rock" or computer == "spock":
        #         print("player wins!")
        #     elif computer == "scissors" or computer == "lizard":
        #         print("computer wins!")
        # elif player == "scissors":
        #     if computer == "paper" or computer == "lizard":
        #         print("player wins!")
        #     elif computer == "rock" or computer == "spock":
        #         print("computer wins!")
        # elif player == "lizard":
        #     if computer == "paper" or computer == "spock":
        #         print("player wins!")
        #     elif computer == "rock" or computer == "scissors":
        #         print("computer wins!")
        # elif player == "spock":
        #     if computer == "rock" or computer == "scissors":
        #         print("player wins!")
        #     elif computer == "paper" or computer == "lizard":
        #         print("computer wins!")
        # else:
        #     print("something went wrong")

        # # def is_tie():
        # 	if player == computer:
        # 		print("It's a tie!")
        # 		return (0, player, computer)

        # def is_win(player, computer):
        # 	if player == "rock":
        # 		if computer == "scissors" or computer == "lizard":
        # 			print("player wins!")
        # 			return True
        # 	elif player == "paper":
        # 		if computer == "rock" or computer == "spock":
        # 			print("player wins!")
        # 			return True
        # 	elif player == "scissors":
        # 		if computer == "paper" or computer == "lizard":
        # 			print("player wins!")
        # 			return True
        # 	elif player == "lizard":
        # 		if computer == "paper" or computer == "spock":
        # 			print("player wins!")
        # 			return True
        # 	elif player == "spock":
        # 		if computer == "rock" or computer == "scissors":
        # 			print("player wins!")
        # 			return True
        # 	else:
        # 		print("something went wrong")
        # 		return False
