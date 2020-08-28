from queue import PriorityQueue
import DrawingFunctions


class TileQueue:

    def __init__(self):
        self.queue = PriorityQueue()
        self.duplicate_checker = set()

    def add(self, screen, block_size, line_width, tile_list, color, start_tile, end_tile, last):
        for tile in tile_list:
            # Ignore the start tile as we don't want to treat it like a normal one
            if tile.x == start_tile.x and tile.y == start_tile.y:
                continue
            # If the end tile was added to the queue don't change its color and other values
            if tile.x == end_tile.x and tile.y == end_tile.y:
                tile.last = last
                self.queue.put(tile)
                continue

            # Don't add blocked tiles as they cannot be traversed
            if tile.blocked:
                continue

            if tile not in self.duplicate_checker:
                # Changing the last value of the tile
                tile.last = last

                # Changing the tile's color
                tile.color = color

                # Updating the f cost of our tile so it can be ordered accordingly in the queue
                tile.update_cost(start_tile, end_tile)

                # Redrawing our added tiles
                DrawingFunctions.draw_tile(screen, block_size, line_width, tile)

                self.queue.put(tile)
                self.duplicate_checker.add(tile)

    # Returns the first tile in the queue
    def get(self):
        return self.queue.get()

    # Returns if the queue is empty
    def empty(self):
        return self.queue.empty()
