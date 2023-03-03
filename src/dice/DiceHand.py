from Dice import dice

class DiceHand:
    
    def __init__(self):
        self.roll_result = None
        
    def roll_dice(self):
        score = 0
        Dice = dice()
        score += Dice.roll()
        print(f"Your current roll is {Dice.roll()}")
        print(f"Your total roll is {score}")         
        
roll = DiceHand()
roll.roll_dice()