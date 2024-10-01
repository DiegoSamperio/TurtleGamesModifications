# Pacman Game based on the FreeGames collection, with modifications made
# for a better gaming experience.
# Authors: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Date: 23/03/2023

from random import choice
from turtle import *
from freegames import floor, vector

# Initialize the state of the game
state = {'score': 0}  # To track the player's score
path = Turtle(visible=False)  # Used to draw the game path
writer = Turtle(visible=False)  # Used to display the score

# Setup the movement vectors for Pacman and ghosts
aim = vector(5, 0)  # Initial direction for Pacman
pacman = vector(-40, -80)  # Starting position of Pacman
ghosts = [
    [vector(-180, 160), vector(5, 0)],  # Ghost 1 position and direction
    [vector(-180, -160), vector(0, 5)],  # Ghost 2 position and direction
    [vector(100, 160), vector(0, -5)],  # Ghost 3 position and direction
    [vector(100, -160), vector(-5, 0)]  # Ghost 4 position and direction
]

# Define the tiles for the Pacman grid (1 = wall, 0 = path)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Function to draw the Pacman game board
def square(x, y):
    "Draw a square at (x, y) on the board."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

# Function to get the offset in the tiles array based on x, y coordinates
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) // 20
    y = (180 - floor(point.y, 20)) // 20
    index = int(x + y * 20)
    return index

# Function to check if Pacman or ghost can move to the next tile
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return True

# Function to draw the entire game world (walls and Pac-dots)
def world():
    "Draw the Pacman world."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

# Function to move Pacman and the ghosts
def move():
    "Move Pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    # Move Pacman if the next tile is valid
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    # Move the ghosts and check for collisions with Pacman
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            course.x = choice(options).x
            course.y = choice(options).y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    # Check if Pacman collides with any ghost
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)

# Function to change Pacman's direction
def change(x, y):
    "Change Pacman's direction."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Set up the game window and event handling
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()

# Bind the arrow keys to change Pacman's direction
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')

# Draw the game world and start the movement loop
world()
move()
done()
