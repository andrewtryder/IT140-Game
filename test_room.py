"""Unit tests for the Room class."""

import unittest
from TextBasedGame import Room


class TestRoom(unittest.TestCase):
    """
    
    Unit tests for the Room class.
    """
    def setUp(self):
        """
        set up a room for testing.
        """
        self.room = Room("Test Room", "This is a test room.")

    def test_init(self):
        """
        Tests that the room is initialized correctly.
        """
        self.assertEqual(self.room.name, "Test Room")
        self.assertEqual(self.room.description, "This is a test room.")
        self.assertEqual(self.room.items, [])
        self.assertEqual(self.room.exits, {})

    def test_add_exit(self):
        """
        Tests that exits are added correctly.
        """
        self.room.add_exit("north", Room("North Room", "This is a room to the north."))
        self.assertEqual(len(self.room.exits), 1)
        self.assertIsNotNone(self.room.get_exit("north"))
        self.assertIsNone(self.room.get_exit("south"))

    def test_add_item(self):
        """
        Tests that items are added correctly.
        """
        self.room.add_item("test item")
        self.assertEqual(len(self.room.items), 1)
        self.assertIn("test item", self.room.items)

    def test_remove_item(self):
        """
        Tests that items are removed correctly.
        """
        self.room.add_item("test item")
        self.room.remove_item("test item")
        self.assertEqual(len(self.room.items), 0)
        self.assertNotIn("test item", self.room.items)

    def test_move(self):
        """
        Tests that the player can move to a room that exists.
        """
        north_room = Room("North Room", "This is a room to the north.")
        self.room.add_exit("north", north_room)
        self.assertEqual(self.room.move("north"), north_room)
        self.assertIsNone(self.room.move("south"))


if __name__ == "__main__":
    unittest.main()
