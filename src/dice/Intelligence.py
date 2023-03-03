import random

class Intelligence:
    
    def __init__(self, level):
        self.level = level
        self.cpu_score = 0

    def cpu_rolling(self):
        
        if self.level == "easy".lower():
            cpu_roll = random.randint(1,3)
                        
        elif self.level == "medium".lower():
            cpu_roll = random.randint(1,6)
                
        elif self.level == "hard".lower():
            cpu_roll = random.randint(1,10)
            if cpu_roll > 6:
                cpu_roll = 6
        
        else:
            raise ValueError(f"Invalid difficulty level: {self.level}")    
        
        
        if cpu_roll == 1:
            self.cpu_score = 0
            print(f"The CPU rolled a {cpu_roll}! It loses all its points!")
            
        else:
            self.cpu_score += cpu_roll
            print(f"CPU rolled a {cpu_roll}. Its total score is {self.cpu_score}!") 
            
    def cpu_hold(self):
         print(f"Cpu is holding. Current score of the CPU is {self.cpu_score}.")