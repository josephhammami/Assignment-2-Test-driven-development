"""
Importing necessary modules for testing Dice class
"""
import sys
import unittest
from pig.dice import Dice

sys.path.append("pig")


class TestDice(unittest.TestCase):
    """
    Testing the Dice class
    """

    def setUp(self):
        """
        Setting up the Dice object for testing
        """
        self.dice = Dice()

    def test_The_roll(self):
        """
        Testing that a random die is being rolled from 1,6
        """

        roll_test = self.dice.roll()
        self.assertTrue(roll_test >= 1 and roll_test <= 6)

    def test_get_roll(self):
        """
        Controlling the dice roll to make sure it is between 1,6
        """

        roll_test = self.dice.get_roll()
        self.assertTrue(roll_test <= 6 and roll_test >= 1)


if __name__ == "__main__":
    unittest.main()
