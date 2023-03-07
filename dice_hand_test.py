import unittest

from DiceHand import DiceHand


class TestDiceHand(unittest.TestCase):

    def setUp(self):
        self.dice_hand = DiceHand()

    def test_roll_dice(self):
        # the dice roll always return a 5
        self.dice_hand.player_roll = 5
        diceRoll = self.dice_hand.roll_dice('Player 2 ')
        self.assertEqual(diceRoll, 5)

        # The dice roll return a 0
        self.dice_hand.player_roll = 1
        diceRoll = self.dice_hand.roll_dice('Player 3')
        self.assertEqual(diceRoll, 0)

    def test_hold(self):
        self.dice_hand.set_player_score(20)
        self.dice_hand.hold("Player 1")
        self.assertEqual(self.dice_hand.player_score, 20)


if __name__ == '__main__':
    unittest.main()
