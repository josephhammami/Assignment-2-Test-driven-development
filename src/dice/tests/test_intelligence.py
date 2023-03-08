"""A class containing unit tests for the Intelligence class."""
import unittest
import random
from unittest.mock import patch
from Intelligence import Intelligence

class Intelligence_test(unittest.TestCase):

    """A class containing unit tests for the Intelligence class."""

    def setUp(self):
        """A set up method that creates an object of Intelligence class. 
        It sets intellegence level to easy"""
        self.intelligence = Intelligence("easy")


    def test_set_level_easy(self):
        """Test that the CPU can roll a random number between 1 and 3
        (inclusive) when the level is set to "easy"."""
        # Seed the random number generator to ensure reproducible results
        random.seed(1)

        # Call the cpu_rolling method to generate a random number
        self.intelligence.cpu_rolling()

        # Check that the cpu_score is within the expected range
        # for an "easy" level roll
        self.assertIn(self.intelligence.cpu_score, range(4))


    def test_set_level_medium(self):
        """Test that the CPU can roll a random number between 1 and 6
        (inclusive) when the level is set to "medium"."""

        # Seed the random number generator to ensure reproducible results
        random.seed(1)

        # Set the level to "medium"
        self.intelligence.set_level("medium")

        # Call the cpu_rolling method to generate a random number
        self.intelligence.cpu_rolling()

        # Check that the cpu_score is within the expected range
        # for a "medium" level roll
        self.assertIn(self.intelligence.cpu_score, range(1, 7))


    def test_set_level_hard(self):
        """Test that the CPU can roll a random number between 1 and 10,
        inclusive, but if the number is greater than 6 it should be set to 6
        when the level is set to "hard"."""

        # Seed the random number generator to ensure reproducible results
        random.seed(1)

        # Set the level to "hard"
        self.intelligence.set_level("hard")

        # Call the cpu_rolling method to generate a random number
        self.intelligence.cpu_rolling()

        # Check that the cpu_score is within the expected range
        # for a "hard" level roll
        self.assertIn(self.intelligence.cpu_score, range(1, 7))



    def test_cpu_rolling(self):
        """Tests the CPU rolling method."""
        with patch('random.randint') as mock_randint:
            # Test easy level
            mock_randint.return_value = 3
            self.intelligence.set_level('easy')
            self.intelligence.cpu_rolling()
            self.assertEqual(self.intelligence.cpu_score, 3)

            # Test medium level
            mock_randint.return_value = 6
            self.intelligence.set_level('medium')
            self.intelligence.cpu_rolling()
            self.assertLessEqual(self.intelligence.cpu_score, 6)

            # Test hard level
            mock_randint.return_value = 10
            self.intelligence.set_level('hard')
            self.intelligence.cpu_rolling()
            self.assertLessEqual(self.intelligence.cpu_score, 6)  # should be capped at 6



    def test_cpu_hold(self):
        """Tests the CPU hold method."""
        self.intelligence.cpu_hold()
        self.assertEqual(self.intelligence.cpu_score, 0)




if __name__ == '__main__':
    unittest.main()
