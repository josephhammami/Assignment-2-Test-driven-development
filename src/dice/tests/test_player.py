"""
Importing necessary modules for testing
"""
import unittest
from unittest.mock import patch
from Player import Player


class TestPlayer(unittest.TestCase):
    """
    Testing the Player Class
    """

    def setUp(self):
        """
        Created a object of Player.
        """
        self.New_player = Player('player')

    def test_get_name(self):
        """
        Test to get_name if that will return correct name.
        """
        p_name = self.New_player.get_name()
        self.assertEqual(p_name, 'player')

    def test_set_name(self):
        """
        Test to set_name if it is rightly name of the player.
        """
        self.New_player.set_name('player')
        p_name = self.New_player.get_name()
        self.assertEqual(p_name, 'player')

    def test_choose_name(self):
        """
        Test to choose_name if it gets the same name of the player's input.
        """

        with patch('builtins.input', return_value='player'):
            self.New_player.choose_name()
            p_name = self.New_player.get_name()
        self.assertEqual(p_name, 'player')

    def test_change_name(self):
        """
        Test to change_name if it is the same name of the player's input.
        """

        with patch('builtins.input', return_value='player'):
            self.New_player.change_name()
            p_name = self.New_player.get_name()
        self.assertEqual(p_name, 'player')


if __name__ == '__main__':
    unittest.main()
