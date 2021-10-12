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
        self.battle()
        # self.display_throw_options()
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
            self.player_two = Computer("Computer")
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
            print("Invalid option. Please select again.")
            self.choose_gametype()

    # def display_throw_options(self):
        
        

            # user_input = input(
            #     "Please choose your throw 'rock', 'paper', 'scissors', lizard or spock")

    def battle(self):
        # self.player1 = Human()
        # player2 = Computer()

    # ->
        self.p1_gesture = self.player_one.gesture_choice()
        self.p2_gesture = self.player_two.gesture_choice()
        print(self.p1_gesture)
        print(self.p2_gesture)
        pass
    #     conditional check

        if self.p1_gesture == self.p2_gesture:
            print("It's a tie!")
            self.best_of_three()
        elif self.p1_gesture == "rock":
            if self.p2_gesture == "scissors" or self.p2_gesture == "lizard":
                print("player 1 wins!")
                self.player_one.score += 1
                self.best_of_three()
                # self.best_of_three()

            elif self.p2_gesture == "paper" or self.p2_gesture == "spock":
                print("player 2 wins!")
                self.player_two.score += 1
                self.best_of_three()
        elif self.p1_gesture == "paper":
            if self.p2_gesture == "rock" or self.p2_gesture == "spock":
                print("player 1 wins!")
                self.player_one.score += 1
                self.best_of_three()
            elif self.p2_gesture == "scissors" or self.p2_gesture == "lizard":
                print("player 2 wins!")
                self.player_two.score += 1
                self.best_of_three()

        elif self.p1_gesture == "scissors":
            if self.p2_gesture == "paper" or self.p2_gesture == "lizard":
                print("player 1 wins!")
                self.player_one.score += 1
                self.best_of_three()
            elif self.p2_gesture == "rock" or self.p2_gesture == "spock":
                print("player 2 wins!")
                self.player_two.score += 1
                self.best_of_three()

        elif self.p1_gesture == "lizard":
            if self.p2_gesture == "paper" or self.p2_gesture == "spock":
                print("player 1 wins!")
                self.player_one.score += 1
                self.best_of_three()
            elif self.p2_gesture == "rock" or self.p2_gesture == "scissors":
                print("player 2 wins!")
                self.player_two.score += 1
                self.best_of_three()

        elif self.p1_gesture == "spock":
            if self.p2_gesture == "rock" or self.p2_gesture == "scissors":
                print("player 1 wins!")
                self.player_one.score += 1
                self.best_of_three()
            elif self.p2_gesture == "paper" or self.p2_gesture == "lizard":
                print("player 2 wins!")
                self.player_two.score += 1
                self.best_of_three()

    def best_of_three(self):
        if self.player_one.score == 2:
            print("Player 1 wins best of 3!")
            # print()
        elif self.player_two.score == 2:
            print("Player 2 wins best of 3!")
            # print()
        else:
            print("Next round!")
            # print()
            self.battle()