from player import Player


class User(Player):
    def __init__(self, name):

        super().__init__(name)
        pass

    def gesture_choice(self):
        self.choice = input(self.gestures)

# user will input which gesture they want
# validate user input or reprompt user if invalid


# player = input("Player choose your move!").lower()
