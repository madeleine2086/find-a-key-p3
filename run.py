# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from math import sqrt
from random import randint

ROOM_WIDTH = 10
ROOM_HEIGHT = 10

player_name = input("What's your name? ")
print(f"Hello {player_name}!")

def play_game():
    key_position_x = randint(0, ROOM_WIDTH)
    key_position_y = randint(0, ROOM_HEIGHT)

    player_position_x = 0
    player_position_y = 0
    key_is_found = False
    steps = 0
    
    print("Your task is to find the key in a dark square room.\nYou start in the bottom left corner.")
    distance_before_steps = sqrt((key_position_x - player_position_x) ** 2 + (key_position_y - player_position_y) ** 2)
    print(key_position_x, key_position_y)

    while not key_is_found:
        steps += 1
        print("")
        print("You can choose to go left [A], right [D], up [W] or down [S]: ")

        player_move = input(f"What's your move? ")

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
            print("Incorrect move, try again!")

        if player_position_x == key_position_x and player_position_y == key_position_y:
            print(f"Congratulations {player_name}! You found the key!")
            print(f"You needed {steps} moves to find it.")
            play_again = input("Do you want to play again?\nType [yes] or [no] ")
            if play_again == "yes":
                play_game()
            else:
                quit()    

        distance_after_steps = sqrt((key_position_x - player_position_x) ** 2 + (key_position_y - player_position_y) ** 2)

        if distance_before_steps > distance_after_steps:
            print("Warmer!")
            print(player_position_x, player_position_y)
        else:
            print("Cold!")
            print(player_position_x, player_position_y)

        distance_before_steps = distance_after_steps

play_game()