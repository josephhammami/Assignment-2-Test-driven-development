from Dice import dice

class DiceHand:
    
    def __init__(self):
        self.roll_result = None
        
    def roll_dice(self):
        Dice = dice()
        self.roll_result = Dice.roll()
        
hand = DiceHand()
hand.roll_dice()
print(hand.roll_result) 