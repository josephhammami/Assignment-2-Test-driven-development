"""
This class will hold the high score of the player through their various games with the CPU.
"""

class HighScore():
    """
    A class representing the high score table for our dice game.
    """

    def __init__(self):
        """
        Constructs a new high score object.
        """
        self.record_player_one = 0
        self.record_player_two = 0
        
    def set_record_player_one(self, new_record):
        
        self.record_player_one = new_record

    def set_record_player_two(self, new_record):
        
        self.record_player_two = new_record
        
    
    def get_record_player_one(self):
        return self.get_record_player_one
    
    def get_record_player_two(self):
        return self.get_record_player_two
    
    
        
        
    def add_record_player_one(self, player, new_record_one):
        """
        Adds a new record to the high score table.
        """
        self.record_player_one.append(player, new_record_one)
        
        
    def add_record_player_two(self, player_two, new_record_two):
        
        self.set_record_player_two(new_record_two)
        self.record_player_two.append(player_two, new_record_two)
        
    def print_highscore_singleplayer(self, player_one, new_record_one):
        """
        Prints out a nice table displaying the high scores.
        """
        print("High Scores Table")
        print("------------------")
        
        print("Single Player Mode:")
        print("-------------------")
        print("{:<10} {:<10}".format("Player", "Record"))
        print("-------------------")
        print("{:<10} {:<10}".format(player_one, new_record_one))
        print("-------------------")
        
    def print_highscore_multiplayer(self, player_one, player_two, new_record_one, new_record_two):
            
        print("Multiplayer Mode:")
        print("------------------")
        print("{:<10} {:<10} {:<10}".format("Player 1", "Record", "Player 2"))
        print("------------------")
        print("{:<10} {:<10}".format(player_one, new_record_one))
        print("{:<10} {:<10}".format(player_two, new_record_two))
        print("------------------")
