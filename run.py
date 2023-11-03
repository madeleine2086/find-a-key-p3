# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

ROOM_WIDTH = 10
ROOM_HEIGHT = 10

key_position_x = randint(0, ROOM_WIDTH)
key_position_y = randint(0, ROOM_HEIGHT)

player_position_x = 0
player_position_y = 0
key_is_found = False

while not key_is_found:
    print("You can choose to go left [A], right [D], up [W] or down [S]: ")

    player_move = input("What's your move? ")

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

    print(player_position_x, player_position_y)