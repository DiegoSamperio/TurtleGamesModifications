# Snake Game based on the FreeGames collection, with modifications made
# for a better gaming experience.
# Authors: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Date: 23/03/2023

from turtle import *
from random import randrange
from freegames import square, vector

# Set up initial positions and direction for snake and food
food = vector(0, 0)  # Position of the food
snake = [vector(10, 0)]  # List of vectors representing the snake's body
aim = vector(0, -10)  # Direction of the snake's movement

# Function to change the direction of the snake
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# Function to check if the snake's head is within the boundaries
def inside(head):
    "Return True if head is inside the boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Function to move the snake and check for collisions
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()  # Copy the current head of the snake
    head.move(aim)  # Move the head in the direction of the aim

    # Check if the snake collides with the boundary or itself
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Draw the collision point
        update()
        return  # End the game

    # Add the new head to the snake
    snake.append(head)

    # Check if the snake eats the food
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10  # Move the food to a new random position
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  # Remove the tail of the snake

    # Clear the screen and draw the snake and food
    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')  # Draw each part of the snake

    square(food.x, food.y, 9, 'red')  # Draw the food
    update()
    ontimer(move, 100)  # Schedule the next move

# Set up the game window and key bindings for snake direction
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Bind arrow keys to change direction
onkey(lambda: change(10, 0), 'Right')  # Move right
onkey(lambda: change(-10, 0), 'Left')  # Move left
onkey(lambda: change(0, 10), 'Up')  # Move up
onkey(lambda: change(0, -10), 'Down')  # Move down

move()  # Start the game loop
done()
