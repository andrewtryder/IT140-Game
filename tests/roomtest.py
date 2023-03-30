import unittest
from unittest.mock import Mock

class RoomTest(unittest.TestCase):
    def setUp(self):
        self.room = Room("Test Room", "This is a test room.")
        self.other_room = Room("Other Room", "This is another test room.")

    def test_add_exit(self):
        self.room.add_exit("north", self.other_room)
        self.assertEqual(self.room.exits["north"], self.other_room)

    def test_get_exit(self):
        self.room.exits["east"] = self.other_room
        self.assertEqual(self.room.get_exit("east"), self.other_room)

    def test_add_item(self):
        self.room.add_item("test item")
        self.assertEqual(self.room.items, ["test item"])

    def test_remove_item(self):
        self.room.items = ["test item"]
        self.room.remove_item("test item")
        self.assertEqual(self.room.items, [])

    def test_move(self):
        self.room.exits["east"] = self.other_room
        self.assertEqual(self.room.move("east"), self.other_room)
        self.assertEqual(self.room.move("south"), None)

    def test_str(self):
        expected_output = "Test Room\n\nThis is a test room."
        self.assertEqual(str(self.room), expected_output)
