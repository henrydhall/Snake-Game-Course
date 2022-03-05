import turtle

# Constants
WIDTH = 500
HEIGHT = 500

# Window
screen = turtle.Screen()
screen.setup( WIDTH, HEIGHT )
screen.title("turtle template")
screen.bgcolor('red')

# Get a turtle (like in oop_turtle)
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('Blue')

# Example of a command to use on your turtle
my_turtle.forward(100)

# Always need to call turtle.done when you're done.
turtle.done()