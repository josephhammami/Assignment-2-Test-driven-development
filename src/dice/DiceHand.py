from Dice import dice

class DiceHand:
    
    def __init__(self):
        self.player_score = 0
        self.dice = dice()
    
    def roll_dice(self, player):
        
        player_roll = self.dice.roll()
        
        if player_roll == 1:
            self.player_score = 0
            print(f"\nUhoh {player} rolled a {player_roll}! They lose all their points!")
        
            
        else:
            self.player_score += player_roll
            print(f"{player} rolled a {player_roll}. Their total score is {self.player_score}!")
        
    
    def hold(self, player):
       
        print(f"\n{player} is holding. Their current score is {self.player_score}.")