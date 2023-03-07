"""
Random is imported to decide what the CPU rolls on the die.
"""
import random

class Intelligence:
<<<<<<< Updated upstream
    """
    This class will hold the core functionalities for the CPU in our dice game. 
    """

    def __init__(self, level):
        """ 
        Initializes an Intelligence object with the given level and a CPU score of 0.
=======
    
    
    def __init__(self, level):
        """
        Initializes a new instance of the Intelligence class.

        Args:
            level (str): The difficulty level of the game.
>>>>>>> Stashed changes
        """
        self.level = level
        self.cpu_score = 0

    def set_level(self, new_level):
        """
<<<<<<< Updated upstream
        Updates the level of difficulty for the CPU.
=======
        Sets a new difficulty level for the game.

        Args:
            new_level (str): The new difficulty level to set.
>>>>>>> Stashed changes
        """
        self.level = new_level

    def cpu_rolling(self):
        """
<<<<<<< Updated upstream
        Stimulates the CPU rolling the dice based on the current level of difficulty.
        Updates the CPU score and prints a message indicating the result of the roll.
        """

=======
        Simulates the CPU rolling the dice and updates its score.

        Raises:
            ValueError: If an invalid difficulty level is set.

        Returns:
            int: The value of the CPU roll.
        """
>>>>>>> Stashed changes
        if self.level == "easy".lower():
            cpu_roll = random.randint(1,3)

        elif self.level == "medium".lower():
            cpu_roll = random.randint(1,6)

        elif self.level == "hard".lower():
            cpu_roll = random.randint(1,10)
            if cpu_roll > 6:
                cpu_roll = 6

        if cpu_roll == 1:
            self.cpu_score = 0
            print(f"\nThe CPU rolled a {cpu_roll}! It loses all its points!")

        else:
            self.cpu_score += cpu_roll
            print(f"\nCPU rolled a {cpu_roll}. Its total score is {self.cpu_score}!")

    def cpu_hold(self):
<<<<<<< Updated upstream
        """
        Instructs the CPU to hold its current score and prints a message indicating the score.
        """
        print(f"\nCPU is holding. Current score of the CPU is {self.cpu_score}.")
        
=======
         """
        Causes the CPU to hold and end its turn.

        Returns:
            int: The final score for the CPU.
        """
         print(f"\nCpu is holding. Current score of the CPU is {self.cpu_score}.")
>>>>>>> Stashed changes
