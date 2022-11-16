from player import Player
import time

class Human(Player):

    def __init__(self,name):
        super().__init__()
        self.name = name 
        self.score = 0

    def choose_gesture(self):
        print("")
        self.human_gesture = int(input(f"{self.name}, choose your gesture:  "))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        time.sleep(1)
        print(f'{self.name} has picked {gesture_list[self.human_gesture]}!')
        print("")
