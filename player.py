"""
This class will hold the core functionalities of the player (user), playing.

our dice game.
"""


class Player:
    """A class representing a player in our dice game."""

    def __init__(self, name):
        """Construct a new Player object."""
        self.name = name

    def set_name(self, new_name):
        """Set the name of the player with the new given value."""
        self.name = new_name

    def get_name(self):
        """Get the name of the current player."""
        return self.name

    def choose_name(self):
        """Allow the player to choose aname by entering it at the prompt."""
        name = input(">> ")
        self.set_name(name)

    def change_name(self):
        """
        Allow the user to change their name by entering a new name at the.

        given prompt.
        """
        new_name = input(">> ")
        self.set_name(new_name)
