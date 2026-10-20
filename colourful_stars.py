import turtle

# Create the drawing screen
screen = turtle.Screen()
screen.title("Colorful Star Pattern")
screen.bgcolor("black")

# Create the turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

# List of colors
colors = ["red", "yellow", "cyan", "lime", "magenta", "orange"]

# Function to draw a star
def draw_star(size, color):
    pen.pencolor(color)

    for i in range(5):
        pen.forward(size)
        pen.right(144)

# Positions for the stars
positions = [
    (-200, 100),
    (0, 100),
    (200, 100),
    (-100, -120),
    (100, -120),
    (0, -20)
]

# Draw the stars
for i in range(len(positions)):
    pen.penup()
    pen.goto(positions[i])
    pen.pendown()
    draw_star(80, colors[i])

# Hide the turtle cursor
pen.hideturtle()

# Keep the window open
turtle.done()