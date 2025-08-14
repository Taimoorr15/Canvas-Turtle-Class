class Pen:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveTo(self, x, y):
        """Move the pen to an absolute position (x, y)."""
        self.x = x
        self.y = y

    def lineTo(self, x, y):
        """Draw a line from current position to (x, y) and update position."""
        print(f"Drawing line from ({self.x}, {self.y}) to ({x}, {y})")
        self.x = x
        self.y = y

    def getPosition(self):
        """Return current pen position."""
        return (self.x, self.y)



