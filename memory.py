# Memory Game based on the FreeGames collection, with modifications made
# for a better gaming experience.
# Authors: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Date: 23/03/2023

from random import shuffle
from turtle import *
from freegames import path

# Load the image of the memory card's back
car = path('car.gif')

# Initialize state variables
tiles = list(range(32)) * 2  # Create a list of 64 tiles (32 pairs)
state = {'mark': None}  # Track the current marked tile
hide = [True] * 64  # Hide all tiles initially
taps = 0  # Count the number of taps made

# Set up the screen and add the car image
setup(420, 420, 370, 0)
addshape(car)
shape(car)
hideturtle()
tracer(False)

# Function to draw a square for each tile
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Function to convert tile index to screen coordinates
def index(x, y):
    "Convert (x, y) coordinates to tile index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Function to convert tile index to screen coordinates
def xy(count):
    "Convert tile count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Function to handle clicks and reveal tiles
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps
    spot = index(x, y)  # Get tile index from click position
    mark = state['mark']

    taps += 1  # Increment tap counter

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # Mark a new tile if it's not already marked or doesn't match
        state['mark'] = spot
    else:
        # If the two tiles match, reveal them
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

# Function to draw the board and tiles
def draw():
    "Draw image and tiles."
    clear()

    # Draw all tiles
    for count in range(64):
        x, y = xy(count)

        if hide[count]:
            square(x, y)  # Draw hidden tile
        else:
            up()
            goto(x + 2, y)
            color('black')
            write(tiles[count], font=('Arial', 30, 'normal'))  # Display tile number

    mark = state['mark']

    if mark is not None and hide[mark]:
        # Highlight the marked tile
        x, y = xy(mark)
        up()
        goto(x, y)
        down()
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Display the number of taps
    up()
    goto(-180, 180)
    down()
    color('black')
    write(f'Taps: {taps}', font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)

# Shuffle the tiles randomly at the start
shuffle(tiles)

# Start the game with the tap handler and drawing loop
onscreenclick(tap)
draw()
done()