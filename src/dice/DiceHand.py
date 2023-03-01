import random


class handDice:

    def __init__(self, dice_faces, dice_face):
        self.dice_faces = dice_faces
        self.dice_face = dice_face

    def the_score(self):
        scor = 0
        keep_going = True
        while keep_going:
            x = input("Do you want to play (y/n): ")
            dice_hand = random.randint(self.dice_face, self.dice_faces)
            if x == 'y':
                scor += dice_hand
                print('you get ', dice_hand)

                if dice_hand == 1:
                    scor = 0
                print('Your scor is :', scor)
            else:
                keep_going = False
