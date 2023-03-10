"""This class will hold the functionalities of the player in our dice game."""


class Player:
    """A class representing a player in our dice game."""

    def __init__(self, name):
        """Construct a new Player object."""
        self.name = name

    def set_name(self, new_name):
        """Set the name of the player with the new given value."""
        self.name = new_name

    def get_name(self):
        """Get the name of the current player in this method."""
        return self.name

    def choose_name(self):
        """Allow the player to choose the name in this method."""
        name = input(">> ")
        self.set_name(name)

    def change_name(self):
        """Allow the user to change the name in this method."""
        new_name = input(">> ")
        self.set_name(new_name)
