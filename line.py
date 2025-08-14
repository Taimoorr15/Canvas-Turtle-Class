from point import Point
import math

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def length(self):
        lx = self.end.x - self.start.x
        ly = self.end.y - self.start.y
        return math.sqrt(lx**2 + ly**2)

    def __str__(self):
        return f"Line from {self.start} to {self.end} has length {self.length():.2f}"
