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
        print("+----------------------------------------------------------------------+") 
        print("|                            Rules of Pig                              |")
        print("+----------------------------------------------------------------------+")
        print("| \u2022          Each player takes turns rolling a die                     |")
        print("| \u2022          You score points equal to the sum of your rolls           |")
        print("| \u2022          If you roll a 1, you lose all your points                 |")
        print("| \u2022          You can choose to hold and pass your turn to the computer |")
        print("| \u2022          The first reach 100 points wins                           |")
        print("+----------------------------------------------------------------------+")
        
    def print_info(self, type):
        
        
        if type == "1":
            print("\n+-------------------------------------------------+")
            print("|                  Information                    |")
            print("+-------------------------------------------------+")
            print("| \u2022 The game will now begin!                      |")
            print("| \u2022 To roll press 'r'                             |")
            print("| \u2022 To hold press 'h'                             |")
            print("| \u2022 If you wish to alter the difficulty press 'd' |")
            print("| \u2022 If you wish to change your name, press 'n'    |")
            print("| \u2022 To view the high score table, press 't'       |")
            print("| \u2022 To activate the cheat, press 'c'              |")
            print("| \u2022 To restart the game, press 'g'                |")
            print("| \u2022 To exit the game, press 'r'                   |")
            print("+-------------------------------------------------+")
            
        elif type == "2": 
            #Cheating is now allowed against other players
            print("\n+-------------------------------------------------+")
            print("|                  Information                    |")
            print("+-------------------------------------------------+")
            print("| \u2022 The game will now begin!                      |")
            print("| \u2022 To roll press 'r'                             |")
            print("| \u2022 To hold press 'h'                             |")
            print("| \u2022 If you wish to alter the difficulty press 'd' |")
            print("| \u2022 If you wish to change your name, press 'n'    |")
            print("| \u2022 To view the high score table, press 't'       |")
            print("| \u2022 To restart the game, press 'g'                |")
            print("| \u2022 To exit the game, press 'r'                   |")
            print("+-------------------------------------------------+")
            
        
    def setup_game(self):
        self.player_one = Player("")
        self.player_two = Player("")
        
        self.print_rules()
        
        print("\nAre you playing against the CPU or a friend? (1 or 2 respectively)")
        option = input(">> ")
        
        
        if option == "1": 
            
            print("\nGo ahead and enter your name!")
            self.player_one.choose_name()  
            
            self.player_versus_cpu()
        
        elif option == "2":
            
            print(f"Go ahead and choose your names!")
            
            print(f"\nPlayer 1:")
            self.player_one.choose_name()
            
            print(f"\nPlayer 2:")
            self.player_two.choose_name()
            
            self.player_versus_player()
         
    def player_versus_cpu(self):
        player_turn = DiceHand()
        
        self.print_info("1")
        
        print("\nBefore we begin, go ahead and decide the CPU's difficulity! (easy/medium/hard)")
        cpu_difficulty = input(">> ")
        self.cpu_level = Intelligence(cpu_difficulty)
        
        while True:
            self.seperator()
            print(f"\n{self.player_one.get_name()} would you like to roll or hold?")
            action = input(">> ")
            
            if action.lower() == "r":
                player_turn.roll_dice(self.player_one.get_name())
                
                if player_turn.player_score >= 100:
                    print("Congrats! You won!")
                    break
                
                self.cpu_turn()
                
                if self.cpu_level.cpu_score >= 100:
                    print("The CPU wins!")
                    break
                
            elif action.lower() == "h":
                player_turn.hold(self.player_one.get_name())
                self.seperator()
            
            elif action.lower() == "d":
                print("\nWhat would you like to change the difficulty to?")
                alter_difficulty = input(">> ")
                self.cpu_level.set_level(alter_difficulty)
                self.seperator()
                
            elif action.lower() == "n":
                print("\nWhat would you like to change your new name to?")
                self.player_one.change_name()
                self.seperator()
            
            elif action.lower() == "c":
                self.cheat(self.player_one.get_name(), player_turn.player_score)
                break
            
    
    def cpu_turn(self):
        self.seperator()
        cpu_hold = random.randint(1,2)
            
        if cpu_hold == 1:
            self.cpu_level.cpu_rolling()
            
        else:
            self.cpu_level.cpu_hold()
    
    def player_versus_player(self):
        
        player_one_turn = DiceHand()
        player_two_turn = DiceHand()
        self.print_info("2")
        
        
        while True:
            
            print(f"{self.player_one.get_name()} would you like to roll or hold?")
            action_player_one = input(">> ")
            self.seperator()
            
            print(f"{self.player_two.get_name()} would you like to roll or hold?")
            action_player_two = input(">> ")
            self.seperator()
            
            if action_player_one.lower() == "r":
                player_one_turn.roll_dice(self.player_one.get_name())
                self.seperator()
                
                if player_one_turn.player_score >= 100:
                    print(f"{self.player_one.get_name()} won!")
            
            if action_player_two.lower() == "r":
                player_two_turn.roll_dice(self.player_two.get_name())
                self.seperator()
                
                if player_two_turn.player_score >= 100:
                    print(f"{self.player_two.get_name()} won!")
                    
            elif action_player_one.lower() == "h":
                player_one_turn.hold(self.player_one.get_name())
                self.seperator()
                
            elif action_player_two.lower() == "h":
                player_two_turn.hold(self.player_two.get_name())
                self.seperator()
            
            elif action_player_one.lower() == "n": 
                print(f"\n {self.player_one.get_name()} what would you like to change your new name to?")
                self.player_one.change_name()
                self.seperator()
            
            elif action_player_two.lower() == "n": 
                print(f"\n {self.player_two.get_name()} what would you like to change your new name to?")
                self.player_two.change_name()
                self.seperator()
      
    
    def cheat(self, player_name, player_score):
        player_score = 100
        print(f"{player_name} cheated and won the game!")
        return player_score
        
    
    
    def seperator(self):
        print("\n-----------------------------------------------------------------------------")         
        
        
                  
new_game = Game()
new_game.setup_game()
