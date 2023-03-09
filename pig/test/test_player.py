"""Importing necessary modules for testing."""
import sys
import unittest
from unittest.mock import patch
from pig.player import Player
sys.path.append("path")


class TestPlayer(unittest.TestCase):
    """Test the Player Class."""

    def setUp(self):
        """Now we create an object of the Player Class."""
        self.new_player = Player('player')

    def test_get_name(self):
        """Test to get_name if that will return correct name."""
        p_name = self.new_player.get_name()
        self.assertEqual(p_name, 'player')

    def test_set_name(self):
        """Test to set_name if it is rightly name of the player."""
        self.new_player.set_name('player')
        p_name = self.new_player.get_name()
        self.assertEqual(p_name, 'player')

    def test_choose_name(self):
        """Test to choose_name if it gets the same name of player input."""
        with patch('builtins.input', return_value='player'):
            self.new_player.choose_name()
            p_name = self.new_player.get_name()
        self.assertEqual(p_name, 'player')

    def test_change_name(self):
        """Test to change_name if it is the same name of the player's input."""
        with patch('builtins.input', return_value='player'):
            self.new_player.change_name()
            p_name = self.new_player.get_name()
        self.assertEqual(p_name, 'player')


if __name__ == '__main__':
    unittest.main()
