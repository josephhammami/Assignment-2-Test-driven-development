"""
The random module is implemented so that a random number.

between 1-6 can be selected for when the player rolls it.
"""
import random


class Dice:
    """
    This class will be holding the functionalities of the possible.

    dice numbers you can roll.
    """

    def roll(self):
        """Do a random number 1 to 6."""
        return random.randint(1, 6)

    def get_roll(self):
        """Get the die roll made by the player."""
        return self.roll()
