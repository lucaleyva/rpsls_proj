class Player:
    def __init__(self):
        # both have gesture picks in common
        # both have a score (+1)
        pass

    # Common things between user and AI.
# gestures = ["rock", "paper", "scissors", "lizard", "spock"]

tie_results = [("rock","rock"), ("paper","paper"), ("scissors","scissors"), ("lizard","lizard"), ("spoke","spoke")]
win_results = [("rock","scissors"),("rock","lizard"),("paper","spock"),("scissors","paper"),("scissors","lizard"),("lizard","spock"),("lizard","paper"),("spock","scissors"),("spock","rock")]
lose_results = [("rock","spock"),("rock","paper"),("paper","scissors"),("paper","lizard"),("scissors","spock"),("scissors","rock"),("lizard","scissors"),("lizard","rock"),("spock","lizard"),("spock","paper")]
