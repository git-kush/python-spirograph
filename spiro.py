import turtle
wn = turtle.Screen()

# Set screen background color
wn.bgcolor('black')

# Create a new turtle
Albert = turtle.Turtle()

# Set Albert's speed, color and rotation variable
Albert.speed(0)
Albert.color('white')
rotate=int(360)

# Function to draw circles
def drawCircles(t,size):
    # Iterate 10 times
    for i in range(10):
        # draw circle
        t.circle(size)
        size=size-4

# Function to draw special shapes
def drawSpecial(t,size,repeat):
  # Iterate for range provided in args
  for i in range(repeat):
    # Draw circles using the drawCirles function
    drawCircles(t,size)
    # move right
    t.right(360/repeat)

# Tell Albert to use the drawSpecial function to draw spirographs
drawSpecial(Albert,100,10)

# Make another turtle
Steve = turtle.Turtle()

# Set steve's speed and color and rotate variable
Steve.speed(0)
Steve.color('yellow')
rotate=int(90)

# Update the function to draw circles
def drawCircles(t,size):
    # Iterate 4 times
    for i in range(4):
        # Make circle
        t.circle(size)
        size=size-10

# Update the function to draw spirographs
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

# Tell Steve to draw spirographs using the drawSpecial function
drawSpecial(Steve,100,10)

# Make another turtle
Barry = turtle.Turtle()

# Set Barry's color and speed
Barry.speed(0)
Barry.color('blue')
rotate=int(80)

# Update the function to draw circles
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5

# Update the function to draw spirographs
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

# Tell Barry to draw spirographs using the drawSpecial function
drawSpecial(Barry,100,10)

# Make another turtles Terry and Will and tell them to do the same . . .
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(Terry,100,10)


Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)

drawSpecial(Will,100,10)

# Exit only after clicking the screen
turtle.Screen().exitonclick()