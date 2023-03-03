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
        
    def information(self):
        print("+---------------------+")
        print("| Information         |")
        print("+---------------------+")
        print("| \u2022 The game will now begin! |")
        print("| \u2022 If you wish to alter the difficulty press 'd' |")
        print("| \u2022 If you wish to change your name press 'n' |")
        print("| \u2022 To view the high score table, press 't' |")
        print("| \u2022 To activate the cheat, press 'c' |")
        print("+-----------------------+")
    
    # #saved        
    # def gameFunction(self, result):
    #     score = []
    #     current_score = 0
        
    #     if score != 1:
    #        score.append(result)
    #        current_score = sum(score)
    #        return current_score
        
    #     else:
    #         return current_score == 0:
                              
            
hand = DiceHand()         
dice = Game()
new_player = Player("Unknown")

dice.rules()
print("Choose a name: ")
new_player.choose_name()

dice.information()
current_score = 0
keep_going = True

while keep_going:
    print("Do you wish to play or HOLD")
    choice = input(">> ")
    
    if choice == "play".lower():
        hand.roll_dice()
        current_score += hand.roll_dice()
        print(f"You rolled a {hand.roll_dice}")
        print(f"Your current score is: {current_score}")
           
        
    
    