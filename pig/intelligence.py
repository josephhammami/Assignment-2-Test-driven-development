"""
Random is imported to decide what the CPU rolls on the die.
"""
import random


class Intelligence:
    """
    This class will hold the core functionalities for the CPU in our dice game.
    """

    def __init__(self, level):
        """
        Initializes an Intelligence object with the given level and a CPU score of 0.
        """
        self.level = level
        self.cpu_score = 0

    def set_level(self, new_level):
        """
        Updates the level of difficulty for the CPU.
        """
        self.level = new_level

    def cpu_rolling(self):
        """
        Stimulates the CPU rolling the dice based on the current level of difficulty.
        Updates the CPU score and prints a message indicating the result of the roll.
        """

        if self.level == "easy".lower():
            cpu_roll = random.randint(1, 3)

        elif self.level == "medium".lower():
            cpu_roll = random.randint(1, 6)
            if self.cpu_score + cpu_roll > 6:
                cpu_roll = 6 - self.cpu_score

        elif self.level == "hard".lower():
            cpu_roll = random.randint(1, 10)
            if cpu_roll > 6:
                cpu_roll = 6
            if self.cpu_score + cpu_roll > 6:
                cpu_roll = 6 - self.cpu_score

        if cpu_roll == 1:
            self.cpu_score = 0
            print(f"\nThe CPU rolled a {cpu_roll}! It loses all its points!")

        else:
            self.cpu_score += cpu_roll
            print(f"\nCPU rolled a {cpu_roll}. Its total score is {self.cpu_score}!")

    def cpu_hold(self):
        """
        Instructs the CPU to hold its current score and prints a message indicating the score.
        """
        print(f"\nCPU is holding. Current score of the CPU is {self.cpu_score}.")
