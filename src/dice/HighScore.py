"""
This class will hold the high score of the player through their various games with the CPU.
"""

class HighScore():
    """
    A class representing the high score table for our dice game.
    """

    def __init__(self):
        """
        Constructs a new high score object.
        """
        self.scores = []


    def add_score(self,score):
        """
        Adds a new record to the high score table.
        """
        self.scores.append(score)


    def get_high_score(self):
        """
        Returns the best record from the high score table.
        """
        return min(self.scores)
    