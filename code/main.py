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
class Board:
    def __init__(self):
        self.mat = None
        self.list_black = []
        self.list_white = []
        self.create_board()

    def create_board(self):
        self.mat = np.array([[2, 0, 2, 0, 2, 0, 2, 0],
                             [0, 2, 0, 2, 0, 2, 0, 2],
                             [2, 0, 2, 0, 2, 0, 2, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 1, 0, 1, 0, 1],
                             [1, 0, 1, 0, 1, 0, 1, 0],
                             [0, 1, 0, 1, 0, 1, 0, 1]])
        # Matrice de 8x8 avec Pour les 3 premiere lige des valeurs 2 pour noir et 1 pour blanc

    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    def draw_pieces(self, screen):

        for row in range(8):
            for col in range(8):
                if self.mat[row, col] == 2:
                    pygame.draw.circle(screen, (0, 0, 0), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)
                elif self.mat[row, col] == 1:
                    pygame.draw.circle(screen, (220, 220, 255), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)

    def sides(self):
        self.list_black = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 2]
        self.list_white = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 1]        
    def moove(self):
        col = event.pos[0] // SQUARE_SIZE
        row = event.pos[1] // SQUARE_SIZE
        if (row,col) in self.list_white:
            if event.button == 1:
                self.mat[row][col] -= 1
                self.mat[row - 1][col + 1] += 1
            elif event.button == 3:  
                self.mat[row][col] -= 1
                self.mat[row - 1][col - 1] += 1
            
            
        elif (row,col) in self.list_black:
            if event.button == 1:     
                self.mat[row][col] -= 2
                self.mat[row + 1][col + 1] += 2
            elif event.button == 3:     
                self.mat[row][col] -= 2
                self.mat[row + 1][col -1] += 2
            
    def remove(self):
        for x in range(0,self.mat.shape[0]):
            for y in range(0,self.mat.shape[1]):
                if self.mat[x][y] >2:
                    self.mat[x][y] = 0
    def kill_enemy(self):
        col = event.pos[0] // SQUARE_SIZE
        row = event.pos[1] // SQUARE_SIZE
        if (row,col) in self.list_white:
            if (row-1,col-1) in self.list_black and self.mat[row-2][col-2] == 0:
                self.mat[row-2][col-2] += 1
                self.mat[row-1][col-1] =0
                if (row-1,col+1) in self.list_black:
                    self.mat[row-1][col+1] = 1
                else:
                    self.mat[row-1][col+1] =0

                print(self.mat)
            elif (row-1,col+1) in self.list_black and self.mat[row-2][col+2] == 0:
                self.mat[row-2][col+2] += 1
                self.mat[row-1][col+1] =0
                
                if (row-1,col+1) in self.list_black:
                    self.mat[row-1][col+1] = 0
                else:
                    self.mat[row-1][col+1] = 1

                print(self.mat)
            

           

        if (row,col) in self.list_black:
            if (row+1,col+1) in self.list_white and self.mat[row+2][col+2] == 0:
                self.mat[row+2][col+2] += 2
                self.mat[row+1][col+1] =0
                if (row-1,col+1) in self.list_black:
                    self.mat[row-1][col+1] = 2
                else:
                    self.mat[row-1][col+1] =0

                print(self.mat)
            elif (row+1,col-1) in self.list_white and self.mat[row+2][col-2] == 0:
                self.mat[row+2][col-2] += 2
                self.mat[row+1][col+1] =0
                if (row+1,col+1) in self.list_black:
                    self.mat[row+1][col+1] = 2
                else:
                    self.mat[row+1][col+1] =0
                print(self.mat)
            
            

            


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

