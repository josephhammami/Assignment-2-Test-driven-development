"""
Test the functionality of the HighScore class.
"""
import sys
import io
import unittest
from unittest.mock import patch
from pig.highscore import HighScore
sys.path.append("pig")

class HighScoreTest(unittest.TestCase):
    """
    Test the functionality of the HighScore class.
    """

    def setUp(self):
        """
        Create a new HighScore object for testing.
        """
        self.highscore = HighScore(0, 0, 0)

    def test_set_record_player_one_singleplayer(self):
        """
        Test that set_record_player_one_singleplayer sets the correct record.
        """
        self.highscore.set_record_player_one_singleplayer(10)
        self.assertEqual(self.highscore.get_record_player_one_singleplayer(), 10)

    def test_set_record_player_one(self):
        """
        Test that set_record_player_one sets the correct record.
        """
        self.highscore.set_record_player_one(20)
        self.assertEqual(self.highscore.get_record_player_one(), 20)

    def test_get_record_player_one_singleplayer(self):
        """
        Test that get_record_player_one_singleplayer returns the correct record.
        """
        self.highscore.set_record_player_one_singleplayer(10)
        self.assertEqual(self.highscore.get_record_player_one_singleplayer(), 10)

    def test_get_record_player_one(self):
        """
        Test that get_record_player_one returns the correct record.
        """
        self.highscore.set_record_player_one(20)
        self.assertEqual(self.highscore.get_record_player_one(), 20)

    def test_get_record_player_two(self):
        """
        Test that get_record_player_two returns the correct record.
        """
        self.highscore.set_record_player_two(30)
        self.assertEqual(self.highscore.get_record_player_two(), 30)

    def test_set_record_player_two(self):
        """
        Test that set_record_player_two sets the correct record.
        """
        self.highscore.set_record_player_two(30)
        self.assertEqual(self.highscore.get_record_player_two(), 30)

    def test_add_record_player_one_singleplayer(self):
        """
        Test that add_record_player_one_singleplayer adds the correct record.
        """
        self.highscore.add_record_player_one_singeplayer(5)
        self.assertEqual(self.highscore.get_record_player_one_singleplayer(), 5)

        self.highscore.add_record_player_one_singeplayer(15)
        self.assertEqual(self.highscore.get_record_player_one_singleplayer(), 5)

    def test_add_record_player_one(self):
        """
        Test that add_record_player_one adds the correct record.
        """
        self.highscore.add_record_player_one(10)
        self.assertEqual(self.highscore.get_record_player_one(), 10)

        self.highscore.add_record_player_one(5)
        self.assertEqual(self.highscore.get_record_player_one(), 5)

    def test_add_record_player_two(self):
        """
        Test that add_record_player_two adds the correct record.
        """
        self.highscore.add_record_player_two(15)
        self.assertEqual(self.highscore.get_record_player_two(), 15)

        self.highscore.add_record_player_two(25)
        self.assertEqual(self.highscore.get_record_player_two(), 15)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_highscore_singleplayer(self, mock_stdout):
        """
        Tests the print_highscore_singleplayer() method.

        This method tests whether the print_highscore_singleplayer() method 
        correctly prints out a high score table for a single player game.

        Args:
        self (TestHighScore): The TestHighScore instance.
        mock_stdout (io.StringIO): The mocked standard output stream.

        Returns:
        None.
        """

        highscore = HighScore(0, 0, 0)
        player_one = "Alice"
        new_record_one = 10
        expected_output = "High Scores Table\n-----------------------\nSingle Player Mode:\n-----------------------\n| Player     | Record |\n-----------------------\n| Alice      | 10     |\n-----------------------\n"
        highscore.print_highscore_singleplayer(player_one, new_record_one)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_highscore_multiplayer(self, mock_stdout):
        """
    Tests the print_highscore_multiplayer() method.

    This method tests whether the print_highscore_multiplayer() method 
    correctly prints out a high score table for a multiplayer game.

    Args:
        self (TestHighScore): The TestHighScore instance.
        mock_stdout (io.StringIO): The mocked standard output stream.

    Returns:
        None.
    """
        highscore = HighScore(0, 0, 0)
        player_one = "Alice"
        player_two = "Bob"
        new_record_one = 10
        new_record_two = 15
        expected_output = "High Scores Table\n----------------------\nMultiplayer Mode:\n----------------------\n| Player     | Record |\n----------------------\n| Alice      | 10     |\n| Bob        | 15     |\n----------------------\n"
        highscore.print_highscore_multiplayer(player_one, player_two,
                                               new_record_one, new_record_two)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
