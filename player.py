class Player:
    def __init__(self):
        # both have gesture picks in common
        # both have a score (+1)
        pass

    # Common things between user and AI.
# gestures = ["rock", "paper", "scissors", "lizard", "spock"]

# tie_results = [("rock","rock"), ("paper","paper"), ("scissors","scissors"), ("lizard","lizard"), ("spoke","spoke")]
# win_results = [("rock","scissors"),("rock","lizard"),("paper","spock"),("scissors","paper"),("scissors","lizard"),("lizard","spock"),("lizard","paper"),("spock","scissors"),("spock","rock")]
# lose_results = [("rock","spock"),("rock","paper"),("paper","scissors"),("paper","lizard"),("scissors","spock"),("scissors","rock"),("lizard","scissors"),("lizard","rock"),("spock","lizard"),("spock","paper")]

# print("Rock...")
# print("Paper...")
# print("Scissors...")
# print("Lizard...")
# print("Spock...")


player1 = input("Player 1, make your move: ")
print("***NO CHEATING!\n" * 20)
player2 = input("Player 2, make your move: ")

if player1 == player2:
	print("It's a tie!")
elif player1 == "rock":
	if player2 == "scissors" or player2 == "lizard":
		print("player1 wins!")
	elif player2 == "paper" or player2 == "spock":
		print("player2 wins!")
elif player1 == "paper":
	if player2 == "rock" or player2 == "spock":
		print("player1 wins!")
	elif player2 == "scissors" or player2 == "lizard":
		print("player2 wins!")
elif player1 == "scissors":
	if player2 == "paper" or player2 == "lizard":
		print("player1 wins!")
	elif player2 == "rock" or player2 == "spock":
		print("player2 wins!")	
elif player1 == "lizard":
	if player2 == "paper" or player2 == "spock":
		print("player1 wins!")
	elif player2 == "rock" or player2 == "scissors":
		print("player2 wins!")	
elif player1 == "spock":
	if player2 == "rock" or player2 == "scissors":
		print("player1 wins!")
	elif player2 == "paper" or player2 == "lizard":
		print("player2 wins!")	
else:
	print("something went wrong")
