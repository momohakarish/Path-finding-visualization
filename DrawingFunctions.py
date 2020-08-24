import pygame


def draw_grid(screen, background_color, line_color, screen_width, screen_height, block_size, line_width):

    # Setting the background color of our screen
    screen.fill(background_color)

    # Drawing our lines
    for x in range((screen_width // block_size)):
        pygame.draw.line(screen, line_color, ((x + 1) * block_size, 0), ((x + 1) * block_size, screen_height), line_width)
    for y in range((screen_height // block_size)):
        pygame.draw.line(screen, line_color, (0, (y + 1) * block_size), (screen_height, (y + 1) * block_size), line_width)


def draw_tile(screen, block_size, line_width, tile):
    rect = pygame.Rect(tile.x * block_size + line_width, tile.y * block_size + line_width, block_size - line_width, block_size - line_width)
    pygame.draw.rect(screen, tile.color, rect)


def draw_first_tiles(screen, block_size, line_width, start_tile, end_tile, color):
    start_tile.color = color
    end_tile.color = color
    draw_tile(screen, block_size, line_width, start_tile)
    draw_tile(screen, block_size, line_width, end_tile)
    pygame.display.update()
