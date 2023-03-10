"""
Dice is imported into DiceHand so the dice rolls can be registered.

for the player who rolled the die.
"""

from dice import Dice


class DiceHand:
    """
    This class will keep track of the player score.

    and their actions throughout the game.
    """

    def __init__(self):
        """
        Initialize a DiceHand object with.

        a player score of 0 and a dice object.
        """
        self.player_score = 0
        self.dice = Dice()

    def set_player_score(self, new_player_score):
        """Set the player's score to the given new score."""
        self.player_score = new_player_score

    def roll_dice(self, player):
        """Get the rolls the dice for the given player and update score."""
        player_roll = self.dice.roll()

        if player_roll == 1:
            self.player_score = 0
<<<<<<< HEAD
            print(f"\nUhoh {player} rolled a {player_roll}! "
                  "They lose all their points!")

        else:
            self.player_score += player_roll
            print(f"{player} rolled a {player_roll}. Their total score "
                  f"is {self.player_score}!")
=======
            print(
                f"\nUhoh {player} rolled a {self.player_roll}! They lose all their points!"
            )

        else:
            self.player_score += self.player_roll
            print(
                f"{player} rolled a {self.player_roll}. Their total score is {self.player_score}!"
            )
>>>>>>> 910bbded5f98bbc9bb53068b342410c4de296c9a

    def hold(self, player):
        """Do this to allows the given player to hold and keep their score."""
        print(f"{player} is holding. "
              f"Their current score is {self.player_score}.")
