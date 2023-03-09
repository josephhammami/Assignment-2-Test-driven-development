"""
The random module is implemented so that a random number
between 1-6 can be selected for when the player rolls it.
"""
import random


class Dice:
    """
    This class will be holding the functionalities of the possible
    dice numbers you can roll.
    """

    def roll(self):
        """
        A random number will be rolled and determine the score for the player.
        """
        return random.randint(1, 6)

    def get_roll(self):
        """
        Gets the die roll made by the player.
        """
        return self.roll()
