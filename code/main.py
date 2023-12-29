import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SQUARE_SIZE = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Board Class

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board Example")
clock = pygame.time.Clock()

# Initialize the board
chess_board = Board()

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            chess_board.moove()
            chess_board.remove()
            chess_board.kill_enemy()
           
    # Clear the screen
    screen.fill(WHITE)

    # Draw the chessboard
    chess_board.draw_board(screen)

    # Draw the pieces
    chess_board.draw_pieces(screen)
    chess_board.sides()

    # Refresh display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

