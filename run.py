# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from math import sqrt
from random import randint

# Creating constant variables for setting the grid size
ROOM_WIDTH = 10
ROOM_HEIGHT = 10

# Asking the player for a name to display the welcome message and use it later in a f string
player_name = input("What's your name? ")
print(f"Hello {player_name}!")

# Creating the function for the game
def play_game():
    # Setting a random key position using randint
    key_position_x = randint(0, ROOM_WIDTH)
    key_position_y = randint(0, ROOM_HEIGHT)

    player_position_x = 0
    player_position_y = 0
    key_is_found = False
    steps = 0

    # Printing rules og the game to the terminal 
    print("Your task is to find the key in a dark square room.\nYou start in the bottom left corner.\nDepending on how close to the key you are, you will see either 'Warmer' or 'Cold' message.")
 
    # Creating 1st variable needed for calculating the distance between the player and the key
    # Variable needed for printing 'Warmer' or 'Cold' message
    distance_before_steps = sqrt((key_position_x - player_position_x) ** 2 + (key_position_y - player_position_y) ** 2)
    
    # Steps in the game while the player is looking for the key:
    while not key_is_found:
        steps += 1
        print("")
        print("You can choose to go left [A], right [D], up [W] or down [S]: ")

        player_move = input(f"What's your move? ")
        
        # Making sure that the player doesn't go outside the grid by displaying appropriate message
        if player_move == "a":
            player_position_x -= 1
            if player_position_x < 0:
                print("You hit the wall!!")
        elif player_move == "d":
            player_position_x += 1
            if player_position_x > ROOM_WIDTH:
                print("You hit the wall!!")
        elif player_move == "w":
            player_position_y += 1
            if player_position_y > ROOM_HEIGHT:
                print("You hit the wall!!")
        elif player_move == "s":
            player_position_y -= 1
            if player_position_y < 0:
                print("You hit the wall!!")
        else:
            # Message displayed in case of using keys other than movement keys: [W, S, A, D]
            print("Incorrect move, try again!")

        # If statement printing appropriate message in case of a player finding the key
        # Giving the option to continue the game or to quit
        if player_position_x == key_position_x and player_position_y == key_position_y:
            print(f"Congratulations {player_name}! You found the key!")
            print(f"You needed {steps} steps to find it.")
            play_again = input("Do you want to play again?\nType [yes] or [no] ")
            if play_again == "yes":
                play_game()
            else:
                quit()    
        # Second variable needed to display 'Cold' or 'Warmer' message
        distance_after_steps = sqrt((key_position_x - player_position_x) ** 2 + (key_position_y - player_position_y) ** 2)

        if distance_before_steps > distance_after_steps:
            print("Warmer!")
        else:
            print("Cold!")

        distance_before_steps = distance_after_steps

play_game()