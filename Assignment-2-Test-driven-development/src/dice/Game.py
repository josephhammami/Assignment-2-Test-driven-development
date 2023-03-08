"""
These modules come from the different classes we are are using to 
simplement different functionalities to our pig game.
"""
import random
from Player import Player
from HighScore import HighScore
from Intelligence import Intelligence
from DiceHand import DiceHand


class Game():
    """
    This class holds the core functionalities of our dice game.
    """

    def __init__(self, player_one, player_two, cpu_level):
        """
        Constructs objects from the classes: "Player" and "Intelligence".
        """

        self.player_one = player_one
        self.player_two = player_two
        self.cpu_level = cpu_level

    def print_rules(self):
        """
        Prints out the rules for our dice game.
        """
        print("+----------------------------------------------------------------------+")
        print("|                            Rules of Pig                              |")
        print("+----------------------------------------------------------------------+")
        print("| \u2022          Each player takes turns rolling a die.                    |")
        print("| \u2022          You score points equal to the sum of your rolls.          |")
        print("| \u2022          If you roll a 1, you lose all your points.                |")
        print("| \u2022          You can hold and pass your turn to the CPU/player.        |")
        print("| \u2022          The first to reach 100 points wins!                       |")
        print("+----------------------------------------------------------------------+")

    def setup_game(self):
        """
        This method is a setup before the actual game starts. 
        It will create two player objects where the users can select their name/s.
        """
        self.player_one = Player("")
        self.player_two = Player("")

        self.print_rules()

        print("\nAre you playing against the CPU or a friend? (1 or 2 respectively)")
        option = input(">> ")

        if option == "1":
            print("\nGo ahead and enter your name!")
            self.player_one.choose_name()
            self.player_versus_cpu()

        elif option == "2":
            print("Go ahead and choose your names!")

            print("\nPlayer 1:")
            self.player_one.choose_name()

            print("\nPlayer 2:")
            self.player_two.choose_name()

            self.player_versus_player()

        else:
            print("Please enter a valid input!")

    def player_versus_cpu(self):
        """
        This method runs the single player game mode against the CPU 
        where the player can choose the difficulty of the CPU.
        """
        player_turn = DiceHand()
        player_score_holder = HighScore(0, 0, 0)
        player_rounds = 0

        while True:

            while True:
                print("\nBefore we begin, go ahead and decide the CPU's difficulity! (easy/medium/hard)")
                cpu_difficulty = input(">> ")

                if cpu_difficulty.lower() in ["easy", "medium", "hard"]:
                    self.cpu_level = Intelligence(cpu_difficulty)
                    break

                else:
                    print("\nPlease enter a valid diffiulty level!")
                    continue

            while True:
                print(f"\n{self.player_one.get_name()} would you like to roll or hold?")
                action = input(">> ")

                if action.lower() == "r":
                    player_turn.roll_dice(self.player_one.get_name())
                    player_rounds += 1

                    if player_turn.player_score >= 100:
                        print("Congrats! You won!")
                        player_score_holder.add_record_player_one_singeplayer(player_rounds)
                        break

                    self.cpu_turn()

                    if self.cpu_level.cpu_score >= 100:
                        print("The CPU wins!")
                        player_score_holder.add_record_player_one(player_rounds)
                        break

                elif action.lower() == "h":
                    player_turn.hold(self.player_one.get_name())
                    player_rounds += 1
                    self.seperator()
                    self.cpu_turn()

                elif action.lower() == "d":
                    print("\nWhat would you like to change the difficulty to?")
                    alter_difficulty = input(">> ")
                    self.cpu_level.set_level(alter_difficulty)
                    self.seperator()

                elif action.lower() == "n":
                    print("\nWhat would you like to change your new name to?")
                    self.player_one.change_name()
                    self.seperator()

                elif action.lower() == "c":
                    self.cheat(self.player_one.get_name(), player_turn.player_score)
                    break

                elif action.lower() == "e":
                    break

                else:
                    print("\nPlease enter a valid input!")

            while True:
                print("\nHere's your single player highscore!")
                player_score_holder.print_highscore_singleplayer(self.player_one.get_name(), player_score_holder.get_record_player_one_singleplayer())
                print("(The record represents how many rounds it took for you to reach 100 points. Try to beat it!)")

                print("\nWould you like to play again? (y/n)")
                choice = input(">> ")

                if choice.lower() == "n":
                    print("Thanks for playing our game!")
                    exit()

                elif choice.lower() == "y":
                    player_turn.set_player_score(0)
                    break

                else:
                    print("Please enter a valid input!")

    def cpu_turn(self):
        """
        This method takes care of the CPU's turn.
        """
        self.seperator()
        cpu_hold = random.randint(1, 2)

        if cpu_hold == 1:
            self.cpu_level.cpu_rolling()

        else:
            self.cpu_level.cpu_hold()

    def player_versus_player(self):
        """
        This method runs the multiplayer mode against another player
        where they play to 100 points.
        """
        player_one_turn = DiceHand()
        player_two_turn = DiceHand()
        player_one_score_holder = HighScore(0, 0, 0)
        player_two_score_holder = HighScore(0, 0, 0)
        player_one_rounds = 0
        player_two_rounds = 0
        while True:

            while True:

                print(f"{self.player_one.get_name()} would you like to roll or hold?")
                action_player_one = input(">> ")
                self.seperator()

                if action_player_one.lower() == "r":
                    player_one_turn.roll_dice(self.player_one.get_name())
                    self.seperator()
                    player_one_rounds += 1


                    if player_one_turn.player_score >= 100:
                        print(f"{self.player_one.get_name()} won!")
                        player_one_score_holder.add_record_player_one(player_one_rounds)
                        break

                    print(f"{self.player_two.get_name()} would you like to roll or hold?")
                    action_player_two = input(">> ")
                    self.seperator()

                    if action_player_two.lower() == "r":
                        player_two_turn.roll_dice(self.player_two.get_name())
                        self.seperator()
                        player_two_rounds += 1

                        if player_two_turn.player_score >= 100:
                            print(f"{self.player_two.get_name()} won!")
                            player_two_score_holder.add_record_player_two(player_two_rounds)
                            break

                    elif action_player_two.lower() == "h":
                        player_two_turn.hold(self.player_two.get_name())
                        self.seperator()
                        player_two_rounds += 1

                    elif action_player_two.lower() == "n":
                        print(f"\n {self.player_two.get_name()} what would you like to change your new name to?")
                        self.player_two.change_name()
                        self.seperator()

                    elif action_player_two.lower() == "e":
                        break

                    else:
                        print("\nPlease enter a valid input!")

                elif action_player_one.lower() == "h":
                    player_one_turn.hold(self.player_one.get_name())
                    self.seperator()
                    player_one_rounds += 1

                elif action_player_one.lower() == "n":
                    print(f"\n {self.player_one.get_name()} what would you like to change your new name to?")
                    self.player_one.change_name()
                    self.seperator()

                elif action_player_one.lower() == "e":
                    break

                else:
                    print("Please enter a valid input!")

            while True:
                print("\nHere's your multiplayer highscore!")
                player_one_score_holder.print_highscore_multiplayer(self.player_one.get_name(), self.player_two.get_name(), player_one_score_holder.get_record_player_one(), player_two_score_holder.get_record_player_two())
                print("(The record represents how many rounds it took for you to reach 100 points. Try to beat it!)")

                print("\nWould you like to play again? (y/n)")
                choice = input(">> ")

                if choice.lower() == "y":
                    player_one_turn.set_player_score(0)
                    player_two_turn.set_player_score(0)
                    break

                elif choice.lower() == "n":
                    print("Thanks for playing our game!")
                    exit()

                else:
                    print("Please enter a valid input!")

    def cheat(self, player_name, player_score):
        """
        This method implements the cheating functionality which
        automatically gives the player 100 points and ends the game.
        """
        player_score = 100
        print(f"{player_name} cheated and won the game!")
        return player_score

    def seperator(self):
        """
        This method simply prints a dotted line that separates the different
        players actions throughout the game.
        """
        print("\n------------------------------------------------------------------")
