# Not very pretty, sorry

import turtle

# Constants
WIDTH = 500
HEIGHT = 500
DELAY = 400 # Milliseconds between screen updates

offsets = { 'up': (0,20), 'down': (0,-20), 'left': (-20,0), 'right':(20,0) }

# Event call back functions
def go_up():
    global snake_direction
    if snake_direction != 'down':
        snake_direction = 'up'

def go_right():
    global snake_direction
    if snake_direction != 'left':
        snake_direction = 'right'

def go_down():
    global snake_direction
    if snake_direction != 'up':
        snake_direction = 'down'

def go_left():
    global snake_direction
    if snake_direction != 'right':
        snake_direction = 'left'

# Animation function
def game_loop():
    stamper.clearstamps() # Remove existing stamps

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 \
        or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT / 2:
        turtle.bye()
    else:
        # Add new head, get rid of tail
        snake.append(new_head)
        snake.pop(0)

        for segment in snake:
            stamper.goto( segment[0], segment[1])
            stamper.stamp()

        screen.update()

        turtle.ontimer(game_loop, DELAY)

# Window
screen = turtle.Screen()
screen.setup( WIDTH, HEIGHT ) # Set screen dimensions
screen.title("Snake")
screen.bgcolor('pink')
screen.tracer(0) # Limit automatic animation

# Events
# Use these to specify callbacks
screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_right, 'Right')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')

# Get a turtle (like in oop_turtle)
stamper = turtle.Turtle()
stamper.shape('square')
stamper.penup()

# Snake as list of coordinate pairs
snake = [[0,0],[20,0],[40,0],[60,0]]
snake_direction = 'up'

# Draw snake for first time
for segment in snake:
    stamper.goto( segment[0], segment[1])
    stamper.stamp()

# Get game_loop running

game_loop()

# Must have to finish
turtle.done() 