import pygame
import sys
import numpy as np
from back_game import Board
from config import *
import time
from game import game
# Initialize Pygame
pygame.init()





screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board Example")
clock = pygame.time.Clock()
chess_board = Board()
game = game()


# Game loop
running = True
turn = 0
click = False
selected = None
def regularise_row_col(pos):
    row = event.pos[1] // SQUARE_SIZE
    col = event.pos[0] // SQUARE_SIZE
    
    return row,col

chess_board.draw_board(screen)
chess_board.draw_pieces(screen)
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
   
            pos = pygame.mouse.get_pos() 
            row,col = regularise_row_col(pos)
            screen.fill(WHITE)

            
    # Clear the screen
                

            # Draw the chessboard
            chess_board.draw_board(screen)

            # Draw the pieces
            chess_board.click(event,screen,row,col,click)
            chess_board.draw_pieces(screen)

            
    pygame.display.update()



# Quit Pygame
pygame.quit()
sys.exit()

