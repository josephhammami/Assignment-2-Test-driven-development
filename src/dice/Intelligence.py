def __init__(self, level):
    self.level = level

def roll_again(self, score):
    if self.level == "easy":
        return True
    elif self.level == "medium":
        return score < 20
    elif self.level == "hard":
        return score < 25 and (score + self.roll_again(score + 6)) < 100
    else:
        raise ValueError(f"Invalid difficulty level: {self.level}")