# Not very pretty, sorry

import turtle

# Constants
WIDTH = 500
HEIGHT = 500
DELAY = 20 # Milliseconds between screen updates

# Window
screen = turtle.Screen()
screen.setup( WIDTH, HEIGHT ) # Set screen dimensions
screen.title("stamps")
screen.bgcolor('cyan')

# Get a turtle (like in oop_turtle)
stamper = turtle.Turtle()
stamper.shape('square')
stamper.color('Blue')
stamper.shapesize(50/20)
stamper.stamp()
stamper.penup()
stamper.shapesize(10/20)
stamper.goto(100,100)
stamper.stamp()

turtle.done() # Must have