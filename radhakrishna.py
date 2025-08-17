import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Krishna Janmashtami Drawing")

# Setup pen
pen = turtle.Turtle()
pen.speed(7)
pen.pensize(2)
pen.color("yellow")

# Function to draw curve
def curve(angle, steps, length):
    for i in range(steps):
        pen.left(angle)
        pen.forward(length)

# Start Drawing Krishna Face Outline
pen.penup()
pen.goto(-100, 50)
pen.pendown()

pen.circle(40, 180)         # face left curve
curve(1, 80, 1)             # smooth jaw line
pen.left(90)
curve(1, 60, 1)

# Hair & Crown
pen.left(100)
curve(1, 80, 1)
pen.circle(40, 100)

# Feather
pen.left(100)
curve(1, 60, 1)
pen.circle(20, 120)

# Back to ear
pen.penup()
pen.goto(-70, 20)
pen.pendown()
pen.circle(10)  # earring

# Lips
pen.penup()
pen.goto(-60, -30)
pen.setheading(-30)
pen.pendown()
curve(2, 20, 1)

# Flute
pen.penup()
pen.goto(-120, -50)
pen.setheading(0)
pen.pendown()
pen.forward(250)

# Radha Face
pen.penup()
pen.goto(60, 50)
pen.pendown()
pen.circle(40, 180)
curve(1, 80, 1)

# Radha Hair
pen.left(90)
curve(1, 60, 1)
pen.left(100)
curve(1, 80, 1)

# Radha Earring
pen.penup()
pen.goto(90, 20)
pen.pendown()
pen.circle(10)

# Radha Lips
pen.penup()
pen.goto(80, -30)
pen.setheading(-30)
pen.pendown()
curve(2, 20, 1)

# Done
pen.hideturtle()
screen.mainloop()
