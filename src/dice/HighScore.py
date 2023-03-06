"""
This class will hold the high score of the player through their various games with the CPU.
"""

class HighScore():
    """
    A class representing the high score table for our dice game.
    """

    def __init__(self, record_player_one, record_player_two, record_player_one_singleplayer):
        """
        Constructs a new high score object.
        """
        self.record_player_one_singleplayer = record_player_one_singleplayer
        self.record_player_one = record_player_one
        self.record_player_two = record_player_two
    
    def set_record_player_one_singleplayer(self, new_record):
        
        self.record_player_one_singleplayer = new_record  
        
    def set_record_player_one(self, new_record):
        
        self.record_player_one = new_record

    def set_record_player_two(self, new_record):
        
        self.record_player_two = new_record
    
    
    def get_record_player_one_singleplayer(self):
        return self.record_player_one_singleplayer 

    def get_record_player_one(self):
        return self.record_player_one
    
    def get_record_player_two(self):
        return self.record_player_two
    
    
    def add_record_player_one_singeplayer(self, new_record):
        
        if self.record_player_one_singleplayer == 0 or new_record < self.record_player_one_singleplayer:
            self.set_record_player_one_singleplayer(new_record)
            
    def add_record_player_one(self, new_record_one):
        """
        Adds a new record to the high score table.
        """
        
        if self.record_player_one == 0 or new_record_one < self.record_player_one:
            self.set_record_player_one(new_record_one)
            
        
        
    def add_record_player_two(self, new_record_two):
        
        if self.record_player_two == 0 or new_record_two < self.record_player_two:
            self.set_record_player_two(new_record_two)
            
    def print_highscore_singleplayer(self, player_one, new_record_one):
        """
        Prints out a nice table displaying the high scores.
        """
        print("High Scores Table")
        print("-----------------------")
        print("Single Player Mode:")
        print("-----------------------")
        print("| {:<10} | {:<6} |".format("Player", "Record"))
        print("-----------------------")
        print("| {:<10} | {:<6} |".format(str(player_one), str(new_record_one)))
        print("-----------------------")
            
    def print_highscore_multiplayer(self, player_one, player_two, new_record_one, new_record_two):
        
        print("High Scores Table")
        print("----------------------")    
        print("Multiplayer Mode:")
        print("----------------------")
        print("| {:<10} | {:<6} |".format("Player", "Record"))
        print("----------------------")
        print("| {:<10} | {:<6} |".format(str(player_one), str(new_record_one)))
        print("| {:<10} | {:<6} |".format(str(player_two), str(new_record_two)))
        print("----------------------")
