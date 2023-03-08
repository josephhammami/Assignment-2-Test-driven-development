import unittest

from Dice import dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.d = dice()

    def test_The_roll(self):
        roll_test = self.d.roll()
        self.assertTrue(roll_test >= 1 and roll_test <= 6)

    def test_get_roll(self):
        roll_test = self.d.get_roll()
        self.assertTrue(roll_test <= 6 and roll_test >= 1)


if __name__ == '__main__':
    unittest.main()
