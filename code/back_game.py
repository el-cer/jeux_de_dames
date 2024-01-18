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
        self.pion = True
        self.selected = None
        self.moove =  None
        self.state = None
        self.turn = None
        self.make_dame = False
        
        
        self.create_board()
        self.sides()
    

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
                color = WHITE if (row + col) % 2 == 0 else BROWN #pour chaque carre mettre 1 fois sur 2 blanc et noir
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
      
    def click(self, event, screen, row, col, click):

        # Ignore events that are not mouse clicks
        if self.selected is None and self.state is None:
            if self.mat[row][col] == 1 or self.mat[row][col] == 2:
                self.sides()

                self.selected = (row, col)
                
                self.valid_moove()
                self.can_kill()
                self.draw_future_position(screen)
                self.is_dame(row,col)
                self.state = 'selected'
                print(self.list_moove_white)
                print(self.list_moove_black)
                

                self.block_action()

                
                
        if self.state == "selected":
            if self.list_moove_black is not None and self.list_moove_white is not None and self.list_kill_moove_black is None or self.list_kill_moove_white is None :
            
                # If the state is selected, check if the second click is valid
                    # Check if the clicked position is (row-1, col+1)
                

                if  self.turn is None and self.selected in self.list_white and (row, col) == (self.selected[0] - 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1] + 1) in self.list_moove_white:

                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] - 1][self.selected[1] + 1] = 1
                    self.state = None
                    self.selected = None
                    self.list_moove_white = None
                    self.moove_yes = True
                    self.turn = 1
                    
                if  self.turn is None and  self.selected in self.list_white and (row, col) == (self.selected[0] - 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1]- 1) in self.list_moove_white:

                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] - 1][self.selected[1] - 1] = 1
                    self.state = None
                    self.selected = None 
                    self.list_moove_white = None
                    self.moove_yes = True
                    self.turn = 1
                if  self.turn == 1 and self.selected in self.list_black and (row, col) == (self.selected[0] + 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] + 1) in self.list_moove_black:

                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] + 1][self.selected[1] + 1] = 2 
                    self.state = None
                    self.selected = None
                    self.list_moove_black = None
                    self.moove_yes = True
                    self.turn = None 
                if self.turn == 1 and self.selected in self.list_black and (row, col) == (self.selected[0] + 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] - 1) in self.list_moove_black:
                    
                    self.mat[self.selected[0]][self.selected[1]] = 0
                    self.mat[self.selected[0] + 1][self.selected[1]- 1] = 2 
                    self.state = None
                    self.selected = None 
                    self.list_moove_black = None
                    self.moove_yes = True
                    self.turn = None 

                

            if self.list_kill_moove_white is not None or self.list_kill_moove_black is not None:
                    if self.turn is None and self.selected in self.list_white and (row, col) == (self.selected[0] - 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] - 2, self.selected[1] + 2) in self.list_kill_moove_white:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] - 1][self.selected[1] + 1] = 0

                        self.mat[self.selected[0] - 2][self.selected[1] + 2] = 1
                        self.state = None
                        self.selected = None 
                        self.list_kill_moove_white = None
                        self.moove_yes = True
                        self.turn = 1

                    if self.turn is None and  self.selected in self.list_white and (row, col) == (self.selected[0] - 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] - 2, self.selected[1]- 2) in self.list_kill_moove_white:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] - 1][self.selected[1] - 1] = 0
                        self.mat[self.selected[0] - 2][self.selected[1] - 2] = 1
                        self.state = None
                        self.selected = None
                        self.list_kill_moove_white = None
                        self.moove_yes = True
                        self.turn = 1
                    #BLACK
                        
                    if self.turn == 1 and self.selected in self.list_black and (row, col) == (self.selected[0] + 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] + 2, self.selected[1] + 2) in self.list_kill_moove_black:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] + 1][self.selected[1] + 1] = 0

                        self.mat[self.selected[0] + 2][self.selected[1] + 2] = 2
                        self.state = None
                        self.selected = None 
                        self.list_kill_moove_black = None
                        self.moove_yes = True
                        self.turn = None
                        

                    if self.turn == 1 and self.selected in self.list_black and (row, col) == (self.selected[0] + 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] + 2, self.selected[1]- 2) in self.list_kill_moove_black:            
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.mat[self.selected[0] + 1][self.selected[1] - 1] = 0

                        self.mat[self.selected[0] + 2][self.selected[1] - 2] = 2
                        self.state = None
                        self.selected = None 
                        self.list_kill_moove_black = None
                        self.moove_yes = True
                        self.turn = None 
    def block_action(self):
        if self.selected in self.list_white and self.list_moove_white is None and self.list_kill_moove_white is None: 
                    self.state = None 
                    self.selected = None
        elif self.turn is None and self.selected in self.list_black: 
            self.state = None 
            self.selected = None
        elif self.turn == 1 and self.selected in self.list_white: 
            self.selected = None
            self.state = None
        
    def is_dame(self,row,col):
        if self.list_white in (8,col):
            self.mat[row,col] = 3
            make_dame = True
            self.dame()


    def draw_future_position(self,screen):
            
        if self.turn is None and self.list_moove_white is not None:
            for pos in self.list_moove_white :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

        if self.turn ==1 and  self.list_moove_black is not None:   
            for pos in self.list_moove_black :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

        if self.turn is None and self.list_kill_moove_white is not None and self.list_moove_white is None :
            for pos in self.list_kill_moove_white :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

        if self.turn == 1 and self.list_kill_moove_black is not None and self.list_moove_black is None :   
            for pos in self.list_kill_moove_black :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                

              
    def draw_pieces(self, screen):
            for row in range(8):
                for col in range(8):
                    x, y = col * SQUARE_SIZE, row * SQUARE_SIZE
                    if self.mat[row, col] == 2: #si la valeur dans la matrice est 2 alors equipe noir
                        screen.blit(piece_black, (x, y))   


                    elif self.mat[row, col] == 1: #inverse
                        screen.blit(piece_white, (x, y))   
                    elif self.mat[row, col] == 3: #si la valeur dans la matrice est 2 alors equipe noir
                        pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 30)

                    
    def sides(self):
        self.list_black = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 2]
        #mettre danns une list les coordonnées des pions noir 
        self.list_white = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 1]        
        
        self.list_empty = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 0]    
    

    def valid_moove(self):
        if  (self.selected[0],self.selected[1]) in self.list_white:
            
            if  (self.selected[0]-1,self.selected[1]+1) in self.list_empty and (self.selected[0]-1,self.selected[1]-1) in self.list_empty: 
                self.list_moove_white =[(self.selected[0]-1,self.selected[1]+1),(self.selected[0]-1,self.selected[1]-1)]
                
            elif (self.selected[0]-1,self.selected[1]+1) in self.list_white or (self.selected[0]-1,self.selected[1]+1) in self.list_black  and  (self.selected[0]-2,self.selected[1]+2) in self.list_black and (self.selected[0]-1,self.selected[1]-1) in self.list_empty or  self.selected[1]+1>=8 and self.selected[0]-1>=0 and self.selected[1]-1>=0  :
                
                self.list_moove_white =[(self.selected[0]-1,self.selected[1]-1)]
            
            elif (self.selected[0]-1,self.selected[1]-1) in self.list_white or (self.selected[0]-1,self.selected[1]-1) in self.list_black and (self.selected[0]-2,self.selected[1]-2) in self.list_black  and (self.selected[0]-1,self.selected[1]+1) in self.list_empty or self.selected[0]-1<0 or self.selected[1]-1<0 and  self.selected[0]-1>=0 and self.selected[1]+1>=0:
                
                self.list_moove_white =[(self.selected[0]-1,self.selected[1]+1)]  
            
            

        elif   (self.selected[0],self.selected[1]) in self.list_black :
            
            if   (self.selected[0]+1,self.selected[1]-1) in self.list_empty and (self.selected[0]+1,self.selected[1]+1) in self.list_empty and self.selected[0]+1<8 and self.selected[1]-1>=0 and self.selected[1]+1<8 and self.selected[1]-1>=0:
              
                self.list_moove_black = [(self.selected[0]+1,self.selected[1]-1),(self.selected[0]+1,self.selected[1]+1)]
           
            elif (self.selected[0]+1,self.selected[1]-1) in self.list_black or (self.selected[0]+1,self.selected[1]-1) in self.list_white and (self.selected[0]+2,self.selected[1]-2) in self.list_white or (self.selected[0]+1,self.selected[1]+1) in self.list_empty or self.selected[1]+1>=8 and self.selected[0]+1>8 and self.selected[1]+1>8:
            
                self.list_moove_black =[(self.selected[0]+1,self.selected[1]+1)]
            
            elif (self.selected[0]+1,self.selected[1]+1) in self.list_black and  (self.selected[0]+1,self.selected[1]+1) in self.list_white and  (self.selected[0]+2,self.selected[1]-2) in self.list_white or (self.selected[0]+1,self.selected[1]-1) in self.list_empty  or self.selected[1]-1>=0 and self.selected[0]+1>8 :
            
                self.list_moove_black =[(self.selected[0]+1,self.selected[1]-1)]  
            

    def can_kill(self):

        if (self.selected[0],self.selected[1]) in self.list_white:
            
                
                if  (self.selected[0]-1,self.selected[1]-1) in self.list_black and (self.selected[0]-2,self.selected[1]-2) in self.list_empty and self.selected[0]-2>=0 and self.selected[1]-2>=0: 
                    
                    self.list_kill_moove_white =[(self.selected[0]-2,self.selected[1]-2)]
                    self.list_moove_white = None
                
                elif (self.selected[0]-2,self.selected[1]+2) in self.list_empty and (self.selected[0]-1,self.selected[1]+1) in self.list_black and self.selected[0]-2>=0 and self.selected[1]+2<8:
                    self.list_kill_moove_white =[(self.selected[0]-2,self.selected[1]+2)]
                    self.list_moove_white = None
        elif (self.selected[0],self.selected[1]) in self.list_black:
           
            if   (self.selected[0]+2,self.selected[1]-2) in self.list_empty and (self.selected[0]+1,self.selected[1]-1) in self.list_white and self.selected[0]+2<8 and self.selected[1]-2>=0:
            
                self.list_kill_moove_black =[(self.selected[0]+2,self.selected[1]-2)]
                self.list_moove_black = None
            elif (self.selected[0]+2,self.selected[1]+2) in self.list_empty and (self.selected[0]+1,self.selected[1]+1) in self.list_white and self.selected[0]+2<8 and self.selected[1]+2<8:
                self.list_kill_moove_black = [(self.selected[0]+2,self.selected[1]+2)]
                self.list_moove_black = None
                         
    def dame(self):
        if self.make_dame is True:
                list_moove_dame = self.list_moove_white+self.list_moove_black
                print(list_moove_dame)
                    
        


                
            

            

