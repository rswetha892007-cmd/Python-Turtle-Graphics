import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Colorful Star Pattern")
screen.bgcolor("black")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "magenta"]

# Draw a colorful star pattern
for i in range(36):
    pen.pencolor(colors[i % len(colors)])

    for j in range(5):
        pen.forward(100)
        pen.right(144)

    pen.right(10)

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()