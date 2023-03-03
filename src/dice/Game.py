from Player import Player
from HighScore import HighScore
from Intelligence import Intelligence
from Histogram import Histogram
from DiceHand import DiceHand
import random



class Game():
    
    def __init__(self):
        pass
    
    def print_rules(self):
        print("+-----------------------+") 
        print("| Rules of Pig          |")
        print("+-----------------------+")
        print("| \u2022 Each player takes turns rolling a die |")
        print("| \u2022 You score points equal to the sum of your rolls |")
        print("| \u2022 If you roll a 1, you lose all your points |")
        print("| \u2022 You can choose to hold and pass your turn to the computer |")
        print("| \u2022 The first reach 100 points wins |")
        print("+-----------------------+")
        
    def print_info(self):
        print("\n+---------------------+")
        print("| Information         |")
        print("+---------------------+")
        print("| \u2022 The game will now begin! |")
        print("| \u2022 To roll press 'r'|")
        print("| \u2022 To hold press 'h'|")
        print("| \u2022 If you wish to alter the difficulty press 'd' |")
        print("| \u2022 If you wish to change your name press 'n' |")
        print("| \u2022 To view the high score table, press 't' |")
        print("| \u2022 To activate the cheat, press 'c' |")
        print("+-----------------------+")
        
    def setup_game(self):
        self.print_rules()
         
        self.player = Player("")
        print("\nGo ahead and enter your name!")
        self.player.choose_name()  
        
        self.begin_game()
         
         
    def begin_game(self):
        player_turn = DiceHand()
        
        self.print_info()
        
        print("Before we begin, go ahead and decide the CPU's difficulity! (easy/medium/hard)")
        cpu_difficulty = input(">> ")
        self.cpu_level = Intelligence(cpu_difficulty)
        
        while True:
            print("Roll or hold?")
            action = input(">> ")
            
            if action.lower() == "r":
                player_turn.roll_dice()
                
                if player_turn.player_score >= 100:
                    print("Congrats! You won!")
                    break
                
                self.cpu_turn()
                
                if self.cpu_level.cpu_score >= 100:
                    print("The CPU wins!")
                    break
                
            elif action.lower() == "h":
                player_turn.hold()
            
            elif action.lower() == "d":
                print("What would you like to change the difficulty to?")
                self.cpu_level = input(">> ")
                
            elif action.lower() == "n":
                self.player.change_name()
            
    
    def cpu_turn(self):
        print("-----------------------------------------------------------------------------")
        cpu_hold = random.randint(1,2)
            
        if cpu_hold == 1:
            self.cpu_level.cpu_rolling()
            
        else:
            self.cpu_level.cpu_hold()
           
new_game = Game()
new_game.setup_game()