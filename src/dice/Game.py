from Player import Player
from HighScore import HighScore
from Intelligence import Intelligence
from Histogram import Histogram
from DiceHand import DiceHand

class Game():
    
    def __init__(self):
        pass
    



    def rules(self):
        print("+-----------------------+")
        print("| Rules of Pig          |")
        print("+-----------------------+")
        print("| \u2022 Each player takes turns rolling a die |")
        print("| \u2022 You score points equal to the sum of your rolls |")
        print("| \u2022 If you roll a 1, you lose all your points |")
        print("| \u2022 You can choose to hold and pass your turn to the next player |")
        print("| \u2022 The first player to score 100 points wins |")
        print("+-----------------------+")


keep_going = True
new_player = Player("Unknown")
dice = Game()

while keep_going:
    dice.rules()
    print("Choose a name: ")
    new_player.choose_name()