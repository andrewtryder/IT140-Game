"""ModuleSixMilestone.py
Andrew Ryder
"""

# disable warning about pylint not liking the file name.
# pylint: disable-msg=C0103

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
}

# initialize current room to Great Hall
CURRENT_ROOM = 'Great Hall'

# Gameplay loop
while CURRENT_ROOM != 'exit':
    # display current room
    print('You are currently in the', CURRENT_ROOM)

    # ask for user input
    direction = input('Which direction do you want to go? (North, South, East, West, or exit) ')

    # handle user input
    if direction == 'exit':
        # end game if player enters "exit"
        CURRENT_ROOM = 'exit'
        print('Thanks for playing!')
    elif direction in rooms[CURRENT_ROOM]:
        # move player to new room if direction is valid
        CURRENT_ROOM = rooms[CURRENT_ROOM][direction]
        print('You have moved', direction, 'to the', CURRENT_ROOM)
    else:
        # invalid input, ask again
        print('Invalid direction, please try again.')
