# This class represents a single tile in our grid
import math


class Tile:

    def __init__(self, x, y, color):
        # coordinates on the grid
        self.x = x
        self.y = y

        self.f_cost = 0     # Sum of g cost and h cost

        self.blocked = False
        self.color = color
        self.last = None    # The tile which we reached the current tile from

    # f cost is equal to the sum of the g cost and f cost which are the distance from the starting point and from the end point respectively
    def update_cost(self, start_cell, end_cell):
        self.f_cost = self._distance(start_cell) + self._distance(end_cell)

    def _distance(self, other):
        return math.dist((self.x, self.y), (other.x, other.y))

    def __repr__(self):
        return f'{str(self.x)}, {str(self.y)}, {str(self.color)}, {str(self.f_cost)}'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.f_cost == other.f_cost

    def __gt__(self, other):
        return self.f_cost > other.f_cost


