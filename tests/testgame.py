import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from unittest.mock import patch
from io import StringIO
from game import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.start_room = Room("Start Room", "You are standing in a dusty old room. There is one door to the east.")
        self.foyer = Room("Foyer", "You're in a nice enterance hall.")
        self.start_room.add_exit("east", self.foyer)
        self.foyer.add_exit("west", self.start_room)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['go east'])
    def test_move(self, mock_input, mock_output):
        next_room = self.start_room.move('east')
        self.assertIn(mock_output.getvalue().strip(), "You move east to Foyer.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['north'])
    def test_move_no_exit(self, mock_input, mock_output):
        next_room = self.start_room.move('go north')
        self.assertIsNone(next_room)
        self.assertIn(mock_output.getvalue().strip(), "There is no exit in that direction.")

if __name__ == "__main__":
    unittest.main()
