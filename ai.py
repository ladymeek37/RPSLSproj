from player import Player
import random
import time

class AI(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0 

    def choose_gesture(self):
        time.sleep(1)
        self.ai_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        print (f"{self.name} has picked {gesture_list[int(self.ai_gesture)]}!")
        print ("")
