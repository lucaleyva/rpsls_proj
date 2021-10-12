from player import Player


class User(Player):
    def __init__(self, name):

        super().__init__(name)
        pass

    def gesture_choice(self):
        is_valid_input = False
        
        while is_valid_input != True:

            choice = input("Please choose your throw '0' for rock, '1' for paper, '2' for scissors, '3' for lizard, '4' for spock.")
            # player = input("Player choose your move!").lower()
            
            if choice == "0":
                self.choice = "rock"
                is_valid_input = True
                # return choice
            elif choice == "1":
                self.choice = "paper"
                is_valid_input = True
                # return choice
            elif choice == "2":
                self.choice = "scissors"
                is_valid_input = True
                # return choice
            elif choice == "3":
                self.choice = "lizard"
                is_valid_input = True
                # return choice
            elif choice == "4":
                self.choice = "spock"
                is_valid_input = True
                # return choice
            else:
                print("Invalid choice. Please select again.")
        return self.choice
        

        # else:
        #     print("Invalid option. Please select again.")
        #     self.gesture_choice()
        

        
# user will input which gesture they want
# validate user input or reprompt user if invalid


# player = input("Player choose your move!").lower()
