class Player:
    def __init__(self, name):
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.score = 0
        self.name = name
        self.choice = None
        pass

    # Common things between user and AI.
