<<<<<<< HEAD
"""standard, library imports."""
=======
"""
Importing necessary modules for testing Dice class
"""
>>>>>>> 910bbded5f98bbc9bb53068b342410c4de296c9a
import sys
import unittest
sys.path.append("pig")
from pig.dice import Dice

sys.path.append("pig")


class TestDice(unittest.TestCase):
    """Testing the Dice class."""

    def setUp(self):
        """Set up the Dice object for testing."""
        self.dice = Dice()

    def test_the_roll(self):
        """Testing that a random die is being rolled from 1,6."""
        roll_test = self.dice.roll()
        self.assertTrue(roll_test >= 1 and roll_test <= 6)

    def test_get_roll(self):
        """Controlling the dice roll to make sure it is between 1,6."""
        roll_test = self.dice.get_roll()
        self.assertTrue(roll_test <= 6 and roll_test >= 1)


if __name__ == "__main__":
    unittest.main()
