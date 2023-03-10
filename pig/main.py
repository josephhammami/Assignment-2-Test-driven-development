"""We import the Shell module which has the command line interface."""
from shell import Shell


def main():
    """Run Shell class instance to execute game with this method."""
    Shell().cmdloop()


if __name__ == "__main__":
    main()
