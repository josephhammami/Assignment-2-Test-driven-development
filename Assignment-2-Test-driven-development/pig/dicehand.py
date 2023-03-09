"""
Dice is imported into DiceHand so the dice rolls can be registered for the player 
who rolled the die.
"""
from dice import Dice

class DiceHand:
    """
    This class will keep track of the player score
    and their actions throughout the game.
    """

    def __init__(self):
        """
        Initializes a DiceHand object with
        a player_score of 0 and a dice object.
        """
        self.player_score = 0
        self.dice = Dice()

    def set_player_score(self, new_player_score):
        """
        Sets the player's score to the given new score.
        """
        self.player_score = new_player_score

    def roll_dice(self, player):
        """
        Rolls the dice for the given player
        and updates their score accordingly.
        """
        self.player_roll = self.dice.roll()

        if self.player_roll == 1:
            self.player_score = 0
            print(f"\nUhoh {player} rolled a {self.player_roll}! They lose all their points!")

        else:
            self.player_score += self.player_roll
            print(f"{player} rolled a {self.player_roll}. Their total score is {self.player_score}!")

    def hold(self, player):
        """
        Allows the given player to hold and keep their current score.
        """
        print(f"{player} is holding. Their current score is {self.player_score}.")
