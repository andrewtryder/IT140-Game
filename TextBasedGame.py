"""
TextBasedGame.py
Andrew Ryder - IT140 - 2023
"""


# pylint: disable=C0301, C0103, R1705, R1723, R0912
class Room:
    """A class for creating rooms and objects in a text-based game.

    This is our Room class. It will be used to create room objects.
    Each room object will have a name, description, list of items, and a dictionary of exits.

    Attributes:
        name (str): The name of the room.
        description (str): A description of the room.
        items (list): A list of items in the room.
        exits (dict): A dictionary of exits from the room.

    Methods:
        add_exit(self, direction, room): Adds an exit to the room.
        get_exit(self, direction): Returns the room object that is in the specified direction.
        add_item(self, item): Adds an item to the room.
        remove_item(self, item): Removes an item from the room.
        move(self, direction): Moves the player to the room in the specified direction.
        __str__(self): Returns a string representation of the room.

    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}

    def add_exit(self, direction, room):
        """Add an exit to the room in the specified direction.

        Args:
            direction (str): The direction to add the exit in. Must be one of: "north", "south", "east", or "west".
            room (Room): The room object to add as an exit in the specified direction.
        """
        self.exits[direction] = room

    def get_exit(self, direction):
        """Get the room object that is in the specified direction.

        Args:
            direction (str): The direction to search for an exit in. Must be one of: "north", "south", "east", or "west".

        Returns:
            Room or None: The room object in the specified direction, or None if no exit is found.
        """
        return self.exits.get(direction)

    def add_item(self, item):
        """
        Remove an item from the room's inventory.

        Args:
            item (Item): The item to remove from the room's inventory.

        Returns:
            None.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Remove an item from the room's inventory.

        Args:
            item (Item): The item to remove from the room's inventory.

        Returns:
            None.
        """
        self.items.remove(item)

    def move(self, direction):
        """
        Move the player to the room in the specified direction.

        Args:
            direction (str): The direction to move in. Must be one of: "north", "south", "east", or "west".

        Returns:
            Room or None: If the direction is valid and there is a room in that direction, returns the room object in that direction. Otherwise, returns None.
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    def __str__(self):
        """
        returns a string representation of the room

        Returns:
            _type_: _description_
        """
        return self.name + '\n\n' + self.description


# Create room objects
start_room = Room("Start Room", "You are standing in a dusty old room. There is one door to the east.")
foyer = Room("Foyer", "You're in a nice enterance hall.")
main_hall = Room("Main Hall", "You enter the main hall with doors in every direction.")
library = Room("Library", "You enter a room filled with books. There are shelves lining the walls and a fireplace on the north wall.")
study = Room("Study", "You enter a small room with a desk and a bookshelf. The walls are lined with portraits.")
ballroom = Room("Ballroom", "You enter a grand ballroom with a chandelier hanging from the ceiling. The walls are lined with mirrors.")
kitchen = Room("Kitchen", "You enter a room with a stove, sink, and cabinets. There is a pile of dirty dishes in the sink.")
secret_passage = Room("Secret Passage", "You enter a hidden passage. It's dark and you can't see very far ahead.")
villain_room = Room("Villain's Room", "You enter a room with a large bed and a desk. The villain is standing in the corner.")

# Add exits to each room
start_room.add_exit("east", foyer)
foyer.add_exit("west", start_room)
foyer.add_exit("north", library)
foyer.add_exit("south", kitchen)
foyer.add_exit("east", main_hall)
library.add_exit("south", foyer)
library.add_exit("east", study)
study.add_exit("west", library)
study.add_exit("south", main_hall)
kitchen.add_exit("north", foyer)
kitchen.add_exit("east", study)
ballroom.add_exit("west", kitchen)
ballroom.add_exit("north", main_hall)
main_hall.add_exit("north", study)
main_hall.add_exit("west", foyer)
main_hall.add_exit("south", ballroom)
main_hall.add_exit("east", secret_passage)
secret_passage.add_exit("west", main_hall)
secret_passage.add_exit("east", villain_room)
villain_room.add_exit("west", secret_passage)

# Add items to each room
library.add_item("note")
study.add_item("photograph")
ballroom.add_item("diary")
foyer.add_item("knife")
kitchen.add_item("flashlight")
secret_passage.add_item("key")


def mainloop():  # pragma: no cover
    """This is the main game loop. It will run until the player wins or loses the game."""
    
    # Set the starting room and initialize the game state
    current_room = start_room
    inventory = []
    # our big boy loop for the game.
    while True:
        # Print the current room description and available exits
        print(current_room)
        print('Exits:', list(current_room.exits.keys()))

        # Check if the player has won or lost the game
        if current_room == villain_room and set(inventory) == {'key', 'flashlight', 'note', 'photograph', 'knife', 'diary'}:
            print('Congratulations, you solved the murder mystery and caught the villain!')
            break

        if current_room == villain_room:
            print('Game over. The villain caught you.')
            break

        # Prompt the player to enter a command
        command = input('What do you want to do? ').lower()

        # Handle movement commands
        if command in current_room.exits:
            current_room = current_room.get_exit(command)
        elif command.startswith('go '):
            direction = command.split(' ')[1]
            if direction in current_room.exits:
                current_room = current_room.get_exit(direction)
            else:
                print("You can't go that way.")

        # Handle item interaction commands
        elif command.startswith('get '):
            item = command.split(' ')[1]
            if item in current_room.items:
                current_room.remove_item(item)
                inventory.append(item)
                print(f'You picked up the {item}.')
            else:
                print('That item is not in this room.')
        # Handle other commands
        elif command == 'inventory':
            print('You are carrying:', inventory)
        elif command == 'help':
            print(
                'Commands: go [direction], get [item], use [item], inventory, help, quit')
        elif command == 'quit':
            print('Thanks for playing!')
            break
        else:
            print('Invalid command. Type "help" for a list of commands.')


if __name__ == "__main__":
    mainloop()
