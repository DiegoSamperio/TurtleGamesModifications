# Paint Application based on the FreeGames collection, with modifications made
# for a better drawing experience.
# Authors: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Date: 23/03/2023

from turtle import *
from freegames import vector

# Define state variables for the current drawing tool
state = {'shape': 'line'}  # Current shape to draw (line, square, circle, etc.)
color = 'black'  # Default drawing color

# Function to draw a line from one point to another
def line(start, end):
    "Draw a line from start to end."
    up()
    goto(start.x, start.y)  # Move to the start position
    down()
    goto(end.x, end.y)  # Draw the line to the end position

# Function to draw a square at a given position
def square(start, end):
    "Draw a square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Function to draw a circle based on start and end positions
def circle(start, end):
    "Draw a circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    turtle_circle(abs(end.x - start.x))
    end_fill()

# Helper function to draw a circle
def turtle_circle(radius):
    "Draw a circle with a given radius."
    for _ in range(360):
        forward(radius * 0.0175)  # Draw the circle using small steps
        left(1)

# Function to draw a rectangle from start to end
def rectangle(start, end):
    "Draw a rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x - start.x)
    left(90)
    forward((end.y - start.y))
    left(90)
    forward(end.x - start.x)
    left(90)
    forward((end.y - start.y))
    left(90)

    end_fill()

# Function to draw a triangle from start to end
def triangle(start, end):
    "Draw a triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

# Function to handle tap events and trigger drawing
def tap(x, y):
    "Store starting point or draw shape."
    start = state.get('start', None)

    if start is None:
        state['start'] = vector(x, y)  # Store the starting point
    else:
        shape = state['shape']
        end = vector(x, y)
        if shape == 'line':
            line(start, end)
        elif shape == 'square':
            square(start, end)
        elif shape == 'circle':
            circle(start, end)
        elif shape == 'rectangle':
            rectangle(start, end)
        elif shape == 'triangle':
            triangle(start, end)

        state['start'] = None  # Reset the starting point after drawing

# Function to set the current drawing tool
def store(key, value):
    "Store the shape and color to use."
    state[key] = value

# Set up the drawing window
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Bind keyboard keys to select shapes
onkey(lambda: store('shape', 'line'), 'l')  # Press 'l' to draw a line
onkey(lambda: store('shape', 'square'), 's')  # Press 's' to draw a square
onkey(lambda: store('shape', 'circle'), 'c')  # Press 'c' to draw a circle
onkey(lambda: store('shape', 'rectangle'), 'r')  # Press 'r' to draw a rectangle
onkey(lambda: store('shape', 'triangle'), 't')  # Press 't' to draw a triangle

# Set up mouse click event to trigger drawing
onscreenclick(tap)

done()
