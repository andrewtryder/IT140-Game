"""Unit tests for TextBasedGame.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from TextBasedGame import Room

# pylint: disable=C0301, C0103, W0612, W0613

class TestRoom(unittest.TestCase):
    """
    Unit tests for Room class
    """
    def setUp(self):
        self.start_room = Room("Start Room", "You are standing in a dusty old room. There is one door to the east.")
        self.foyer = Room("Foyer", "You're in a nice enterance hall.")
        self.start_room.add_exit("east", self.foyer)
        self.foyer.add_exit("west", self.start_room)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['go east'])
    def test_move(self, mock_input, mock_output):
        """ Tests that the player can move to a room that exists
        """
        next_room = self.start_room.move('east')
        self.assertIn(mock_output.getvalue().strip(), "You move east to Foyer.")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['north'])
    def test_move_no_exit(self, mock_input, mock_output):
        """Tests that the player cannot move to a room that does not exist
        """
        next_room = self.start_room.move('go north')
        self.assertIsNone(next_room)
        self.assertIn(mock_output.getvalue().strip(), "There is no exit in that direction.")

if __name__ == "__main__":
    unittest.main()
