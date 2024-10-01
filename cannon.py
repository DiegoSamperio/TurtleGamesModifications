# Cannon Game based on the FreeGames collection, with modifications made
# for a better gaming experience.
# Authors: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Date: 23/03/2023

from random import randrange
from turtle import *
from freegames import vector

# Set up the ball and targets
ball = vector(-200, -200)  # Ball's initial position off-screen
speed = vector(0, 0)  # Initial speed of the ball
targets = []  # List to hold target positions

# Function to fire the cannonball by setting the ball's position and speed
def tap(x, y):
    "Respond to screen tap by firing the cannonball."
    if not inside(ball):
        # Set the ball's position to the firing point and set the speed vector
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

# Function to check if the object is within the screen boundaries
def inside(xy):
    "Return True if xy within screen boundaries."
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Function to draw the ball and targets on the screen
def draw():
    "Draw ball and targets."
    clear()

    # Draw all targets
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Draw the ball only if it's within the screen
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Function to move the ball and targets
def move():
    "Move ball and targets."
    # Add new random targets
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move all targets leftward
    for target in targets:
        target.x -= 0.5

    # Move the ball based on its speed vector
    if inside(ball):
        speed.y -= 0.35  # Gravity effect on the ball
        ball.move(speed)

    # Create a list of remaining targets that are still within the screen
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # Remove the ball if it goes off-screen
    draw()

    # Check for end conditions
    for target in targets:
        if not inside(target):
            targets.remove(target)

    # Schedule the next frame
    ontimer(move, 50)

# Set up the game window and key bindings
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()