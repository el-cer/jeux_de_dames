import pygame
import sys
import numpy as np
from config import *
import time
import game_play


class Board:
    def __init__(self,running):
        self.mat = None
        
        self.list_kill_moove_black = None
        self.list_kill_moove_white = None 
        self.list_moove_black,self.list_moove_white = None,None
        self.selected = None
        self.state = None
        self.turn = None
        self.make_dame = False
        self.moove_to = None
        self.new_click = None
        self.list_row_col = []
        self.list_moove_dame = None
        self.list_kill_moove_black_dame = None
        self.white_list_kill_dame_black = None
        self.list_kill_moove_dame_black = None
        self.list_kill_moove_dame_white = None
        self.black_list_kill_dame = None
        self.running = running
        
        self.create_board()
        self.game = game_play.game(self.mat,self.turn,running)  

        self.game.sides()

    

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
                color = WHITE if (row + col) % 2 == 0 else BROWN #pour chaque carre mettre 1 fois sur 2 blanc et marron
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
      
    def click(self,screen, row, col):
        
        
        # Ignore events that are not mouse clicks
        if self.selected is not None and self.list_kill_moove_white is not None or self.list_kill_moove_black is not None:
            self.draw_future_position(screen)

            self.state = 'selected'
            self.block_action()


        elif self.selected is None and self.state is None and self.mat[row][col] == 1 or self.mat[row][col] == 2 or self.mat[row][col] == 3 or self.mat[row][col] == 4:
                self.game.sides()
                self.selected = (row, col)
                
                

                
                self.valid_moove_white()
                self.valid_moove_black()
                self.can_kill()
                self.can_kill_dame()
                self.dame_valid_moove()
                self.draw_future_position(screen)

                

                
                
                
                                
                self.block_action()  
                print(self.selected,'l: 87')

                self.state = 'selected'
                
                
        if self.state == "selected":
            print('selected')
            if self.list_moove_black is not None and self.list_moove_white is not None or self.list_kill_moove_black is None or self.list_kill_moove_white is None :
                print(self.selected,self.list_moove_dame,'l : 94')
                if self.selected in self.game.list_dame_white or self.selected in self.game.list_dame_black:
                    if  self.turn is None and self.selected in self.game.list_dame_white  and (row, col) == (self.selected[0] - 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1] + 1) in self.list_moove_dame[0]:
                        moove_id_no_eat = 1
                        self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                        self.turn = 1
                    elif  self.turn is None and self.selected in self.game.list_dame_white  and (row, col) == (self.selected[0] - 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1] + 1) in self.list_moove_dame[0]:
                        moove_id_no_eat = 2
                        self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                        self.turn = 1
                    elif  self.turn is None and self.selected in self.game.list_dame_white and (row, col) == (self.selected[0] + 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] + 1) in self.list_moove_dame[1]:
                        moove_id_no_eat = 3
                        self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                        self.turn = 1
                    elif  self.turn is None and self.selected in self.game.list_dame_white  and (row, col) == (self.selected[0] + 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] - 1) in self.list_moove_dame[1]:
                        moove_id_no_eat = 4
                        self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                        self.turn = 1

                    elif  self.turn ==1 and self.selected in self.game.list_dame_black  and (row, col) == (self.selected[0] - 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1] + 1) in self.list_moove_dame[0]:
                            moove_id_no_eat = 6
                            self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                            self.turn = None

                    elif  self.turn ==1 and self.selected in self.game.list_dame_black and (row, col) == (self.selected[0] + 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] + 1) in self.list_moove_dame[1]:
                            moove_id_no_eat = 7
                            self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                            self.turn = None

                    elif  self.turn ==1 and self.selected in self.game.list_dame_black  and (row, col) == (self.selected[0] + 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] - 1) in self.list_moove_dame[1]:
                            moove_id_no_eat = 8
                            self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                            self.turn = None
                    
                            #moove dame 
                    if  self.turn == 1 and self.selected in self.game.list_dame_black  and (row, col) == (self.selected[0] - 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1] + 1) in self.list_moove_dame[0]:
                        moove_id_no_eat = 5
                        self.game.moove_dame_compute(self.selected,self.state,moove_id_no_eat)
                        self.turn = None

                if  self.turn is None and self.selected in self.game.list_white  and (row, col) == (self.selected[0] - 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1] + 1) in self.list_moove_white:
                    
                    self.mat[self.selected[0] - 1][self.selected[1] + 1] = self.mat[self.selected[0]][self.selected[1]]
                    self.mat[self.selected[0]][self.selected[1]] = 0

                    self.state = None
                    self.selected = None
                    
                    self.list_moove_white = None
                    self.turn = 1
                    self.moove_to = (row,col)
                    self.is_dame()

                    
                    
                if  self.turn is None and  self.selected in self.game.list_white and (row, col) == (self.selected[0] - 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] - 1, self.selected[1]- 1) in self.list_moove_white:

                    self.mat[self.selected[0] - 1][self.selected[1] - 1] = self.mat[self.selected[0]][self.selected[1]]
                    self.mat[self.selected[0]][self.selected[1]] = 0

                    self.state = None
                    self.selected = None 
                    self.list_moove_white = None

                    self.turn = 1
                    self.moove_to = (row,col)

                    self.is_dame()

                if  self.turn == 1 and self.selected in self.game.list_black and (row, col) == (self.selected[0] + 1, self.selected[1] + 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] + 1) in self.list_moove_black:

                    self.mat[self.selected[0] + 1][self.selected[1] + 1] = self.mat[self.selected[0]][self.selected[1]] 
                    self.mat[self.selected[0]][self.selected[1]] = 0

                    self.state = None
                    self.selected = None
                    self.list_moove_black = None

                    self.turn = None 
                    self.moove_to = (row,col)

                    self.is_dame()
                if self.turn == 1 and self.selected in self.game.list_black and (row, col) == (self.selected[0] + 1, self.selected[1] - 1) and self.selected is not None and (self.selected[0] + 1, self.selected[1] - 1) in self.list_moove_black:
                    
                    self.mat[self.selected[0] + 1][self.selected[1]- 1] = self.mat[self.selected[0]][self.selected[1]] 
                    self.mat[self.selected[0]][self.selected[1]] = 0

                    self.state = None
                    self.selected = None 

                    self.list_moove_black = None
                    self.turn = None 
                    self.moove_to = (row,col)
                    self.is_dame()
                

            if self.list_kill_moove_white is not None or self.list_kill_moove_black is not None or self.list_kill_moove_dame_white is not None or self.list_kill_moove_dame_black is not None:
                    
                    print('l : 188')
                    print(self.selected,self.state)
                    if self.selected in self.game.list_dame_white or self.selected in self.game.list_dame_black:
                        print('l : 194')

                        print(self.list_kill_moove_dame_black)



                        if self.turn is None and self.selected in self.game.list_dame_white and (row, col) == (self.selected[0] - 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] - 2, self.selected[1] + 2) in self.list_kill_moove_dame_white[0]:
                            moove_id_eat = 1
                            self.mat[self.selected[0] - 1][self.selected[1] + 1] = 0

                            self.mat[self.selected[0] - 2][self.selected[1] + 2] = self.mat[self.selected[0]][self.selected[1]] 
                            self.mat[self.selected[0]][self.selected[1]] = 0                        
                            self.turn = 1
                            self.selected = None
                            self.state = None
                            self.list_kill_moove_dame_white = None
                        elif  self.turn is None and self.selected in self.game.list_dame_white  and (row, col) == (self.selected[0] - 2, self.selected[1] - 2) and self.selected is not None and (self.selected[0] - 2, self.selected[1] - 2) in self.list_kill_moove_dame_white[0]:
                            self.moove_id_eat = 2   


                            self.mat[self.selected[0] - 1][self.selected[1] - 1] = 0
                            self.mat[self.selected[0] - 2][self.selected[1] - 2] = self.mat[self.selected[0]][self.selected[1]] 
                            self.mat[self.selected[0]][self.selected[1]] = 0

                            self.selected = None
                            self.state = None 
                            self.turn = 1
                            self.list_kill_moove_dame_white = None
                        if self.turn is None and self.selected in self.game.list_dame_white and (row, col) == (self.selected[0] + 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] + 2, self.selected[1] + 2) in self.list_kill_moove_dame_white[1]:            


                            self.mat[self.selected[0] + 1][self.selected[1] + 1] = 0

                            self.mat[self.selected[0] + 2][self.selected[1] + 2] = self.mat[self.selected[0]][self.selected[1]] 
                            self.mat[self.selected[0]][self.selected[1]] = 0

                            self.selected = None
                            self.state = None 
                            self.turn = 1
                        if self.turn is None and self.selected in self.game.list_dame_white and (row, col) == (self.selected[0] + 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] + 2, self.selected[1]- 2) in self.list_kill_moove_dame_white[1]:            
                        
                            self.mat[self.selected[0] + 1][self.selected[1] - 1] = 0

                            self.mat[self.selected[0] + 2][self.selected[1] - 2] =  self.mat[self.selected[0]][self.selected[1]]
                            self.mat[self.selected[0]][self.selected[1]] = 0
                            

                            self.turn = None 
                        #moove_list_dame_black    
                        if self.turn ==1 and self.selected in self.game.list_dame_black and (row, col) == (self.selected[0] - 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] - 2, self.selected[1] + 2) in self.list_kill_moove_dame_black[0]:

                            self.mat[self.selected[0] - 1][self.selected[1] + 1] = 0

                            self.mat[self.selected[0] - 2][self.selected[1] + 2] = self.mat[self.selected[0]][self.selected[1]] 
                            self.mat[self.selected[0]][self.selected[1]] = 0                        
                            self.turn = None
                            self.selected = None
                            self.state = None
                            self.list_kill_moove_dame_black = None
                        elif  self.turn ==1 and self.selected in self.game.list_dame_black  and (row, col) == (self.selected[0] - 2, self.selected[1] - 2) and self.selected is not None and (self.selected[0] - 2, self.selected[1] - 2) in self.list_kill_moove_dame_black[0]:
                            self.moove_id_eat = 2   


                            self.mat[self.selected[0] - 1][self.selected[1] - 1] = 0
                            self.mat[self.selected[0] - 2][self.selected[1] - 2] = self.mat[self.selected[0]][self.selected[1]] 
                            self.mat[self.selected[0]][self.selected[1]] = 0

                            self.selected = None
                            self.state = None 
                            self.turn = None
                            self.list_kill_moove_dame_white = None
                        if self.turn==1 and self.selected in self.game.list_dame_black and (row, col) == (self.selected[0] + 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] + 2, self.selected[1] + 2) in self.list_kill_moove_dame_black[1]:            


                            self.mat[self.selected[0] + 1][self.selected[1] + 1] = 0

                            self.mat[self.selected[0] + 2][self.selected[1] + 2] = self.mat[self.selected[0]][self.selected[1]] 
                            self.mat[self.selected[0]][self.selected[1]] = 0

                            self.selected = None
                            self.state = None 
                            self.turn = None
                        if self.turn==1 and self.selected in self.game.list_dame_black and (row, col) == (self.selected[0] + 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] + 2, self.selected[1]- 2) in self.list_kill_moove_dame_black[1]:            
                        
                            self.mat[self.selected[0] + 1][self.selected[1] - 1] = 0

                            self.mat[self.selected[0] + 2][self.selected[1] - 2] =  self.mat[self.selected[0]][self.selected[1]]
                            self.mat[self.selected[0]][self.selected[1]] = 0
                            

                            self.turn = None 
                            
                        
                             
                        

                             
                        

                            """self.moove_to = (row,col)
                            self.selected = self.moove_to

                            self.game.sides()
                            self.can_kill()
                            self.can_kill_dame()"""
                            
                            """if self.list_kill_moove_dame is not None:
                                self.turn = None
                                self.kill(screen,row,col)   
                            else:
                                selected = None
                                state = None
                                self.list_kill_moove_dame = None"""
            
                    if self.turn is None and self.selected in self.game.list_white and (row, col) == (self.selected[0] - 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] - 2, self.selected[1] + 2) in self.list_kill_moove_white:            
                        
                        self.mat[self.selected[0] - 1][self.selected[1] + 1] = 0

                        self.mat[self.selected[0] - 2][self.selected[1] + 2] = self.mat[self.selected[0]][self.selected[1]] 
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        
                        self.list_kill_moove_white = None

                        self.moove_to = (row,col)
                        self.selected = self.moove_to
                        self.game.sides()
                        self.can_kill()
                        
                        
                        if self.list_kill_moove_white is not None:
                            self.kill(screen,row,col)   
                        else:
                            self.selected = None
                            self.state = None 
                            self.turn = 1
                  
                        
                        self.is_dame()


                    if self.turn is None and  self.selected in self.game.list_white and (row, col) == (self.selected[0] - 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] - 2, self.selected[1]- 2) in self.list_kill_moove_white:            
                        self.mat[self.selected[0] - 1][self.selected[1] - 1] = 0
                        self.mat[self.selected[0] - 2][self.selected[1] - 2] = self.mat[self.selected[0]][self.selected[1]] 
                        self.mat[self.selected[0]][self.selected[1]] = 0

                        self.list_kill_moove_white = None
                        
                        self.turn = 1
                        self.moove_to = (row,col)
                        self.selected = self.moove_to
                        self.game.sides()
                        self.can_kill()

                        if self.list_kill_moove_white is not None:
                            self.turn = None
                            self.kill(screen,row,col)   
                        else:
                            self.selected = None
                            self.state = None
                        
                        self.is_dame()

                    #BLACK
                        
                    if self.turn == 1 and self.selected in self.game.list_black and (row, col) == (self.selected[0] + 2, self.selected[1] + 2) and self.selected is not None and (self.selected[0] + 2, self.selected[1] + 2) in self.list_kill_moove_black:            
                        self.mat[self.selected[0] + 1][self.selected[1] + 1] = 0

                        self.mat[self.selected[0] + 2][self.selected[1] + 2] = self.mat[self.selected[0]][self.selected[1]] 
                        self.mat[self.selected[0]][self.selected[1]] = 0

                        self.list_kill_moove_black = None

                        self.turn = None
                        self.moove_to = (row,col)
                        self.selected = self.moove_to
                        self.game.sides()
                        self.can_kill()

                        if self.list_kill_moove_black is not None:
                            self.turn = 1
                            self.kill(screen,row,col)   
                        else:
                            self.selected = None
                            self.state = None
                        
                        
                        self.is_dame()

                        

                    if self.turn == 1 and self.selected in self.game.list_black and (row, col) == (self.selected[0] + 2, self.selected[1] -2) and self.selected is not None and (self.selected[0] + 2, self.selected[1]- 2) in self.list_kill_moove_black :            
                        
                        self.mat[self.selected[0] + 1][self.selected[1] - 1] = 0

                        self.mat[self.selected[0] + 2][self.selected[1] - 2] =  self.mat[self.selected[0]][self.selected[1]]
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        

                        self.list_kill_moove_black = None

                        self.turn = None 
                        self.moove_to = (row,col)
                        self.selected = self.moove_to
                        self.game.sides()
                        self.can_kill()
                        
                        if self.list_kill_moove_black is not None:
                            self.turn = 1
                            self.kill(screen,row,col)   
                        else:
                            self.selected = None
                            self.state = None
                        
                             
                        
                        self.is_dame()
            self.game.winner()
            self.running = self.game.running
        
    def click_dame(row,col):
        pass 

    

        """elif self.selected  in self.list_row_col:
                self.list_row_col.remove(self.selected)
        if len(self.list_row_col)>1:    
                for first in self.game.list_white:
                    for last in self.list_row_col:
                        if last == first:
                            print(self.selected)
                            self.selected = None
                            self.selected = last
                            print(self.selected)
                            self.state = "selected"""
 
        
    def is_dame(self):
        if self.moove_to[0]==0 :
            self.make_dame =True
            self.mat[self.moove_to[0],self.moove_to[1]] = 3
        elif self.moove_to[0]==7:
            self.make_dame =True
            self.mat[self.moove_to[0],self.moove_to[1]] = 4
        else:
             pass



    def draw_future_position(self,screen):
            
        if self.turn is None and self.list_moove_white is not None:
            for pos in self.list_moove_white :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

                print('l : 379')
        if self.turn is None and  self.selected in self.game.list_dame_white and self.list_moove_white is not None:
            for pos in self.list_moove_white :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 383')
        if self.turn is None and  self.selected in self.game.list_dame_white and self.list_moove_black is not None:
            for pos in self.list_moove_black :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 387')

        if self.turn == 1 and  self.selected in self.game.list_dame_black and self.list_moove_white is not None :
            for pos in self.list_moove_white :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 392')

        if self.turn == 1 and  self.selected in self.game.list_dame_black and self.list_moove_black is not None:
            for pos in self.list_moove_black :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 397')


        if self.turn ==1 and  self.list_moove_black is not None:   
            for pos in self.list_moove_black :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 403')

        if self.turn is None and self.list_kill_moove_white is not None and self.list_moove_white is None :
            for pos in self.list_kill_moove_white :
                print(self.selected)
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 408')
                print(self.list_kill_moove_white,'408')

        if self.turn is None and self.black_list_kill_dame is not None and self.selected in self.game.list_dame_white :
            for pos in self.black_list_kill_dame:
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 413')

        if self.turn == 1 and self.list_kill_moove_black is not None and self.list_moove_black is None :   
            for pos in self.list_kill_moove_black :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), 10)
                print('l : 418')
        
        
        
        

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
                    elif self.mat[row, col] == 4: #si la valeur dans la matrice est 2 alors equipe noir
                        pygame.draw.circle(screen, BROWN, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 30)

                    
    def block_action(self):
        """if self.selected in self.game.list_white  and self.list_moove_white is None and self.list_kill_moove_white is None: 
                    print('l: 455')
                    self.state = None 
                    self.selected = None"""
        """if self.selected in self.game.list_black and self.list_moove_black is None and self.list_kill_moove_black is None: 
                    print('l: 459')
                    self.state = None 
                    self.selected = None"""
        if self.turn is None and self.selected in self.game.list_black: 
            print('l: 463')
            self.state = None 
            self.selected = None
            self.turn = None
        elif self.turn == 1 and self.selected in self.game.list_white: 
            print('l: 468')
            self.selected = None
            self.state = None
            self.turn = 1
        

    def valid_moove_white(self):
        self.list_kill_moove_white = None
        if self.list_kill_moove_white is None:   
            if  (self.selected[0],self.selected[1]) in self.game.list_white or (self.selected[0],self.selected[1]) in self.game.list_dame_black or (self.selected[0],self.selected[1]) in self.game.list_dame_white:
                if (self.selected[0]-1,self.selected[1]+1) not in self.game.list_empty and (self.selected[0]-1,self.selected[1]-1) not in self.game.list_empty:
                    self.list_moove_white = None
                    print('l:465')
     
                elif  (self.selected[0]-1,self.selected[1]+1) in self.game.list_empty and (self.selected[0]-1,self.selected[1]-1) in self.game.list_empty: 
                    self.list_moove_white =[(self.selected[0]-1,self.selected[1]+1),(self.selected[0]-1,self.selected[1]-1)]
                    print('l:469')
                    
                elif (self.selected[0]-1,self.selected[1]-1) in self.game.list_empty and (self.selected[0]-1,self.selected[1]+1) not in self.game.list_empty   or  self.selected[1]+1>=8 and self.selected[0]-1>=0 and self.selected[1]-1>=0  :
                    
                    self.list_moove_white =[(self.selected[0]-1,self.selected[1]-1)]
                    print('l:474')
                elif (self.selected[0]-1,self.selected[1]-1) not in self.game.list_empty and (self.selected[0]-1,self.selected[1]+1) in self.game.list_empty or self.selected[0]-1<0 or self.selected[1]-1<0 and  self.selected[0]-1>=0 and self.selected[1]+1>=0:
                    self.list_moove_white =[(self.selected[0]-1,self.selected[1]+1)]  
                    print('l:477')
                
    def valid_moove_black(self):  
        if self.list_kill_moove_black is None:
            if   (self.selected[0],self.selected[1]) in self.game.list_black or (self.selected[0],self.selected[1]) in self.game.list_dame_black or (self.selected[0],self.selected[1]) in self.game.list_dame_white:
                if (self.selected[0]+1,self.selected[1]+1) not in self.game.list_empty and (self.selected[0]+1,self.selected[1]-1) not in self.game.list_empty:
                    self.list_moove_black = None   
                    print('l : 486')
                elif   (self.selected[0]+1,self.selected[1]-1) in self.game.list_empty and (self.selected[0]+1,self.selected[1]+1) in self.game.list_empty and self.selected[0]+1<8 and self.selected[1]-1>=0 and self.selected[1]+1<8 and self.selected[1]-1>=0:
                
                    self.list_moove_black = [(self.selected[0]+1,self.selected[1]-1),(self.selected[0]+1,self.selected[1]+1)]
                    print('l : 490')
                
                elif (self.selected[0]+1,self.selected[1]+1) in self.game.list_empty and (self.selected[0]+1,self.selected[1]-1) not in self.game.list_empty   and self.selected[1]+1<8 and self.selected[0]+1<8 and self.selected[1]+1<8:
                    self.list_moove_black =[(self.selected[0]+1,self.selected[1]+1)]

                    print('l : 495')
                elif (self.selected[0]+1,self.selected[1]-1) in self.game.list_empty and (self.selected[0]+1,self.selected[1]+1) not in self.game.list_empty and (self.selected[0]+2,self.selected[1]+2) not in self.game.list_empty and self.selected[1]-1>=0 and self.selected[0]+1<8 :
                    self.list_moove_black =[(self.selected[0]+1,self.selected[1]-1)]  
                    print(self.list_moove_black)
                    print('l :499')
                
                else:
                    self.list_moove_black = None
            
                

    def can_kill(self):
        self.game.list_white += self.game.list_dame_white
        self.game.list_black += self.game.list_dame_black

        if (self.selected[0],self.selected[1]) in self.game.list_white or (self.selected[0],self.selected[1]) in self.game.list_dame_white:      
            
            if  (self.selected[0]-1,self.selected[1]-1) in self.game.list_black and (self.selected[0]-2,self.selected[1]-2) in self.game.list_empty and self.selected[0]-2>=0 and self.selected[1]-2>=0: 
                self.list_kill_moove_white =[(self.selected[0]-2,self.selected[1]-2)]
                self.list_moove_white = None
                print('l 507')


            
            elif (self.selected[0]-2,self.selected[1]+2) in self.game.list_empty and (self.selected[0]-1,self.selected[1]+1) in self.game.list_black and self.selected[0]-2>=0 and self.selected[1]+2<8:
                self.list_kill_moove_white =[(self.selected[0]-2,self.selected[1]+2)]
                self.list_moove_white = None

                print('l 512')
        elif (self.selected[0],self.selected[1]) in self.game.list_black or (self.selected[0],self.selected[1]) in self.game.list_dame_black:

            if   (self.selected[0]+2,self.selected[1]-2) in self.game.list_empty and (self.selected[0]+1,self.selected[1]-1) in self.game.list_white and self.selected[0]+2<8 and self.selected[1]-2>=0:
                self.list_kill_moove_black =[(self.selected[0]+2,self.selected[1]-2)]
                self.list_moove_black = None
                print('l 519')

            elif (self.selected[0]+2,self.selected[1]+2) in self.game.list_empty and (self.selected[0]+1,self.selected[1]+1) in self.game.list_white and self.selected[0]+2<8 and self.selected[1]+2<8:
                self.list_kill_moove_black = [(self.selected[0]+2,self.selected[1]+2)]
                self.list_moove_black = None
                print('l 524')
                  
    def can_kill_dame(self):
        self.game.list_black += self.game.list_dame_black
        if (self.selected[0],self.selected[1]) in self.game.list_dame_white:
            if   (self.selected[0]+2,self.selected[1]-2) in self.game.list_empty and (self.selected[0]+1,self.selected[1]-1) in self.game.list_black and self.selected[0]+2<8 and self.selected[1]-2>=0:
                self.black_list_kill_dame =[(self.selected[0]+2,self.selected[1]-2)]
                self.list_moove_black = None
                print('l : 532')

            elif (self.selected[0]+2,self.selected[1]+2) in self.game.list_empty and (self.selected[0]+1,self.selected[1]+1) in self.game.list_black and self.selected[0]+2<8 and self.selected[1]+2<8:
                self.black_list_kill_dame = [(self.selected[0]+2,self.selected[1]+2)]

                self.list_moove_black = None
                print('l : 539')

        if (self.selected[0],self.selected[1]) in self.game.list_dame_black:      
            
            if  (self.selected[0]-1,self.selected[1]-1) in self.game.list_white and (self.selected[0]-2,self.selected[1]-2) in self.game.list_empty and self.selected[0]-2>=0 and self.selected[1]-2>=0: 
                self.white_list_kill_dame_black =[(self.selected[0]-2,self.selected[1]-2)]
                self.list_moove_white = None
                print('l : 546')
            
            elif (self.selected[0]-2,self.selected[1]+2) in self.game.list_empty and (self.selected[0]-1,self.selected[1]+1) in self.game.list_white and self.selected[0]-2>=0 and self.selected[1]+2<8:
                self.white_list_kill_dame_black =[(self.selected[0]-2,self.selected[1]+2)]
                self.list_moove_white = None
                print('l : 551')
    
    

                
            
    def dame_valid_moove(self):
        if self.selected in self.game.list_dame_white or self.selected in self.game.list_dame_black  :
            if  self.list_moove_white  is not None or self.list_moove_black  is not None:  
                self.list_moove_dame = [self.list_moove_white,self.list_moove_black]
                print('l : 563')
            else:
                self.list_moove_dame = (None,None)
        
        if self.selected in self.game.list_dame_black :
                self.list_moove_white = None
                self.list_moove_black = None
                self.list_kill_moove_dame_black = [self.white_list_kill_dame_black,self.list_kill_moove_black]
                print('l: 572')

        if self.selected in self.game.list_dame_white:
                
        
                    self.list_moove_white = None
                    self.list_moove_black = None
                    self.list_kill_moove_dame_white = [self.list_kill_moove_white,self.black_list_kill_dame]
                    
                    print('l:582')

    def kill(self,screen,row,col):
            
            if self.list_kill_moove_white or  self.list_moove_black is not None:
                self.click(screen,row,col)
                
                
            elif self.list_kill_moove_dame is not None:
                self.click(screen,row,col)
        
        
    
            
        
            

