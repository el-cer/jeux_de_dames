import pygame
import sys
import numpy as np
from back_game import Board
from config import *
import game_play

# Initialize Pygame
pygame.init()





screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checker GAME ELIOT CERON ")
clock = pygame.time.Clock()
running = True

checkers_back = Board(running)


# Game loop
running = True
turn = 0
click = False
selected = None
def regularise_row_col(pos):
    row = event.pos[1] // SQUARE_SIZE
    col = event.pos[0] // SQUARE_SIZE
    
    return row,col

checkers_back.draw_board(screen)
checkers_back.draw_pieces(screen)
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or checkers_back.running==False:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
   
            pos = pygame.mouse.get_pos() 
            row,col = regularise_row_col(pos)
            screen.fill(WHITE)

            
    # Clear the screen
                
            
            # Draw the chessboard
            checkers_back.draw_board(screen)

            # Draw the pieces
            checkers_back.click(screen,row,col)
            checkers_back.draw_pieces(screen)    
    pygame.display.update()



# Quit Pygame
pygame.quit()
sys.exit()

