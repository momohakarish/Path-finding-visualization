# This class represents a single tile in our grid

class Tile:

    def __init__(self,x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f'{str(self.x)}, {str(self.y)}, {str(self.color)}'


