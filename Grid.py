from Tile import Tile


class Grid:

    DEFAULT_TILE_COLOR = (200, 200, 200)    # White

    def __init__(self, width, height):
        self.grid = self._create_grid(width, height)

    def __repr__(self):
        grid = ''
        for row in self.grid:
            grid += str(row) + '\n'
        return grid

    def _create_grid(self, width, height):
        grid = []
        for y in range(height):
            grid.append([])
            for x in range(width):
                grid[y].append(Tile(x, y, Grid.DEFAULT_TILE_COLOR))
        return grid


b = Grid(4, 5)
print(b)