import pygame
import sys
import numpy as np
from back_game import Board
from config import *
import time
# Initialize Pygame
pygame.init()





screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board Example")
clock = pygame.time.Clock()

chess_board = Board()

# Game loop
running = True
turn = 0
click = False
def regularise_row_col(pos):
    row = event.pos[1] // SQUARE_SIZE
    col = event.pos[0] // SQUARE_SIZE
    
    return row,col
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
             
            click = True
            
            pos = pygame.mouse.get_pos() 
            row,col = regularise_row_col(pos)

            chess_board.valid_moove(row,col)
            chess_board.draw_valid_position(screen,row,col)
            chess_board.moove(event,screen)
            chess_board.remove()
            chess_board.kill_enemy(event,turn)

            

        
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

