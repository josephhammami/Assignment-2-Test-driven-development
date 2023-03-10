"""Implement random module to generate random numbers with this module."""
import random


class Dice:
    """This class functionality of dice numbers you can roll."""

    def roll(self):
        """Random number will be rolled and determine score for the player."""
        return random.randint(1, 6)

    def get_roll(self):
        """Get the die roll made by the player using this method."""
        return self.roll()
