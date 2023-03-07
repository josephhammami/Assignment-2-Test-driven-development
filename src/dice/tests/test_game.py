"""
Necessary modules to run the tests
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from Game import Game


class Game_Test(unittest.TestCase):
    """
    A test suite for the Game class.
    """

    def test_init_objects(self):
        """
        Test that initializing a Game object sets the player names and CPU level correctly.
        """
        new_game = Game("Name1","Name2","easy")
        self.assertEqual(new_game.player_one, "Name1")
        self.assertEqual(new_game.player_two, "Name2")
        self.assertEqual(new_game.cpu_level, "easy")

    @patch('random.randint', return_value=1)
    def test_cpu_turn_roll(self, mock_randint):
        """
        Test that the cpu_turn() method correctly calls cpu_rolling() when a 1 is generated.
        """
        game = Game("","","")
        game.cpu_level = MagicMock()
        game.cpu_turn()
        game.cpu_level.cpu_rolling.assert_called_once()

    @patch('random.randint', return_value=2)
    def test_cpu_turn_hold(self, mock_randint):
        """
        Test that the cpu_turn() method correctly calls cpu_hold() when a 2 is generated.
        """
        game = Game("","","")
        game.cpu_level = MagicMock()
        game.cpu_turn()
        game.cpu_level.cpu_hold.assert_called_once()


    @patch('sys.stdout', new_callable=StringIO)
    def test_cheat(self, mock_stdout):
        """
        Test that the cheat() method correctly sets the player score to 100 and prints a message.
        """
        game = Game(None, None, None)
        player_name = "Joseph"
        player_score = 0
        new_score = game.cheat(player_name, player_score)
        expected_output = f"{player_name} cheated and won the game!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(new_score, 100)


if __name__ == "__main__":
    unittest.main()
