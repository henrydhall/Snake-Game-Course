# Not very pretty, sorry

import turtle

# Constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 # Milliseconds between screen updates

def move_snake():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    snake.append(new_head)
    snake.pop(0)

    for segment in snake:
        stamper.goto( segment[0], segment[1])
        stamper.stamp()

    screen.update()

    turtle.ontimer(move_snake, DELAY)

# Window
screen = turtle.Screen()
screen.setup( WIDTH, HEIGHT ) # Set screen dimensions
screen.title("Snake")
screen.bgcolor('pink')
screen.tracer(0) # Limit automatic animation

# Get a turtle (like in oop_turtle)
stamper = turtle.Turtle()
stamper.shape('square')
stamper.penup()

# Snake as list of coordinate pairs
snake = [[0,0],[20,0],[40,0],[60,0]]

# Draw snake for first time
for segment in snake:
    stamper.goto( segment[0], segment[1])
    stamper.stamp()

# Get move_snake running

move_snake()

turtle.done() # Must have to finish