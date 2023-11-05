
## Find The Key - Game Description

- Find The Key is simple but enjoyable, command line game.
- The player's goal is to find the key that's hidden in a dark, square room. The key can be anywhere and its position is randomly set before the player starts.
- The player is guided by messages describing player's distance from the key. If the distance is deacreasing, a 'Warmer!' message is printed to the terminal. If the distance is increasing, a 'Cold!' message is printed instead.
- The player's goal is to find the key by navigating themselves with the help of messages printed while taking steps.
- The game is written in Python and can be accessed in a mock terminal.


## How To Play

1. The player starts the game in a square room, sized 10 x 10.
2. The player's starting position is 0, 0 - on x and y axis respectively.
3. The player can go in four different directions, using 'W' for up, 'S' for down, 'A' for left and 'D' for right.
4. If, after making a move, the player sees 'Warmer' message, distance between the key and the player is smaller than it was before making that move - good direction.
5. If, after making a move, the player sees 'Cold!' message displayed, distance between the key and the player is bigger than it was before making that move - wrong direction.
6. When the key is found, the player has the option to continue with another round or quitting the game.

## Features

- Random key position generation, using randint from random library.
- Accepts user input:
    - The player types their name, which is then used to display personal 'Congratulations' message.
    - The player navigates in the room by typing which direction they want to go.
    - The player decides if they want to continue with another round or stop playing.
- Input Validation:
    - Message displayed when player is trying to go outsie the grid size - player can't make a move outside the room.
    - Message 'Incorrect move, try again!' displayed if values other than 'W', 'S', 'A', 'D' are keyed in.

## Future Features

- Allow players to select the room size.
- Allow players to start from different corners of the room.

## Testing

- I have manually tested this project by:
    - Testing in my local terminal and Code Institute Heroku terminal.
    - Giving invalid inputs by typing values other than control keys; trying to go outside of the grid size.

## Testing

- PEP8 - no errors returned.

## Deployment

- This project was deployed using Code Institute's mock terminal for Heroku:
    - Steps for deployment:
        - Fork or clone this repository
        - Create a new Heroku app
        - Set the buildbacks to Python and NodeJS in that order
        - Link the Heroku app to the repository
        - Click on Deploy

## Credits

- Code Institute for the deployment terminal.
- This project is inspired by work of developers sharing their knowledge onlie:
    - https://www.youtube.com/@KacperSieradzinski
    - https://www.youtube.com/@AniaKubow
    - https://www.youtube.com/@programmingwithmosh
    - https://www.youtube.com/@TechWithTim
