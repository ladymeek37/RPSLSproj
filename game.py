from human import Human
from ai import AI

class Game:

    def __init__(self):
        human = Human("Jeff")
        ai = AI("AI")

    def display_welcome(self):
        print('')
        print ("Welcome to Rock, Paper, Sciccors, Lizard, Spock!")
        print("Each match will be best of three games.")
        print("Use number keys 0-4 to make a selection.")
        print('')
        pass
    
    def display_rules(self):
        print("")
        print ("RULES:")
        print ("Scissors cut Paper")
        print ("Paper covers Rock")
        print ("Rock crushes Lizard")
        print ("Lizard poisons Spock")
        print ("Spock smashes Scissors")
        print ("Scissors decapitates Lizard")
        print ("Lizard eats Paper")
        print ("Paper disproves Spock")
        print ("Spock vaporizes Rock")
        print ("Rock crushes Scissors")
        print("")

    def display_options(self):
        print("")
        print("OPTONS:")
        print ("Choose 0 for rock.")
        print ("Choose 1 for paper.")
        print ("Choose 2 for scissors.")
        print ("Choose 3 for lizard.")
        print ("Choose 4 for spock.")

    def game_phase(self):
        self.display_rules()
        number_of_players = input(int("How many players? 1 or 2"))
        if number_of_players == 1:
            self.display_options()
            gesture_input = input(int("Choose your gesture.  "))




        print
        pass

    def display_overall_winner(self):
        pass

    def play_again(self):
        pass

    def run_game(self):
        pass
