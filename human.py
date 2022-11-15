from player import Player

class Human(Player):

    def __init__(self,name):
        super().__init__()
        self.name = name 
        self.score = 0

    def choose_gesture(self):
        print("")
        self.choose_gesture = int(input("Choose your gesture:  "))
        gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
        print(f'{self.name} has picked {gesture_list[self.choose_gesture]}')
        print("")
