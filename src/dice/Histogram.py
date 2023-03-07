class Histogram():
    
    def __init__(self, player):
        self.player_rolls = player
        self.rolls = []
            
    def set_rolls(self, added_rolls):
        self.rolls = added_rolls
            
    def add_roll(self, roll):
        self.rolls.append(roll)
            
    def show(self, rounds):
        print(f"Roll Distribution for {self.player_rolls}:")
        for i in range(1, 7):
            freq = self.rolls.count(i)
            print(f"Roll {i}: {'*' * freq}")


