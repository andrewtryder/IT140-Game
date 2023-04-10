# Andrew Ryder
# IT140 - ModuleSixMilestone.py

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
}

#initialize current room to Great Hall
current_room = 'Great Hall'

#Gameplay loop
while current_room != 'exit':
    #display current room
    print('You are currently in the', current_room)
    
    #ask for user input
    direction = input('Which direction do you want to go? (North, South, East, West, or exit) ')
    
    #handle user input
    if direction == 'exit':
        #end game if player enters "exit"
        current_room = 'exit'
        print('Thanks for playing!')
    elif direction in rooms[current_room]:
        #move player to new room if direction is valid
        current_room = rooms[current_room][direction]
        print('You have moved', direction, 'to the', current_room)
    else:
        #invalid input, ask again
        print('Invalid direction, please try again.')
