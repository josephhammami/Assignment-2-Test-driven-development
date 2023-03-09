"""The cmd module allows use to create an interactive environment."""
import cmd
from game import Game


class Shell(cmd.Cmd):
    """The main command line interface for our Pig Game."""

    intro = "Welcome to the Pig game! Type '?' for gameplay options.\n1. Start a new game\n2. Quit\n"
    new_game = "1. Start a new game"
    quit_game = "2. Quit"
    prompt = ">> "

    def __init__(self):
        """Initialize a new instance of the Shell and Game class using this method."""
        super().__init__()
        self.game = Game(None, None, None)

    def default(self, line):
        """Pass the given line to the 'do_notify' method to default behavior of shell with this method."""
        self.do_notify(line)

    def do_help(self, arg):
        """Display information by calling the 'print_info' method with this method."""
        self.print_info()

    def do_1(self, arg):
        """Start a new game by calling the 'setup_game' method of the Game Class using this method."""
        self.game.setup_game()

    def do_2(self, arg):
        """Quits the game from the command line interface with this method."""
        return self.quit()

    def print_info(self):
        """Display the keybinds that the user can use during the game using this method."""
        # Cheating is now allowed against other players
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
        """Display an error message to the user if an invalid input is provided with this method."""
        print("Invalid input, type '?' for gameplay options.")

    def quit(self):
        """Terminates the program from the command line interface witb this method."""
        print("Thanks for playing our game!")
        exit()


if __name__ == "__main__":
    shell = Shell()
    shell.cmdloop()
