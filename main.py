import pygame
import os
import DrawingFunctions
import time
from Grid import Grid
from TileQueue import TileQueue
from tkinter import Tk, StringVar
from tkinter.ttk import *

# Constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

WINDOW_STARTING_X_POS = 480
WINDOW_STARTING_Y_POS = 50

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
GREEN = (0, 204, 0)
BLUE = (0, 153, 153)
RED = (204, 0, 0)

BLOCK_SIZE = 15
LINE_WIDTH = 2
FPS = 144

LEFT_CLICK = 1


# Displays the shortest path found by the algorithm
def display_shortest_path(last_tile):
    while last_tile.last is not None:
        last_tile.color = BLUE
        DrawingFunctions.draw_tile(screen, BLOCK_SIZE, LINE_WIDTH, last_tile)
        pygame.display.update()
        last_tile = last_tile.last


# Draws all blocked tiles which the user marked
def draw_blocked_tiles():
    finished = False  # Loop control variable
    mouse_down = False  # Variable for mouse hold

    while not finished:

        for event in pygame.event.get():
            if event == pygame.QUIT:    # On quit button clicked
                finished = True
                continue
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:    # On left mouse click
                mouse_down = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT_CLICK:
                mouse_down = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:    # If enter button is clicked
                finished = True

            if mouse_down:
                # Getting the click position and adjusting it to our grid
                position = pygame.mouse.get_pos()
                x, y = position
                x, y = x // BLOCK_SIZE, y // BLOCK_SIZE

                # Getting the clicked tile and changing it to be blocked and have the appropriate color
                tile = grid.get_tile(x, y)
                tile.blocked = True
                tile.color = BLACK

                # Drawing the tile
                DrawingFunctions.draw_tile(screen, BLOCK_SIZE, LINE_WIDTH, tile)

            pygame.display.update()


# Parse the tkinter variables we got from the tkinter window
def parse_tkinter(first_coordinates, second_coordinates):
    global start_tile, end_tile

    first = first_coordinates.get().split(',')
    start_tile = grid.get_tile(int(first[0]), int(first[1]))
    second = second_coordinates.get().split(',')
    end_tile = grid.get_tile(int(second[0]), int(second[1]))


# Displaying a tkinter window and getting user input from it
# User inputs the start and end coordinates for the tiles
def tkinter_input():
    # Creating a tkinter window for starting points input
    root = Tk()
    root.title('Enter coordinates')
    root.geometry('250x150+850+400')

    # Variables for storing our input
    first_coordinates = StringVar()
    second_coordinates = StringVar()

    # Input widgets
    first_input = Entry(root, width=35, textvariable=first_coordinates)
    second_input = Entry(root, width=35, textvariable=second_coordinates)

    # Setting prompts
    first_input.insert(0, 'Enter coordinates in (x,y) format')
    second_input.insert(0, 'Enter coordinates in (x,y) format')

    # Displaying the input widgets
    first_input.grid(row=0, column=0)
    second_input.grid(row=1, column=0)

    # Creating submit button
    submit_button = Button(root, text='Submit', command=lambda: root.destroy())
    submit_button.grid(row=2, column=0)

    root.mainloop()

    # Parsing the input variables and updating the global variables which are the start and end tiles
    parse_tkinter(first_coordinates, second_coordinates)


def main():

    # Drawing our screen
    DrawingFunctions.draw_grid(screen, WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, LINE_WIDTH)
    pygame.display.update()

    # Getting coordinates for the start and end tiles
    tkinter_input()

    # If the start tile equals the end tile just quit
    if start_tile.x == end_tile.x and start_tile.y == end_tile.y:
        return

    # Drawing start and end tiles
    DrawingFunctions.draw_first_tiles(screen, BLOCK_SIZE, LINE_WIDTH, start_tile, end_tile, BLUE)

    # Drawing our blocked tiles
    draw_blocked_tiles()

    # Setting up regular variables
    tile_queue = TileQueue()

    # Initializing our queue
    start_tile_neighbours = grid.get_neighbour_tiles(start_tile.x, start_tile.y)
    tile_queue.add(screen, BLOCK_SIZE, LINE_WIDTH, start_tile_neighbours, GREEN, start_tile, end_tile, start_tile)

    # Setting up loop variables
    running = True

    while running:

        # Pulling out the best tile
        best_tile = tile_queue.get()

        # If the algorithm reached the end tile break
        if best_tile.x == end_tile.x and best_tile.y == end_tile.y:
            display_shortest_path(best_tile)
            time.sleep(5)
            break

        best_tile.color = RED
        DrawingFunctions.draw_tile(screen, BLOCK_SIZE, LINE_WIDTH, best_tile)

        # Adding the best tile's neighbours to the queue
        neighbours = grid.get_neighbour_tiles(best_tile.x, best_tile.y)
        tile_queue.add(screen, BLOCK_SIZE, LINE_WIDTH, neighbours, GREEN, start_tile, end_tile, best_tile)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if tile_queue.empty():
            running = False

        pygame.display.update()


# Initializing the game
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{WINDOW_STARTING_X_POS},{WINDOW_STARTING_Y_POS}'  # Setting the initial starting position of the window in the middle of the screen
pygame.init()

# Creating the game and setting it up
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption('A* visualizer')
clock = pygame.time.Clock()     # FPS clock

# Creating global variables
grid = Grid(SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE)
start_tile = grid.get_tile(0, 0)
end_tile = grid.get_tile(0, 0)


# Starting the visualization
main()

