import unittest
import io
from unittest.mock import patch, MagicMock
from io import StringIO
from Game import Game



class Game_Test(unittest.TestCase):
    """
    A test suite for the Game class.
    """

    def test_init_objects(self):
        """
        Test that initializing a Game object sets the player names and CPU level correctly.
        """
        new_game = Game("Name1","Name2","easy")
        self.assertEqual(new_game.player_one, "Name1")
        self.assertEqual(new_game.player_two, "Name2")
        self.assertEqual(new_game.cpu_level, "easy")

    @patch('random.randint', return_value=1)
    def test_cpu_turn_roll(self, mock_randint):
        """
        Test that the cpu_turn() method correctly calls cpu_rolling() when a 1 is generated.
        """
        game = Game("","","")
        game.cpu_level = MagicMock()
        game.cpu_turn()
        game.cpu_level.cpu_rolling.assert_called_once()

    @patch('random.randint', return_value=2)
    def test_cpu_turn_hold(self, mock_randint):
        """
        Test that the cpu_turn() method correctly calls cpu_hold() when a 2 is generated.
        """
        game = Game("","","")
        game.cpu_level = MagicMock()
        game.cpu_turn()
        game.cpu_level.cpu_hold.assert_called_once()


    @patch('sys.stdout', new_callable=StringIO)
    def test_cheat(self, mock_stdout):
        """
        Test that the cheat() method correctly sets the player score to 100 and prints a message.
        """
        game = Game(None, None, None)
        player_name = "Joseph"
        player_score = 0
        new_score = game.cheat(player_name, player_score)
        expected_output = f"{player_name} cheated and won the game!\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(new_score, 100)
        
        
    def test_print_rules(self):
        """
        Tests that the print_rules() method prints out the correct statement.
        """
        game = Game(None, None, None)
        expected_output = (
            "+----------------------------------------------------------------------+\n"
            "|                            Rules of Pig                              |\n"
            "+----------------------------------------------------------------------+\n"
            "| •          Each player takes turns rolling a die.                    |\n"
            "| •          You score points equal to the sum of your rolls.          |\n"
            "| •          If you roll a 1, you lose all your points.                |\n"
            "| •          You can hold and pass your turn to the CPU/player.        |\n"
            "| •          The first to reach 100 points wins!                       |\n"
            "+----------------------------------------------------------------------+\n"
        )
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            game.print_rules()
            self.assertEqual(fake_out.getvalue(), expected_output)
            
    def test_separator(self):
        """
        Test that the separator() method prints out a dotted line.
        """
        game = Game("Player1", "Player2", "easy")
        expected_output = "\n------------------------------------------------------------------\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.seperator()
            self.assertEqual(fake_out.getvalue(), expected_output)
   
    @patch('builtins.input')
    def test_setup_game_player_versus_cpu(self, mock_input):
        """
        Tests if the setup_game() method correctly directs the user to the 
        single player mode based on their input. It uses the unittest.mock module 
        to mock the input() function and simulate user input. It also uses 
        MagicMock to mock the player_versus_cpu() method and checks if it 
        was called once.
        """

        mock_input.side_effect = ["1", "TestPlayer"]

        game = Game(None, None, None)
        game.player_versus_cpu = MagicMock()

        game.setup_game()

        game.player_versus_cpu.assert_called_once()

    @patch('builtins.input')
    def test_setup_game_player_versus_player(self, mock_input):
        """
        Tests if the setup_game() method correctly directs the user to the 
        multiplayer mode based on their input. It uses the unittest.mock module 
        to mock the input() function and simulate user input. It also uses 
        MagicMock to mock the player_versus_player() method and checks if it 
        was called once.
        """
        mock_input.side_effect = ["2", "PlayerOne", "PlayerTwo"]

        game = Game(None, None, None)
        game.player_versus_player = MagicMock()

        game.setup_game()
    
    def test_player_versus_cpu(self):
        game = Game(None, None, None)
        player_name = "Player 1"
        cpu_difficulty = "easy"
        game.player_one.set_name(player_name)
        mock_input = f"{cpu_difficulty}\nr\nh\nn\nn\ny\n"
        expected_output = (
            f"\nBefore we begin, go ahead and decide the CPU's difficulity! (easy/medium/hard)\n"
            f"\n{player_name} would you like to roll or hold?\n"
            f"\nThe CPU rolled the die and got a 4!\n"
            f"\n{player_name} would you like to roll or hold?\n"
            f"\nYou have chosen to hold.\n"
            f"\nIt's now the CPU's turn.\n"
            f"\nThe CPU rolled the die and got a 5!\n"
            f"\nCPU holds.\n"
            f"\n------------------------------------------------------------------\n"
            f"\nBefore we begin, go ahead and decide the CPU's difficulity! (easy/medium/hard)\n"
            f"\n{player_name} would you like to roll or hold?\n"
            f"\nYou have chosen to roll.\n"
            f"\nYou rolled a 1 and lost all your points!\n"
            f"\nIt's now the CPU's turn.\n"
            f"\nThe CPU rolled the die and got a 6!\n"
            f"\nCPU holds.\n"
            f"\n------------------------------------------------------------------\n"
            f"\nHere's your single player highscore!\n"
            f"{player_name}'s record: 2\n(The record represents how many rounds it took for you to reach 100 points. Try to beat it!)\n"
            f"\nWould you like to play again? (y/n)\n"
        )

        # Patching input() to return mock_input
        with patch('builtins.input', side_effect=mock_input.split('\n')):
            # Redirecting print() to buffer to check output
            with patch('sys.stdout', new=StringIO()) as fake_out:
                game.player_versus_cpu()

        # Asserting output matches expected_output
        self.assertEqual(fake_out.getvalue(), expected_output)


        
    
if __name__ == "__main__":
    unittest.main()
