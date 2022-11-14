from player import Player
import random

class AI(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0 
        
    def choose_gesture(self):
        self.choose_gesture = str(random.randint(0,4))
        gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
        print (f"{self.name} has picked {gesture_list[int(self.choose_gesture)]}")
