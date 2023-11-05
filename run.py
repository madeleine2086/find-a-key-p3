# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from math import sqrt
from random import randint

# Creating constant variables for setting the grid size
ROOM_WIDTH = 10
ROOM_HEIGHT = 10

# Asking for a name to display the welcome message and use in f string later
player_name = input("What's your name? ")
print(f"Hello {player_name}!")

# Creating the function for the game


def play_game():

    # Setting a random key position using randint
    key_x = randint(0, ROOM_WIDTH)
    key_y = randint(0, ROOM_HEIGHT)

    player_x = 0
    player_y = 0
    key_is_found = False
    steps = 0

    # Printing rules og the game to the terminal
    print("Your task is to find the key in a dark square room.")
    print("You start in the bottom left corner.")
    print("We will guide you to the key by displaying 'Warmer' or 'Cold'")

    # Creating 1st variable for calculating distance to the key
    # Variable needed for printing 'Warmer' or 'Cold' message
    before_step = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    # Steps in the game while the player is looking for the key:
    while not key_is_found:
        steps += 1
        print("")
        print("You can choose to go left [A], right [D], up [W] or down [S]: ")

        player_move = input(f"What's your move? ")

        # Making sure that the player doesn't go outside the grid
        if player_move == "a":
            player_x -= 1
            if player_x < 0:
                print("You hit the wall!!")
                player_x = 0
        elif player_move == "d":
            player_x += 1
            if player_x > ROOM_WIDTH:
                print("You hit the wall!!")
                player_x = ROOM_WIDTH
        elif player_move == "w":
            player_y += 1
            if player_y > ROOM_HEIGHT:
                print("You hit the wall!!")
                player_y = ROOM_HEIGHT
        elif player_move == "s":
            player_y -= 1
            if player_y < 0:
                print("You hit the wall!!")
                player_y = 0
        else:
            # Message displayed in case of using keys other than movement keys
            print("Incorrect move, try again!")
            continue

        # If statement printing a message in case player finds the key
        # Giving the option to continue the game or to quit
        if player_x == key_x and player_y == key_y:
            print(f"Congratulations {player_name}! You found the key!")
            print(f"You needed {steps} steps to find it.")
            print("Do you want to play again?")
            play_again = input("Type [yes] or [no] ")
            if play_again == "yes":
                play_game()
            else:
                quit()
        # Second variable needed to display 'Cold' or 'Warmer' message
        after_step = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

        if before_step > after_step:
            print("Warmer!")
        else:
            print("Cold!")

        # After making one step in either direction,
        # distance_after_steps becomes distance_before_steps for the next step:
        before_step = after_step


play_game()