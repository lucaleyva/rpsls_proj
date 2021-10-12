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
