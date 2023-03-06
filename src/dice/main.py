"""
The game module will import the Game class which has the core functionality of the gameplay 
of our dice game and it also has all the other classes imported to it.
"""
from Game import Game

def main():
    """
    The game will run an instance of the Game class which will in turn run our game.
    """
    new_game = Game()
    new_game.setup_game()

if __name__ == "__main__":
    main()
