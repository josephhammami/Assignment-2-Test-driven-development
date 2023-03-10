"""A class containing unit tests for the Intelligence class."""
import sys
import unittest
import random
from unittest.mock import patch
from pig.intelligence import Intelligence

sys.path.append("pig")


class IntelligenceTest(unittest.TestCase):
    """A class containing unit tests for the Intelligence class."""

    def setUp(self):
        """
        Set up method that creates an object of Intelligence class.

        It sets intellegence level to easy
        """
        self.intelligence = Intelligence("easy")

    def test_set_level_easy(self):
        """
        Test that the CPU can roll a random number between 1 and 3 (inclusive).

        - when the level is set to "easy".
        """
        random.seed(1)
        self.intelligence.cpu_rolling()
        self.assertIn(self.intelligence.cpu_score, range(4))

    def test_set_level_medium(self):
        """
        Test that the CPU can roll a random number between 1 and 6 (inclusive).

        - when the level is set to "medium".
        """
        random.seed(1)
        self.intelligence.set_level("medium")
        self.intelligence.cpu_rolling()
        self.assertIn(self.intelligence.cpu_score, range(1, 7))

    def test_set_level_hard(self):
        """
        Test that the CPU can roll a random number between 1 and 10.

        -but if the number is greater than 6 it should be set to 6
        when the level is set to "hard".
        """
        random.seed(1)
        self.intelligence.set_level("hard")
        self.intelligence.cpu_rolling()
        self.assertIn(self.intelligence.cpu_score, range(1, 7))

    def test_cpu_rolling(self):
        """Tests the CPU rolling method."""
        with patch("random.randint") as mock_randint:

            mock_randint.return_value = 3
            self.intelligence.set_level("easy")
            self.intelligence.cpu_rolling()
            self.assertEqual(self.intelligence.cpu_score, 3)

            mock_randint.return_value = 6
            self.intelligence.set_level("medium")
            self.intelligence.cpu_rolling()
            self.assertLessEqual(self.intelligence.cpu_score, 6)

            mock_randint.return_value = 10
            self.intelligence.set_level("hard")
            self.intelligence.cpu_rolling()
            self.assertLessEqual(self.intelligence.cpu_score, 6)

    def test_cpu_hold(self):
        """Tests the CPU hold method."""
        self.intelligence.cpu_hold()
        self.assertEqual(self.intelligence.cpu_score, 0)


if __name__ == "__main__":
    unittest.main()
