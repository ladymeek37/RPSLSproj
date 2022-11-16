from human import Human
from ai import AI
import time

class Game:

    def __init__(self):
        self.human_one = Human("Player One")
        self.human_two = Human("Player Two")
        self.ai = AI("AI")

    def display_welcome(self):
        print('')
        print ("Welcome to Rock, Paper, Sciccors, Lizard, Spock!")
        print("Each match will be best of three games.")
        print('')
        time.sleep(1)
        pass
    
    def display_rules(self):
        print ("")
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
        print ("")
        time.sleep(1)

    def display_options(self):
        time.sleep(1)
        print("")
        print("OPTONS:")
        print ("Choose 0 for rock.")
        print ("Choose 1 for paper.")
        print ("Choose 2 for scissors.")
        print ("Choose 3 for lizard.")
        print ("Choose 4 for spock.")
        print("Use number keys 0-4 to make a selection.")
        time.sleep(1)

    def game_phase(self):
        human_one_score = 0
        human_two_score = 0
        ai_score = 0
        round = 1

        number_of_players = int(input("How many players? 1 or 2  "))

        while number_of_players == 1 and round <= 3:
            self.display_options()
            self.human_one.choose_gesture()
            human_one_gesture = self.human_one.human_gesture
            self.ai.choose_gesture()
            ai_gesture = int(self.ai.ai_gesture)

            time.sleep(1)
            if human_one_gesture == 2 and ai_gesture == 1:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 1 and ai_gesture == 2:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 1 and ai_gesture == 0:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 0 and ai_gesture == 1:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 0 and ai_gesture == 3:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 3 and ai_gesture == 0:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 3 and ai_gesture == 4:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 4 and ai_gesture == 3:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 4 and ai_gesture == 2:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 2 and ai_gesture == 4:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 2 and ai_gesture == 3:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 3 and ai_gesture == 2:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 3 and ai_gesture == 1:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 1 and ai_gesture == 3:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 1 and ai_gesture == 4:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 4 and ai_gesture == 1:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 4 and ai_gesture == 0:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 0 and ai_gesture == 4:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == 0 and ai_gesture == 2:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 2 and ai_gesture == 0:
                ai_score += 1
                print("AI wins this round!")
                round += 1
            elif human_one_gesture == ai_gesture:
                print ("Tie!")
                round += 1

            if round == 4 and ai_score > human_one_score:
                    self.winner = "AI"
            if round == 4 and human_one_score > ai_score:
                    self.winner = "Player One"
            if round == 4 and human_one_score == ai_score:
                    self.winner = "Tie!"
            

        while number_of_players == 2 and round <= 3:
            self.display_options()
            self.human_one.choose_gesture()
            human_one_gesture = self.human_one.human_gesture
            self.human_two.choose_gesture()
            human_two_gesture = self.human_two.human_gesture
            time.sleep(1)
            if human_one_gesture == 2 and human_two_gesture == 1:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 1 and human_two_gesture == 2:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 1 and human_two_gesture == 0:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 0 and human_two_gesture == 1:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 0 and human_two_gesture == 3:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 3 and human_two_gesture == 0:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 3 and human_two_gesture == 4:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 4 and human_two_gesture == 3:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 4 and human_two_gesture == 2:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 2 and human_two_gesture == 4:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 2 and human_two_gesture == 3:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 3 and human_two_gesture == 2:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 3 and human_two_gesture == 1:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 1 and human_two_gesture == 3:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 1 and human_two_gesture == 4:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 4 and human_two_gesture == 1:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 4 and human_two_gesture == 0:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 0 and human_two_gesture == 4:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == 0 and human_two_gesture == 2:
                human_one_score += 1
                print("Player One wins this round!")
                round += 1
            elif human_one_gesture == 2 and human_two_gesture == 0:
                human_two_score += 1
                print("Player Two wins this round!")
                round += 1
            elif human_one_gesture == human_two_gesture:
                print ("Tie!")
                round += 1

            if round == 4 and human_two_score > human_one_score:
                self.winner = self.human_two.name
            if round == 4 and human_one_score > human_two_score :
                self.winner = self.human_one.name
            if round == 4 and human_one_score == human_two_score :
                self.winner = "It's a tie!"
                
            pass

    def display_overall_winner(self):
        print ("")
        print ("And the winner of Rock, Paper, Sciccors, Lizard, Spock is...")
        print (f"{self.winner}!!!")

    def play_again(self):
        print("")
        again = input("Do you want to play again? y/n  ")
        print("")
        while again == "y":
            self.game_phase()
            self.display_overall_winner()
            print("")
            again = input("Do you want to play again? y/n  ")
        if again == "n":
            print("")
            print("Thanks for playing!")
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.game_phase()
        self.display_overall_winner()
        self.play_again()
        pass
