import unittest

from DiceHand import DiceHand


class TestDiceHand(unittest.TestCase):

    def setUp(self):
        """" Initializes a DiceHand object """
        self.DiceHand = DiceHand()

    def test_rollDice(self):
        """" The dice roll always return a 2 """
        self.DiceHand.dice.roll = lambda: 2
        self.DiceHand.roll_dice('Test')
        self.assertEqual(self.DiceHand.player_score, 2)
        """" The dice roll always return a 0  """
        self.DiceHand.dice.roll = lambda: 1
        self.DiceHand.roll_dice('Test')
        self.assertEqual(self.DiceHand.player_score, 0)

    def test_hold(self):
        """" The player score is always 15 if player has hold """
        self.DiceHand.set_player_score(15)
        self.DiceHand.hold('Test')
        self.assertEqual(self.DiceHand.player_score, 15)


if __name__ == '__main__':
    unittest.main()
