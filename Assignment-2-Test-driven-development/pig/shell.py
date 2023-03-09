"""
The cmd module allows use to create an interactive environment inside the command line. 
The Game class holds the core functionalities of our game and is implemented to run
the different methods through our shell interface.
"""
import cmd
from game import Game


class Shell(cmd.Cmd):
    """
    The main command line interface for our Pig Game.
    """
    intro = "Welcome to the Pig game! Type '?' for gameplay options.\n1. Start a new game\n2. Quit\n"
    new_game =  "1. Start a new game"
    quit_game = "2. Quit"
    prompt = ">> "

    def __init__(self):
        """
        Initializes a new instance of the Shell class with an instance of the Game class.
        """
        super().__init__()
        self.game = Game(None, None, None)

    def default(self, line):
        self.do_notify(line)

    def do_help(self, arg):
        """
        Calls the print_info method that displays information about the different keybinds.
        """
        self.print_info()

    def do_1(self, arg):
        """
        Starts a new game by calling the setup_game method of the Game Class.
        """
        self.game.setup_game()

    def do_2(self, arg):
        """
        Quits the game from the command line interface.
        """
        return self.quit()

    def print_info(self):
        """
        Displays keybinds the user can use during the game.
        """
        #Cheating is now allowed against other players
        print("\n+-------------------------------------------------+")
        print("|                  Information                    |")
        print("+-------------------------------------------------+")
        print("|     (MAY ONLY BE USED DURING ACTIVE GAME)       |")
        print("+-------------------------------------------------+")
        print("| \u2022 The game will now begin!                      |")
        print("| \u2022 To roll press 'r'                             |")
        print("| \u2022 To hold press 'h'                             |")
        print("| \u2022 If you wish to alter the difficulty press 'd' |")
        print("| \u2022 If you wish to change your name, press 'n'    |")
        print("| \u2022 To restart the game, press 'g'                |")
        print("| \u2022 To cheat, press 'c' (singleplayer)            |")
        print("| \u2022 To exit the game, press 'e'                   |")
        print("+-------------------------------------------------+")
        print("\nInitial highscore will be added when first ever game is played.")

    def do_notify(self, arg):
        """
        Displays an error message to the user if invalid input has been entered.
        """
        print("Invalid input, type '?' for gameplay options.")

    def quit(self):
        """
        The method that terminates the program from the command line interface.
        """
        print("Thanks for playing our game!")
        exit()

if __name__ == "__main__":
    shell = Shell()
    shell.cmdloop()
