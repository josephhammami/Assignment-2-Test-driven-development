"""
The game module will import the Shell Class which has the command line interface that will1
display gameplay of our dice game and it also has access to our other classes.
"""
from shell import Shell

def main():
    """
    The game will run an instance of the Shell class which will in turn run our game.
    """
    Shell().cmdloop()


if __name__ == "__main__":
    main()
