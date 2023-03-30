import random

# Define the rooms in the mansion
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def move(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    def __str__(self):
        return self.name + '\n\n' + self.description

# Create room objects
start_room = Room("Start Room", "You are standing in a dusty old room. There is one door to the east.")
foyer = Room("Foyer", "You're in a nice enterance hall.")
main_hall = Room("Main Hall", "You enter the main hall with doors in every direction.")
library = Room("Library", "You enter a room filled with books. There are shelves lining the walls and a fireplace on the north wall.")
study = Room("Study", "You enter a small room with a desk and a bookshelf. The walls are lined with portraits.")
ballroom = Room("Ballroom", "You enter a grand ballroom with a chandelier hanging from the ceiling. The walls are lined with mirrors.")
dining_room = Room("Dining Room", "You enter a room with a large dining table and chairs. The walls are lined with paintings.")
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

# Set the starting room and initialize the game state
current_room = start_room
inventory = []

# Define the game loop
while True:
    # Print the current room description and available exits
    print(current_room)
    print('Exits:', list(current_room.exits.keys()))

    # Check if the player has won or lost the game
    if current_room == villain_room and set(inventory) == set(['key', 'flashlight', 'note', 'photograph', 'knife', 'diary']):
        print('Congratulations, you solved the murder mystery and caught the villain!')
        break
    elif current_room == villain_room:
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
            print('You can\'t go that way.')
    
    # Handle item interaction commands
    elif command.startswith('get '):
        item = command.split(' ')[1]
        if item in current_room.items:
            current_room.remove_item(item)
            inventory.append(item)
            print(f'You picked up the {item}.')
        else:
            print('That item is not in this room.')
    elif command.startswith('use '):
        item = command.split(' ')[1]
        if item == 'flashlight':
            if current_room == kitchen:
                print('The flashlight reveals a key hidden under a pile of dirty dishes.')
                kitchen.add_item('key')
            else:
                print('You don\'t see anything useful.')
        elif item == 'knife':
            if current_room == dining_room:
                print('You use the knife to cut open the upholstery on the dining room chairs, but find nothing of interest.')
            else:
                print('You can\'t use that here.')
        elif item == 'key':
            if current_room == villain_room:
                print('You use the key to unlock the door to the villain\'s room.')
                villain_room.add_item('villain')
            else:
                print('You can\'t use that here.')
        else:
            print('You can\'t use that here.')
    
    # Handle other commands
    elif command == 'inventory':
        print('You are carrying:', inventory)
    elif command == 'help':
        print('Commands: go [direction], get [item], use [item], inventory, help, quit')
    elif command == 'quit':
        print('Thanks for playing!')
        break
    else:
        print('Invalid command. Type "help" for a list of commands.')

       
