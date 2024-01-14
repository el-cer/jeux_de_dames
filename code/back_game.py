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
        self.list_kill_moove_black = None
        self.list_kill_moove_white = None 
        self.list_moove_black,self.list_moove_white = None,None
        self.moove_yes = False
        self.draw_future_position = True
        self.pion = True
        self.selected = None
        self.moove =  None
        self.state = None
        self.yes = None
        self.turn = None

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
      
    def click(self, event, screen, row, col, click):
        # Ignore events that are not mouse clicks
        if self.selected is None and self.state is None:
            if self.mat[row][col] == 1 or self.mat[row][col] == 2:

                self.selected = (row, col)
                pygame.draw.circle(screen, GREY, (self.selected[1]+1 * SQUARE_SIZE + SQUARE_SIZE // 2, self.selected[0]-1 * SQUARE_SIZE + SQUARE_SIZE // 2),10)
                pygame.display.flip()
                self.valid_moove()

                self.can_kill()
                print(self.list_kill_moove_black,self.list_moove_black)
                
                self.state = 'selected'
        if self.state == "selected":
            if self.list_kill_moove_black is None or self.list_kill_moove_white is None :
            
                # If the state is selected, check if the second click is valid
                    # Check if the clicked position is (row-1, col+1)
                
                if  self.selected in self.list_white and (row, col) == (self.selected[0] - 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1] + 1) in self.list_moove_white:
                
                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] - 1][self.selected[1] + 1] = 1
                    self.state = None
                    self.selected = None
                    self.list_moove_white = None
                if  self.selected in self.list_white and (row, col) == (self.selected[0] - 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1]- 1) in self.list_moove_white:

                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] - 1][self.selected[1] - 1] = 1
                    self.state = None
                    self.selected = None 
                    self.list_moove_white = None

                if  self.selected in self.list_black and (row, col) == (self.selected[0] + 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] + 1) in self.list_moove_black:

                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] + 1][self.selected[1] + 1] = 2 
                    self.state = None
                    self.selected = None
                    self.list_moove_black = None

                if self.selected in self.list_black and (row, col) == (self.selected[0] + 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] - 1) in self.list_moove_black:
                    
                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] + 1][self.selected[1]- 1] = 2 
                    self.state = None
                    self.selected = None 
                    self.list_moove_black = None

            if self.list_kill_moove_white is not None or self.list_kill_moove_black is not None:
                    if self.selected in self.list_white and (row, col) == (self.selected[0] - 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] - 2, self.selected[1] + 2) in self.list_kill_moove_white:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] - 1][self.selected[1] + 1] = 0

                        self.mat[self.selected[0] - 2][self.selected[1] + 2] = 1
                        self.state = None
                        self.selected = None 
                        self.list_kill_moove_white = None


                    if  self.selected in self.list_white and (row, col) == (self.selected[0] - 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] - 2, self.selected[1]- 2) in self.list_kill_moove_white:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] - 1][self.selected[1] - 1] = 0
                        self.mat[self.selected[0] - 2][self.selected[1] - 2] = 1
                        self.state = None
                        self.selected = None
                        self.list_kill_moove_white = None
                    #BLACK
                    if self.selected in self.list_black and (row, col) == (self.selected[0] + 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] + 2, self.selected[1] + 2) in self.list_kill_moove_black:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] + 1][self.selected[1] + 1] = 0

                        self.mat[self.selected[0] + 2][self.selected[1] + 2] = 2
                        self.state = None
                        self.selected = None 
                        self.list_kill_moove_black = None
                        

                    if self.selected in self.list_black and (row, col) == (self.selected[0] + 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] + 2, self.selected[1]- 2) in self.list_kill_moove_black:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] + 1][self.selected[1] - 1] = 0

                        self.mat[self.selected[0] + 2][self.selected[1] - 2] = 2
                        self.state = None
                        self.selected = None 
                        self.list_kill_moove_black = None
    def change_turn(self):
        if self.turn is None:
            self.turn = 1
        else:
            self.turn =None                
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
    

    def valid_moove(self):
        if  (self.selected[0],self.selected[1]) in self.list_white:
            
            if  (self.selected[0]-1,self.selected[1]+1) in self.list_empty and (self.selected[0]-1,self.selected[1]-1) in self.list_empty: 
                self.list_moove_white =[(self.selected[0]-1,self.selected[1]+1),(self.selected[0]-1,self.selected[1]-1)]
            
            elif (self.selected[0]-1,self.selected[1]+1) in self.list_white or (self.selected[0]-1,self.selected[1]-1) in self.list_empty or  self.selected[1]+1>=8 and self.selected[0]-1>=0 and self.selected[1]-1>=0  :
                
                self.list_moove_white =[(self.selected[0]-1,self.selected[1]-1)]
            
            elif (self.selected[0]-1,self.selected[1]-1) in self.list_white and  self.selected[0]-1>=0 and self.selected[1]+1>=0:
                
                self.list_moove_white =[(self.selected[0]-1,self.selected[1]+1)]  
            else:
                self.list_moove_white = None
        elif   (self.selected[0],self.selected[1]) in self.list_black :
            
            if   (self.selected[0]+1,self.selected[1]-1) in self.list_empty and (self.selected[0]+1,self.selected[1]+1) in self.list_empty and self.selected[0]+1<8 and self.selected[1]-1>=0 and self.selected[1]+1<8 and self.selected[1]-1>=0:
              
                self.list_moove_black = [(self.selected[0]+1,self.selected[1]-1),(self.selected[0]+1,self.selected[1]+1)]
           
            elif (self.selected[0]+1,self.selected[1]-1) in self.list_black or (self.selected[0]+1,self.selected[1]+1) in self.list_empty or self.selected[1]+1>=8 and self.selected[0]+1>8 and self.selected[1]+1>8:
            
                self.list_moove_black =[(self.selected[0]+1,self.selected[1]+1)]
            
            elif (self.selected[0]+1,self.selected[1]+1) in self.list_black or (self.selected[0]+1,self.selected[1]-1) in self.list_empty  or self.selected[1]-1>=0 and self.selected[0]+1>8 :
            
                self.list_moove_black =[(self.selected[0]+1,self.selected[1]-1)]  
            else:
                self.list_moove_black = None
    
    def can_kill(self):

        if (self.selected[0],self.selected[1]) in self.list_white:
            
                
                if  self.mat[self.selected[0]-2][self.selected[1]-2] ==0 and (self.selected[0]-1,self.selected[1]-1) in self.list_black: 
                    
                    self.list_kill_moove_white =[(self.selected[0]-2,self.selected[1]-2)]
                
                else:
                    self.list_kill_moove_white =[(self.selected[0]-2,self.selected[1]+2)]

        elif (self.selected[0],self.selected[1]) in self.list_black and self.selected[0]+1<8 and self.selected[1]-1>=0 and self.selected[1]+1<8 and self.selected[1]-1>=0 and (self.selected[0]+1,self.selected[1]-1) in self.list_white or (self.selected[0]+1,self.selected[1]+1) in self.list_white:
           
            if   self.mat[self.selected[0]+2][self.selected[1]-2] ==0 and (self.selected[0]+1,self.selected[1]-1) in self.list_white:
            
                self.list_kill_moove_black =[(self.selected[0]+2,self.selected[1]-2)]
            else:
                self.list_kill_moove_black = [(self.selected[0]+2,self.selected[1]+2)]
            
    
                    
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
    


                
            

            

