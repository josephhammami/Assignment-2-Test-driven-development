""" 
This class will hold the core functionalities of the player (user), playing our dice game.
"""

class Player:
    """ 
    A class representing a player in our dice game.
    """

    name = ""

    def __init__(self, name):
        """ 
        Constructs a new Player object.
        
        Parameters:
        - name (str): the initial name of the player.
        """
        self.name = name

    def set_name(self,new_name):
        """ 
        sets the name of the player with the new given value.
        
        Parameters:
        - new_name (str): the new name of the player.
        """
        self.name = new_name

    def choose_name(self):
        """
        Allows the player to choose their name by entering it at the prompt.
        """
        name = input(">> ")
        self.set_name(name)

    def change_name(self):
        """
        Allows the user to change their name by entering a new name at the given prompt. 
        """
        new_name = input(">> ")
        self.set_name(new_name)