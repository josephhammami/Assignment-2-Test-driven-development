import random

class Intelligence:
    
    def __init__(self, level):
        self.level = level
        self.cpu_score = 0
        
    def set_level(self, new_level):
        self.level = new_level

    def cpu_rolling(self):
        
        if self.level == "easy".lower():
            cpu_roll = random.randint(1,3)
                        
        elif self.level == "medium".lower():
            cpu_roll = random.randint(1,6)
                
        elif self.level == "hard".lower():
            cpu_roll = random.randint(1,10)
            if cpu_roll > 6:
                cpu_roll = 6  
    
        if cpu_roll == 1:
            self.cpu_score = 0
            print(f"\nThe CPU rolled a {cpu_roll}! It loses all its points!")
            
        else:
            self.cpu_score += cpu_roll
            print(f"\nCPU rolled a {cpu_roll}. Its total score is {self.cpu_score}!") 
            
    def cpu_hold(self):
         print(f"\nCPU is holding. Current score of the CPU is {self.cpu_score}.")