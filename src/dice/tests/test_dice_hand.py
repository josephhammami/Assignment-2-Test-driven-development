"""
Importing necessary modules for testing the DiceHand Class
"""
import unittest
from DiceHand import DiceHand


class TestDiceHand(unittest.TestCase):
    """
    Testing DiceHand Class
    """

    def setUp(self):
        """
        Setting up DiceHand object for testing
        """
        self.dicehand = DiceHand()

    def test_roll_dice_two(self):
        """" The dice roll always return a 2 """
        self.dicehand.dice.roll = lambda: 2
        self.dicehand.roll_dice('Test')
        self.assertEqual(self.dicehand.player_score, 2)

    def test_roll_dice_zero(self):
        """" The dice roll always return a 0  """
        self.dicehand.dice.roll = lambda: 1
        self.dicehand.roll_dice('Test')
        self.assertEqual(self.dicehand.player_score, 0)

    def test_hold(self):
        """" The player score is always 15 if player has hold """
        self.dicehand.set_player_score(15)
        self.dicehand.hold('Test')
        self.assertEqual(self.dicehand.player_score, 15)


if __name__ == '__main__':
    unittest.main()
