import pygame
import sys
import numpy as np
from config import *
import time
class Board:
    def __init__(self):
        self.mat = None
        self.list_black = []
        self.list_white = []
        self.moove_yes = False
        self.draw_future_position = True
        self.pion = True
        self.selected = None

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
                color = WHITE if (row + col) % 2 == 0 else BLACK #pour chaque carre mettre 1 fois sur 2 blanc et noir
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    def draw_pieces(self, screen):

        for row in range(8):
            for col in range(8):
                if self.mat[row, col] == 2: #si la valeur dans la matrice est 2 alors equipe noir
                    pygame.draw.circle(screen, (0, 0, 0), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)
                    
                elif self.mat[row, col] == 1: #inverse
                    pygame.draw.circle(screen, (220, 220, 255), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)

    def sides(self):
        self.list_black = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 2]
        #mettre danns une list les coordonnées des pions noir 
        self.list_white = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 1]        
        
        self.list_empty = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 0]        

    def valid_moove(self,row,col):
        if (row,col) in self.list_white  and row-1>=0 and col+1<8 and col-1>=0:
            self.list_moove_white =[(row-1,col+1),(row-1,col-1)]

        elif (row,col) in self.list_black and row+1<8 and col+1<8 and col-1>=0:
            self.list_moove_black = [(row+1,col-1),(row+1,col+1)]
        
    
            

        #pareil pour les blanc
    def draw_valid_position(self,screen,row,col):
        if self.valid_moove in self.list_empty:
            pygame.draw.circle(screen, GREY, ((col + 1) * SQUARE_SIZE + SQUARE_SIZE // 2, (row - 1) * SQUARE_SIZE + SQUARE_SIZE // 2), 5)
            pygame.draw.circle(screen, GREY, ((col - 1) * SQUARE_SIZE + SQUARE_SIZE // 2, (row - 1) * SQUARE_SIZE + SQUARE_SIZE // 2), 5)
            pygame.display.flip() 
             # Update the display to show the temporary circles
        

    def click_on_future(self,click, position, event, row, col):
        pass
 
              
    def moove(self,event,screen):
        col = event.pos[0] // SQUARE_SIZE
        row = event.pos[1] // SQUARE_SIZE
        #a chaque click on a la position du pion
 
        if (row,col) in self.list_white and all(move in self.list_empty for move in self.list_moove_white):
            print(True)
            if event.button == 1:
                    self.mat[row][col] -= 1
                    self.mat[row - 1][col + 1] += 1
                    print('1')
                #si click gauche le pion va aller a droite
            elif event.button == 3:
                    self.mat[row][col] -= 1 
                    self.mat[row - 1][col - 1] += 1
                    
                
                #button =3 click droit c'est pour aller a droite
            
            
        elif (row,col) in self.list_black and all(move in self.list_empty for move in self.list_moove_white):
            print('can')
            if event.button == 1 :
                    self.mat[row][col] = 0
                    self.mat[row + 1][col + 1] += 2                    
            elif event.button == 3:
                    self.mat[row][col] =0
                    self.mat[row + 1][col -1] += 2
            
    def remove(self):
        for x in range(0,self.mat.shape[0]):
            for y in range(0,self.mat.shape[1]):
                if self.mat[x][y] >2:
                    self.mat[x][y] = 0
        #mle pb est que quand un  pion en mange un autre les 2 s'aditionne 
        #alors on va mettre une valeur 0 par defaut afin qu'elle soit sas couleurs
    def kill_enemy(self,event,turn):
        col = event.pos[0] // SQUARE_SIZE
        row = event.pos[1] // SQUARE_SIZE
        if (row,col) in self.list_white:
            if (row-1,col-1) in self.list_black and (row-1,col-1) not in self.list_white and self.mat[row-2][col-2] == 0 and event.button == 3 :
                self.mat[row][col] =0
                self.mat[row-2][col-2] += 1
                self.mat[row-1][col-1] =0
            elif (row-1,col+1) in self.list_black and (row-1,col+1) not in self.list_white and self.mat[row-2][col+2] == 0 and event.button == 1 :
                self.mat[row][col] =0
                self.mat[row-2][col+2] += 1
                self.mat[row-1][col+1] =0
                
            


        if (row,col) in self.list_black:
            if (row+1,col+1) in self.list_white and self.mat[row+2][col+2] ==0   and event.button == 1 and row+2<8 and col+2<8:
                self.mat[row,col] =0
                self.mat[row+2][col+2] += 2
                self.mat[row+1,col+1] =0
            elif (row+1,col-1) in self.list_white and self.mat[row+2][col-2] == 0 and event.button == 3 and row+2<8 and col-2>=0 :
                
                self.mat[row,col] =0

                self.mat[row+2][col-2] += 2
                self.mat[row+1,col-1] =0
                
            

            

