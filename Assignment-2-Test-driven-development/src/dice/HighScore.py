"""
This class will hold the core functionalities for displaying and storing the players records.
"""


class HighScore():
    """
    A class representing the high score table for our dice game.
    """

    def __init__(self, record_player_one, record_player_two, record_player_one_singleplayer):
        """
        Constructs a new high score object for each available player.
        """
        self.record_player_one_singleplayer = record_player_one_singleplayer
        self.record_player_one = record_player_one
        self.record_player_two = record_player_two

    def set_record_player_one_singleplayer(self, new_record):
        """
        Sets a new record for player_one in the single player mode.
        """
        self.record_player_one_singleplayer = new_record

    def set_record_player_one(self, new_record):
        """
        Sets a new record for player_one in the multiplayer mode.
        """
        self.record_player_one = new_record

    def set_record_player_two(self, new_record):
        """
        Sets a new record for player_one in the multiplayer mode.
        """
        self.record_player_two = new_record

    def get_record_player_one_singleplayer(self):
        """
        Get the current record of player_one for the single player mode.
        """
        return self.record_player_one_singleplayer

    def get_record_player_one(self):
        """
        Get the currect record of player_one in the multiplayer mode.
        """
        return self.record_player_one

    def get_record_player_two(self):
        """
        Get the current record of player_two in the multiplayer mode.
        """
        return self.record_player_two

    def add_record_player_one_singeplayer(self, new_record):
        """
        Adds a new record for the player if the current record is set at 0 
        or the new record is less than the current one.
        """
        if self.record_player_one_singleplayer == 0 or new_record < self.record_player_one_singleplayer:
            self.set_record_player_one_singleplayer(new_record)

    def add_record_player_one(self, new_record_one):
        """
        Adds a new record for the player if the current record is set at 0 
        or the new record is less than the current one.
        """
        if self.record_player_one == 0 or new_record_one < self.record_player_one:
            self.set_record_player_one(new_record_one)

    def add_record_player_two(self, new_record_two):
        """
        Adds a new record for the player if the current record is set at 0 
        or the new record is less than the current one.
        """
        if self.record_player_two == 0 or new_record_two < self.record_player_two:
            self.set_record_player_two(new_record_two)

    def print_highscore_singleplayer(self, player_one, new_record_one):
        """
        Prints out a table displaying the high score of player_one from the single player mode.
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
        """_
        Prints out a table displaying the high score of player_one 
        and two from the multiplayer mode.
        """
        print("High Scores Table")
        print("----------------------")
        print("Multiplayer Mode:")
        print("----------------------")
        print("| {:<10} | {:<6} |".format("Player", "Record"))
        print("----------------------")
        print("| {:<10} | {:<6} |".format(str(player_one), str(new_record_one)))
        print("| {:<10} | {:<6} |".format(str(player_two), str(new_record_two)))
        print("----------------------")
