import unittest
import random
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
        self.intelligence.set_level("easy")
        # Call the cpu_rolling method to generate a random number
        self.intelligence.cpu_rolling()

        # Check that the cpu_score is within the expected range
        # for an "easy" level roll
        self.assertIn(self.intelligence.cpu_roll, range(1, 4))


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

    
    def test_invalid_level(self):
        """Test that an exception is raised when an invalid level is set."""
        self.intelligence.set_level("invalid")
        # Attempt to set an invalid level
        with self.assertRaises(ValueError):
            self.intelligence.cpu_rolling()
    
        
        
    def test_cpu_rolling(self):
        """Tests the CPU rolling method."""
        random.seed(1)
        cpu_roll = self.intelligence.cpu_rolling()
        self.assertIn(cpu_roll, range(1, 4))

        self.intelligence.set_level('medium')
        random.seed(2)
        cpu_roll = self.intelligence.cpu_rolling()
        self.assertIn(cpu_roll, range(1, 7))

        self.intelligence.set_level('hard')
        random.seed(3)
        cpu_roll = self.intelligence.cpu_rolling()
        self.assertIn(cpu_roll, range(1, 11))



    def test_cpu_hold(self):
        """Tests the CPU hold method."""
        self.intelligence.cpu_hold()
        self.assertEqual(self.intelligence.cpu_score, 0)




if __name__ == '__main':
    unittest.main()