from computer import Computer
from user import User


class Gameboard:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        pass

    def run_game(self):
        self.display_welcome()
        self.choose_gametype()
        pass

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard and Spock!')
        print('The rules are the same as traditional Rock Paper Scissors but adding Lizard and Spock. Here are all the combinations: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes, Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard')
        # we can worry about the looks of this later

    def choose_gametype(self):
        game_type = input(
            "Please select a game type: '1' for single user or '2' for multiplayer")
        if game_type == '1':
            self.player_one = User("Al")
            self.player_two = Computer()
            # print('you have chosen to play against a computer)
            pass
            # set up user vs computer
        elif game_type == '2':
            self.player_one = User("Al")
            self.player_two = User('Bob')
            # print(you have chosen to play against another user)
            # set up user vs user
            pass
        else:
            self.choose_gametype

        def display_throw_options(self):
            user_choice = User
            user_choice = self.gesture_choice
            # user_input = input(
            #     "Please choose your throw 'rock', 'paper', 'scissors', lizard or spock")

    # def battle(self):
    #     self.player1 = Human()
    #     player2 = Computer()

    # # ->
    #     self.p1_gesture = player1.choseGesture()
    #     self.p2_gesture = player2.choseGesture()

        # conditional check

    # <-
