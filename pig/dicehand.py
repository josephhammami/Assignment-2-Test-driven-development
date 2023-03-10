"""Import Dice into DiceHand to register player's die rolls."""
from dice import Dice


class DiceHand:
    """Track player score and actions throughout the game using this class."""

    def __init__(self):
        """Initialize DiceHand object with player_score 0 and dice object."""
        self.player_score = 0
        self.dice = Dice()

    def set_player_score(self, new_player_score):
        """Set player's score to given new score using this method."""
        self.player_score = new_player_score

    def roll_dice(self, player):
        """Roll dice for given player and update their score in this method."""
        self.player_roll = self.dice.roll()

        if self.player_roll == 1:
            self.player_score = 0
            print(
                f"\nUhoh {player} rolled a {self.player_roll}! They lose all their points!"
            )

        else:
            self.player_score += self.player_roll
            print(
                f"{player} rolled a {self.player_roll}. Their total score is {self.player_score}!"
            )

    def hold(self, player):
        """Allow the player to hold current score in this method."""
        print(f"{player} is holding. Their current score is {self.player_score}.")
