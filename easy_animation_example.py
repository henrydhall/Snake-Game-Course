# Example of an animation using turtle library
# Not very pretty, sorry

import turtle

# Constants
WIDTH = 500
HEIGHT = 500
DELAY = 20 # Milliseconds between screen updates

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY )

# Window
screen = turtle.Screen()
screen.setup( WIDTH, HEIGHT ) # Set screen dimensions
screen.title("animationg example")
screen.bgcolor('red')
screen.tracer(0) # Turn on automatic animation

# Get a turtle (like in oop_turtle)
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('Blue')


if __name__ == '__main__':
    move_turtle()
    turtle.done() # Always need to call turtle.done when you're done.
        
# In the next clip he goes over global variables...to use a global variable in a function, say something like
# 'global my_var_name'