from player import Player


class User(Player):
    def __init__(self, name):

        super().__init__(name)
        pass

    def gesture_choice(self):
        self.choice = input("Please choose your throw '0' for rock, '1' for paper, '2' for scissors, '3' for lizard, '4' for spock.")
        # player = input("Player choose your move!").lower()
        
        if self.choice == "0":
            self.choice = "rock"
        elif self.choice == "1":
            self.choice = "paper"
        elif self.choice == "2":
            self.choice = "scissors"
        elif self.choice == "3":
            self.choice = "lizard"
        elif self.choice == "4":
            self.choice = "spock"
        return self.choice
        
# user will input which gesture they want
# validate user input or reprompt user if invalid


# player = input("Player choose your move!").lower()
