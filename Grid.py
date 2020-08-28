from Tile import Tile


class Grid:

    DEFAULT_TILE_COLOR = (250, 250, 250)    # White

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.__create_grid(width, height)

    # Returns representation of our grid
    # O(width * height) Time complexity
    def __repr__(self):
        grid = ''
        for row in self.grid:
            grid += str(row) + '\n'
        return grid

    # Returns a tile from our grid with given coordinates
    # O(1) Time complexity
    def get_tile(self, x, y):
        return self.grid[y][x]

    # Returns a list of cells of all cells neighbouring a cell in the board
    # O(1) Time complexity
    # O(1) Space complexity
    def get_neighbour_tiles(self, x, y):
        cells = []
        if self.__valid_point(x - 1, y - 1):  # Top left
            cells.append(self.grid[y - 1][x - 1])
        if self.__valid_point(x, y - 1):  # Top
            cells.append(self.grid[y - 1][x])
        if self.__valid_point(x + 1, y - 1):  # Top right
            cells.append(self.grid[y - 1][x + 1])
        if self.__valid_point(x - 1, y):  # Left
            cells.append(self.grid[y][x - 1])
        if self.__valid_point(x + 1, y):  # Right
            cells.append(self.grid[y][x + 1])
        if self.__valid_point(x - 1, y + 1):  # Bottom left
            cells.append(self.grid[y + 1][x - 1])
        if self.__valid_point(x, y + 1):  # Bottom
            cells.append(self.grid[y + 1][x])
        if self.__valid_point(x + 1, y + 1):  # Bottom Right
            cells.append(self.grid[y + 1][x + 1])
        return cells

    # Creates a 2D grid with given dimensions
    # O(width * height) Time complexity
    # O(width * height) Space complexity
    def __create_grid(self, width, height):
        grid = []
        for y in range(height):
            grid.append([])
            for x in range(width):
                grid[y].append(Tile(x, y, Grid.DEFAULT_TILE_COLOR))
        return grid

    # Returns if a coordinate is a valid point on the grid
    # O(1) Time complexity
    # O(1) Space complexity
    def __valid_point(self, x, y):
        return self.height > y >= 0 and self.width > x >= 0

