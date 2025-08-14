import math
import turtle as t  # Python's built-in turtle graphics

class Turtle:
    def __init__(self, x=0, y=0, angle=0):
        # Tracking attributes
        self.x = x
        self.y = y
        self.angle = angle  # in degrees

        # Create turtle graphics window + turtle
        self.screen = t.Screen()
        self.turtle = t.Turtle()
        self.turtle.setheading(angle)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

    def forward(self, distance):
        # Math-based tracking
        rad = math.radians(self.angle)
        self.x += distance * math.cos(rad)
        self.y += distance * math.sin(rad)

        # Turtle graphics movement
        self.turtle.forward(distance)

        print(f"Moved forward {distance} → New position: ({self.x:.2f}, {self.y:.2f})")

    def backward(self, distance):
        self.forward(-distance)  # negative distance

    def left(self, degrees):
        self.angle = (self.angle + degrees) % 360
        self.turtle.left(degrees)
        print(f"Turned left {degrees}° → New angle: {self.angle}°")

    def right(self, degrees):
        self.angle = (self.angle - degrees) % 360
        self.turtle.right(degrees)
        print(f"Turned right {degrees}° → New angle: {self.angle}°")

    def position(self):
        return (self.x, self.y)

    def heading(self):
        return self.angle

    def wait(self):
        """Keeps the window open until user clicks."""
        self.screen.mainloop()

