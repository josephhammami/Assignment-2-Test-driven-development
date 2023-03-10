<<<<<<< HEAD
"""standard library imports."""
=======
"""Importing necessary modules for testing the DiceHand Class."""
>>>>>>> 910bbded5f98bbc9bb53068b342410c4de296c9a
import sys
import unittest
sys.path.append("pig")
from pig.dicehand import DiceHand

sys.path.append("pig")


class TestDiceHand(unittest.TestCase):
    """Testing DiceHand Class."""

    def setUp(self):
<<<<<<< HEAD
        """Set up DiceHand object for testing."""
        self.dicehand = DiceHand()

    def test_roll_dice_two(self):
        """The dice roll always return a 2."""
=======
        """ Setting up DiceHand object for testing."""
        self.dicehand = DiceHand()

    def test_roll_dice_two(self):
        """The dice roll always return a 2 with this test."""
>>>>>>> 910bbded5f98bbc9bb53068b342410c4de296c9a
        self.dicehand.dice.roll = lambda: 2
        self.dicehand.roll_dice("Test")
        self.assertEqual(self.dicehand.player_score, 2)

    def test_roll_dice_zero(self):
<<<<<<< HEAD
        """Get dice roll always return a 0."""
=======
        """The dice roll always return a 0 with this test."""
>>>>>>> 910bbded5f98bbc9bb53068b342410c4de296c9a
        self.dicehand.dice.roll = lambda: 1
        self.dicehand.roll_dice("Test")
        self.assertEqual(self.dicehand.player_score, 0)

    def test_hold(self):
<<<<<<< HEAD
        """Get player score is always 15 if player has hold."""
=======
        """The player score is always 15 if player has hold with this test."""
>>>>>>> 910bbded5f98bbc9bb53068b342410c4de296c9a
        self.dicehand.set_player_score(15)
        self.dicehand.hold("Test")
        self.assertEqual(self.dicehand.player_score, 15)


if __name__ == "__main__":
    unittest.main()
