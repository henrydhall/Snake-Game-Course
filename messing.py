# Not very pretty, sorry

import turtle
import random

# Constants
WIDTH = 800
HEIGHT = 600
DELAY = 100 # Milliseconds between screen updates
FOOD_SIZE = 10

offsets = { 'up': (0,20), 'down': (0,-20), 'left': (-20,0), 'right':(20,0) }

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction('up'),'Up')
    screen.onkey(lambda: set_snake_direction('down'),'Down')
    screen.onkey(lambda: set_snake_direction('left'),'Left')
    screen.onkey(lambda: set_snake_direction('right'),'Right')

def set_snake_direction(direction):
    global snake_direction
    if direction == 'up':
        if snake_direction != 'down':
            snake_direction = 'up'
    elif direction == 'down':
        if snake_direction != 'up':
            snake_direction = 'down'
    elif direction == 'left':
        if snake_direction != 'right':
            snake_direction = 'left'
    elif direction == 'right':
        if snake_direction != 'left':
            snake_direction = 'right'
    

# Animation function
def game_loop():
    stamper.clearstamps() # Remove existing stamps

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH/2 \
        or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT / 2:
        start_game() # Reset the game, start over
    else:
        # Add new head
        snake.append(new_head)

        # Check if they ate the food
        if not food_collision():
            # Get rid of tail
            snake.pop(0) # There is a collision, we don't want to pop, thus the 'not food_collision()' condition

        for segment in snake:
            stamper.goto( segment[0], segment[1])
            stamper.stamp()

        screen.title(f'Snake Game. Score: {score}')
        screen.update()

        turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_position, score # bring in globals
    if get_distance(snake[-1], food_position) < 20:
        score += 1 # increment score
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    x = random.randint( -WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint( -HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)
    return (x,y)

def get_distance(position_1,position_2):
    # Accepts 2 coordinate pairs, returns the distance using pythagorean theorem
    x1,y1 = position_1
    x2,y2 = position_2
    distance = ((y2-y1)**2 + (x2-x1)**2 ) ** 0.5
    return distance

def start_game():
    global score, snake, snake_direction, food_position
    score = 0
    # Snake as list of coordinate pairs
    snake = [[0,0],[20,0],[40,0],[60,0]]
    snake_direction = 'up'
    food_position = get_random_food_position()
    food.goto(food_position)
    game_loop()

# Window
screen = turtle.Screen()
screen.setup( WIDTH, HEIGHT ) # Set screen dimensions
screen.title("Snake")
screen.bgcolor('pink')
screen.tracer(0) # Limit automatic animation

# Events
# Use these to specify callbacks
screen.listen()
bind_direction_keys()

# Get a turtle (like in oop_turtle)
stamper = turtle.Turtle()
stamper.shape('circle')
stamper.penup()

# Food 
food = turtle.Turtle()
food.shape("triangle")
food.color("red")
food.shapesize( FOOD_SIZE / 20 )
food.penup()

# Start the game!
start_game()

# Must have to finish
turtle.done() 