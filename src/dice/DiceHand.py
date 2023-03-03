from Dice import dice

class DiceHand:
    
    def __init__(self):
        self.player_score = 0
        self.dice = dice()
    
    def roll_dice(self):
    
        player_roll = self.dice.roll()
        
        if player_roll == 1:
            self.player_score = 0
            print(f"Uhoh you rolled a {player_roll}! You lose all your points!")
        
            
        else:
            self.player_score += player_roll
            print(f"You rolled a {player_roll}. Your total score is {self.player_score}!")
        
    
    def hold(self):
       
        print(f"You're holding. Your current score is {self.player_score}.")