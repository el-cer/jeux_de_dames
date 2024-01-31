import pygame
import sys
import numpy as np
from config import *
import time
import game_play


class Board:
    def __init__(self,running):
        self.mat = None
        
        self.dame_movements = []


        self.black_eat_movement_list = []
        self.white_piece_eat_movement_list = [] 
        self.black_movement_list,self.white_movement_list = [],[]
        self.selected = None
        self.state = None
        self.turn = None
        self.make_dame = False
        self.moove_to = None


        self.list_row_col_main = None

        self.new = None

        self.running = running

        self.last_position = None
        self.other_click = None 

        self.list_eat_dame_black = []
        self.list_eat_dame_white = []
        self.tuple = None


        self.create_board()
        self.game = game_play.game(self.mat,running)  #initialisation d'une autre class de la file back_game.py

        self.game.sides() #cette fonction permet defaire des liste de chaque pions

    

    def create_board(self):
        self.mat = np.array([[ 0, 2, 0, 2, 0, 2, 0, 2],
                             [ 2, 0, 2, 0, 2, 0, 2, 0],
                             [ 0, 2, 0, 2, 0, 2, 0, 2],
                             [ 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 0, 0, 0, 0, 0, 0, 0, 0],
                             [ 1, 0, 1, 0, 1, 0, 1, 0],                                                                                                                                                                                                                                
                             [ 0, 1, 0, 1, 0, 1, 0, 1],
                             [ 1, 0, 1, 0, 1, 0, 1, 0]])

        # Matrice de 8x8 avec Pour les 3 premiere lige des valeurs 2 pour noir et 1 pour blanc
    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = BROWN if (row + col) % 2 == 0 else WHITE #pour chaque carre mettre 1 fois sur 2 blanc et marron
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
      
    def draw_pieces(self, screen):
            for row in range(8):
                for col in range(8):
                    x, y = col * SQUARE_SIZE, row * SQUARE_SIZE
                    if self.mat[row, col] == 2: #si la valeur dans la matrice est 2 alors equipe noir
                        screen.blit(piece_black, (x, y))   
                        #screen.blit permet de mettre une image sur le board
                    elif self.mat[row, col] == 1: #inverse
                        screen.blit(piece_white, (x, y))   
                    
                    elif self.mat[row, col] == 3: 
                         screen.blit(white_dame, (x, y))  
                    elif self.mat[row, col] == 4: 
                         screen.blit(black_dame, (x, y))  
                    
    def click(self,screen, row, col):
        
       
        
        if self.selected is not None and len(self.white_piece_eat_movement_list)>0 or len(self.black_eat_movement_list)>0 or len(self.list_eat_dame_white)>0 or len(self.list_eat_dame_black)>0:
            #self.selected can be not None if a  piece can re eat
            self.draw_future_position(screen)


            self.state = 'selected'
            self.game.block_action(self.selected,self.turn,self.state,self.white_movement_list,self.black_movement_list,self.dame_movements,self.white_piece_eat_movement_list,self.black_eat_movement_list,self.list_eat_dame_black,self.list_eat_dame_white)
            
            self.selected = self.game.selected
            self.state = self.game.state
            self.turn = self.game.turn 

        elif self.selected is None and self.state is None and self.mat[row][col] !=0:
                self.game.sides()
                
                self.selected = (row,col)

                self.can_eat()
                self.valid_moove_white()
                
                self.valid_moove_black()
                
                
                self.valid_eat_moove_dam_white()

                
                self.valid_eat_moove_dam_black()
                
                if self.selected in self.game.list_dame_white and len(self.list_eat_dame_white)==0:
                    self.valid_moove_dam()
                    
                if self.selected in self.game.list_dame_black and len(self.list_eat_dame_black)==0:
                    self.valid_moove_dam()
                
                self.state = 'selected'
                self.game.block_action(self.selected,self.turn,self.state,self.white_movement_list,self.black_movement_list,self.dame_movements,self.white_piece_eat_movement_list,self.black_eat_movement_list,self.list_eat_dame_black,self.list_eat_dame_white) 
                
                self.selected = self.game.selected
                self.state = self.game.state
                self.turn = self.game.turn 

                
                self.draw_future_position(screen)
         
        if self.state == "selected":
            
            if (row,col) != self.selected: 
                #so we want the second click and the first is the self.selected
                self.other_click = (row,col)
                self.cancel_click()


            if len(self.dame_movements)>0 or len(self.white_movement_list)>0 or len(self.black_movement_list)>0:
                #DAME MOVEMENTS
                if self.turn is None and self.selected in self.game.list_dame_white:
                    if (row,col) in self.dame_movements:
                        self.mat[row,col] = self.mat[self.selected[0]][self.selected[1]]
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.turn = 1
                        self.selected = None 
                        self.state = None
                        self.dame_movements = None
                        self.dame_movements = []

                if self.turn==1 and self.selected in self.game.list_dame_black:    
                    if (row,col) in self.dame_movements:
                        self.mat[row,col] = self.mat[self.selected[0]][self.selected[1]]
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        self.turn = None
                        self.selected = None 
                        self.state = None
                        self.dame_movements = None
                        self.dame_movements = []

                #PIECES MOVEMENTS
                if  self.turn is None and self.selected in self.game.list_white and (row,col) in self.white_movement_list:
                    
                    self.mat[row,col] = self.mat[self.selected[0]][self.selected[1]]
                    self.mat[self.selected[0]][self.selected[1]] = 0

                    self.state = None
                    self.selected = None
                    self.white_movement_list =  None
                    self.white_movement_list = []
                    self.turn = 1
                    self.moove_to = (row,col)
                    self.is_dame()



                if  self.turn == 1 and self.selected in self.game.list_black and (row,col) in self.black_movement_list:

                    self.mat[row,col] = self.mat[self.selected[0]][self.selected[1]] 
                    self.mat[self.selected[0]][self.selected[1]] = 0

                    self.state = None
                    self.selected = None
                    self.black_movement_list = None
                    self.black_movement_list = []
                    self.moove_to = (row,col)

                    self.turn = None
                    self.is_dame()
 

            if len(self.black_eat_movement_list)>0 or len(self.white_piece_eat_movement_list)>0  or len(self.list_eat_dame_white)>0 or len(self.list_eat_dame_black)>0:


                    if self.selected in self.game.list_dame_white or self.selected in self.game.list_dame_black:
                        if  self.turn is None and self.selected in self.game.list_dame_white and (row,col) in self.list_eat_dame_white:
                            
                                new = self.assign_tuple()  #explication en ligne 614

                                self.mat[new[0]][new[1]] = 0
                                self.mat[row][col] = self.mat[self.selected[0]][self.selected[1]] 
                                self.mat[self.selected[0]][self.selected[1]] = 0

                                self.selected = None
                                self.state = None 
                                
                                
                                self.selected = (row,col)
                                self.list_eat_dame_white = None
                                self.list_eat_dame_white = []
                    
                                self.game.sides()
                                self.valid_eat_moove_dam_white()

                                if len(self.list_eat_dame_white)>0:
                                    self.turn = None
                                    self.eat(screen,row,col)   
                                else:
                                    self.selected = None
                                    self.state  = None
                                    self.turn = 1
                                    self.list_eat_dame_white = []

                                    
                                
                        
                        #moove_list_dame_black  
                              
                        if self.turn ==1 and self.selected in self.game.list_dame_black and (row,col) in self.list_eat_dame_black:
                            new = self.assign_tuple()
                            self.mat[new[0]][new[1]] = 0
                            self.mat[row,col] = self.mat[self.selected[0]][self.selected[1]] 
                            self.mat[self.selected[0]][self.selected[1]] = 0

                            self.selected = None
                            self.state = None 
                            
                            self.moove_to = (row,col)
                            self.selected = self.moove_to
                            self.list_eat_dame_black = None
                            self.list_eat_dame_black = []
                            self.turn = 1
                
                            self.game.sides()
                            self.valid_eat_moove_dam_black()
            
                            if len(self.list_eat_dame_black)>0:
                                self.turn = 1
                                self.eat(screen,row,col)   
                            else:
                                self.selected = None
                                self.selected = None
                                self.list_eat_dame_black = []
                                self.turn = None
                    




                            print(self.selected,'l_483')
                    #EAT WHITE piece
                    if self.turn is None and self.game.list_white and (row,col) in self.white_piece_eat_movement_list:
                        self.mat[self.tuple[0]][self.tuple[1]] = 0

                        self.mat[row,col] = self.mat[self.selected[0]][self.selected[1]] 
                        self.mat[self.selected[0]][self.selected[1]] = 0

                        self.white_piece_eat_movement_list = None
                        self.white_piece_eat_movement_list = []
                        self.moove_to = (row,col)
                        self.selected = self.moove_to
                        self.game.sides()
                        self.can_eat()
                        
                        
                        if len(self.white_piece_eat_movement_list)>0:
                            self.turn = None
                            self.eat(screen,row,col)   
                        else:
                            self.selected = None
                            self.state = None 
                            self.turn = 1
                  
                        
                        self.is_dame()

                    #BLACK
                        
                    if self.turn == 1 and self.selected in self.game.list_black and (row,col) in self.black_eat_movement_list:
                        self.mat[self.tuple[0]][self.tuple[1]] = 0

                        self.mat[row,col] =  self.mat[self.selected[0]][self.selected[1]]
                        self.mat[self.selected[0]][self.selected[1]] = 0
                        
                        self.black_eat_movement_list = None
                        self.black_eat_movement_list = []

                        
                        self.moove_to = (row,col)
                        self.selected = self.moove_to #permet de recalculé si la piece a des coups a faire
                        self.game.sides()
                        self.can_eat()
                        
                        if len(self.black_eat_movement_list)>0:
                            self.turn = 1
                            self.eat(screen,row,col) 
                            self.selected = self.moove_to
                            self.state = "selected"
  
                        else:
                            self.selected = None
                            self.state = None
                            self.turn = None 
                        
                             
                        
                        self.is_dame()
            self.game.winner(self.turn) #chaque fin de coup la fonction winner analyse la len de chaque list 
            #si len==0 alors winner du coté opposé
            self.running = self.game.running
          
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
        if self.turn is None and self.selected in self.game.list_white and len(self.white_movement_list)>0:
            for pos in self.white_movement_list :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)
        
        if self.turn is None and self.selected in self.game.list_white and len(self.white_piece_eat_movement_list)>0:
            for pos in self.white_piece_eat_movement_list :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)

        if self.turn is None and  self.selected in self.game.list_dame_white and len(self.dame_movements)>0:
            for pos in self.dame_movements :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)
        
        if self.turn is None and  self.selected in self.game.list_dame_white and len(self.list_eat_dame_white)>0:
            for pos in self.list_eat_dame_white :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)

        #COLOR black        

        
        if self.turn ==1  and self.selected in self.game.list_black and  len(self.black_movement_list)>0:   
            for pos in self.black_movement_list :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)
        
        if self.turn ==1 and self.selected in self.game.list_black and  len(self.black_eat_movement_list)>0:   
            for pos in self.black_eat_movement_list :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)

        #list_dame_black        
        if self.turn == 1 and self.selected in self.game.list_dame_black    and len(self.dame_movements)>0 :   
            for pos in self.dame_movements :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)
        
        if self.turn == 1 and self.selected in self.game.list_dame_black    and len(self.list_eat_dame_black)>0:   
            for pos in self.list_eat_dame_black :
                pygame.draw.circle(screen, BLUE, (pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS_FUTURE_POSITION)
        
   

    def cancel_click(self):#this function cancel the piece selected if you want to click on another piece
        
        
        if self.selected in self.game.list_white and self.selected not in self.game.list_dame_white and self.turn is None  and self.state=="selected" and len(self.white_piece_eat_movement_list)==0  and self.other_click not in self.white_movement_list:
            self.selected = None
            self.state = None 
            self.turn = None
            self.white_movement_list = []

        if self.selected in self.game.list_white and self.selected not in self.game.list_dame_white and self.turn is None and self.state=="selected" and len(self.white_piece_eat_movement_list)>0  and self.other_click not in self.white_piece_eat_movement_list:
            self.selected = None
            self.state = None 
            self.turn = None
            self.white_piece_eat_movement_list = []
            self.other_click = None 
            self.tuple = None

        if self.selected in self.game.list_black and self.selected not in self.game.list_dame_black and self.turn==1 and self.state=="selected" and len(self.black_eat_movement_list)==0 and self.selected in self.game.list_black and self.other_click not in self.black_movement_list:
            self.selected = None
            self.state = None 
            self.turn = 1
            self.black_movement_list = []

        if self.selected in self.game.list_black and self.selected not in self.game.list_dame_black and  self.turn==1 and self.state=="selected" and len(self.black_eat_movement_list)>0 and self.selected in self.game.list_black and self.other_click not in self.black_eat_movement_list:
            self.selected = None
            self.state = None 
            self.tuple = None
            self.turn = 1
            self.black_eat_movement_list = []

        if self.selected in self.game.list_dame_white and self.turn is None and self.state=="selected" and len(self.list_eat_dame_white)==0  and self.other_click not in self.dame_movements: 

                self.selected = None
                self.state  = None 
                self.turn = None
                self.tuple = None
                self.dame_movements = []
        if self.selected in self.game.list_dame_white and self.turn is None and self.state=="selected" and len(self.list_eat_dame_white)>0  and self.other_click not in self.list_eat_dame_white: 

                self.selected = None
                self.state  = None 
                self.turn = None
                self.tuple = None
                self.dame_movements = []

        if self.selected in self.game.list_dame_black and self.turn==1 and self.state=="selected" and len(self.list_eat_dame_black)==0  and self.other_click not in self.dame_movements: 

                self.selected = None
                self.state  = None 
                self.turn = None
                self.tuple = None
                self.dame_movements = []
        if self.selected in self.game.list_dame_black and self.turn is None and self.state=="selected" and len(self.list_eat_dame_black)>0  and self.other_click not in self.list_eat_dame_black: 

                self.selected = None
                self.state  = None 
                self.turn = None
                self.tuple = None
                self.dame_movements = []
        
    def valid_moove_white(self):
        if  self.turn is None and (self.selected[0],self.selected[1]) in self.game.list_white:
            if len(self.white_piece_eat_movement_list)==0: 
                print(self.selected,'l_445')  
                for row in str(self.selected[0]):
                        for col in str(self.selected[1]): 
                        
                                if (int(row)-1,int(col)+1) not in self.game.list_empty and (int(row)-1,int(col)-1) not in self.game.list_empty:
                                    self.white_movement_list = []
                                    
                    
                                elif  (int(row)-1,int(col)+1) in self.game.list_empty and (int(row)-1,int(col)-1) in self.game.list_empty: 
                                    self.white_movement_list.append((int(row)-1,int(col)+1))
                                    self.white_movement_list.append((int(row)-1,int(col)-1))
                                    
                                elif (int(row)-1,int(col)-1) in self.game.list_empty and (int(row)-1,int(col)+1) not in self.game.list_empty   or  int(col)+1>=8 and int(row)-1>=0 and int(col)-1>=0  :
                                    
                                    self.white_movement_list.append((int(row)-1,int(col)-1))
                                elif (int(row)-1,int(col)-1) not in self.game.list_empty and (int(row)-1,int(col)+1) in self.game.list_empty or int(row)-1<0 or int(col)-1<0 and  int(row)-1>=0 and int(col)+1>=0:
                                    self.white_movement_list.append((int(row)-1,int(col)+1))  
                                       
                                    
    def valid_moove_black(self): 
        if  self.turn==1 and  (self.selected[0],self.selected[1]) in self.game.list_black:
            if len(self.black_eat_movement_list)==0:
                
                for row in str(self.selected[0]):
                        for col in str(self.selected[1]): 
                                
                                    if (int(row)+1,int(col)+1) not in self.game.list_empty and (int(row)+1,int(col)-1) not in self.game.list_empty:
                                        self.black_movement_list = []   
                                    
                                    elif   (int(row)+1,int(col)-1) in self.game.list_empty and (int(row)+1,int(col)+1) in self.game.list_empty and int(row)+1<8 and int(col)-1>=0 and int(col)+1<8 and int(col)-1>=0:
                                        self.black_movement_list.append((int(row)+1,int(col)+1))
                                        self.black_movement_list.append((int(row)+1,int(col)-1))

                                    
                                    elif (int(row)+1,int(col)+1) in self.game.list_empty and (int(row)+1,int(col)-1) not in self.game.list_empty   and int(col)+1<8 and int(row)+1<8 and int(col)+1<8:
                                        self.black_movement_list.append((int(row)+1,int(col)+1))

                                    elif (int(row)+1,int(col)-1) in self.game.list_empty and (int(row)+1,int(col)+1) not in self.game.list_empty and int(col)-1>=0 and int(row)+1<8 :
                                        self.black_movement_list.append((int(row)+1,self.selected[1]-1))
                                    
                                    
                    
                

    def can_eat(self):
        
            #fonction eat 
            if self.turn is None and (self.selected[0],self.selected[1]) in self.game.list_white:      
                
                if  (self.selected[0]-2,self.selected[1]-2) in self.game.list_empty and (self.selected[0]-1,self.selected[1]-1) in self.game.list_black or (self.selected[0]-1,self.selected[1]-1) in self.game.list_dame_black  and self.selected[0]-2>=0 and self.selected[1]-2>=0: 
                    self.white_piece_eat_movement_list.append((self.selected[0]-2,self.selected[1]-2))
                    self.tuple = (self.selected[0]-1,self.selected[1]-1)
                    self.white_movement_list = []


                
                elif (self.selected[0]-2,self.selected[1]+2) in self.game.list_empty and (self.selected[0]-1,self.selected[1]+1) in self.game.list_black or (self.selected[0]-1,self.selected[1]+1) in self.game.list_dame_black and self.selected[0]-2>=0 and self.selected[1]+2<8:
                    self.white_piece_eat_movement_list.append((self.selected[0]-2,self.selected[1]+2))
                    self.tuple = (self.selected[0]-1,self.selected[1]+1)

                    self.white_movement_list = []

            elif self.turn ==1 and (self.selected[0],self.selected[1]) in self.game.list_black:

                if   (self.selected[0]+2,self.selected[1]-2) in self.game.list_empty and (self.selected[0]+1,self.selected[1]-1) in self.game.list_white or (self.selected[0]+1,self.selected[1]-1) in self.game.list_dame_white and self.selected[0]+2<8 and self.selected[1]-2>=0:
                    self.black_eat_movement_list.append((self.selected[0]+2,self.selected[1]-2))
                    self.tuple = (self.selected[0]+1,self.selected[1]-1)
                    
                    self.black_movement_list = []

                elif (self.selected[0]+2,self.selected[1]+2) in self.game.list_empty and (self.selected[0]+1,self.selected[1]+1) in self.game.list_white or (self.selected[0]+1,self.selected[1]+1) in self.game.list_dame_white and self.selected[0]+2<8 and self.selected[1]+2<8:
                    self.black_eat_movement_list.append((self.selected[0]+2,self.selected[1]+2))
                    self.tuple = (self.selected[0]+1,self.selected[1]+1)
                    self.black_movement_list = []


    def valid_moove_dam(self):
    
        self.list_moove_tuples = []
        #ATTENTION cette fonction ne s'active que si la liste eat dame est pas vide 
        if self.selected in self.game.list_dame_white or self.selected in self.game.list_dame_black:
            self.pieces = self.game.list_black+self.game.list_white
            
            for i in range(1,8):
                if self.selected[0]-i>=0 and self.selected[1]-i>=0:
                    self.dame_movements.append((self.selected[0]-i, self.selected[1]-i)) #on rajoute dans la liste
                    # toute les pieces ou il y a (self.selected[0]-i, self.selected[1]-i)
                    for value in self.dame_movements: #boucle sur la list et value = (x,y) ou x=row et y= col
                        if value in self.pieces: #on enleve toute les pieces ou il y a des pieces
                            #et on garde les piece ou il y a des pieces vides
                            
                              self.dame_movements.remove(value)
                            
                if self.selected[0]-i>=0 and self.selected[1]+i<=7:
                    self.dame_movements.append((self.selected[0]-i, self.selected[1]+i))
                    for value in self.dame_movements:
                         if value in self.pieces:
                              self.dame_movements.remove(value)
                if self.selected[0]+i<=7 and self.selected[1]-i>=0:
                    self.dame_movements.append((self.selected[0]+i, self.selected[1]-i))
                    for value in self.dame_movements:
                         if value in self.pieces :
                              self.dame_movements.remove(value)
                if self.selected[0]+i<=7 and self.selected[1]+i<=7:
                    self.dame_movements.append((self.selected[0]+i, self.selected[1]+i))
                    for value in self.dame_movements:
                         if value in self.pieces:
                              self.dame_movements.remove(value)
                        
            
                            
                        
                            
 
                                    
    def valid_eat_moove_dam_black(self):
            id_eat_black = None
            if self.turn==1 and self.selected in self.game.list_dame_black:
                self.dame_movements =[]
                self.list_index_dame_black = [None] * 4 
                self.list_row_col_main = [None]*4
                for row in str(self.selected[0]):
                    for col in str(self.selected[1]):
                        for i in range(1,8):
 
                                    if (int(row)-i,int(col)-i) in self.game.list_white or (int(row)-i,int(col)-i) in self.game.list_dame_white:
                                            #parcour de list (row-i,col-i)----> diagonale gauche . 
                                            value = (int(row)-i,int(col)-i) #value enregistre le moment ou ou (row-i,col-i) est d'une piece de la couleur opposée
                                            id_eat_black = 0
                                            
                                            if  int(row)-i>=0 and int(col)-i>=0: #si les valeurs ne sont pas négative
                                                self.tuple = value #pour que ce soit plus lisible 

                                                if (self.tuple[0]-1,self.tuple[1]-1) in self.game.list_empty:
                                                    #verifie si la piece (row-i,col-i) en (row-1,col-1) donc dans sa diagonale gauche
                                                    #est vide  pour que la dame puisse eat

                                                    self.list_index_dame_black[id_eat_black] = (self.tuple[0],self.tuple[1]) 
                                                    #grace à id_eat on va rajouter la self.tuple
                                                    # a un index precis de la self.list_index_dame_black

                                                    self.list_eat_dame_black.append((self.tuple[0]-1,self.tuple[1]-1))
                                                    #rajout dans la  list_eat_dame_black de  la coordonée ou ira la piece
                                                    #quand il aura eat

                                                    self.list_row_col_main[id_eat_black] = (self.tuple[0]-1,self.tuple[1]-1)
                                                    
                                                    """exemple :
                                                    (6,5)== position dame_noire
                                                    pion blanc en (4,3) et que en (3,2) il n'y a aucun pions.
                                                
                                                    #ALORS self.list_index_dame_black[0] = (4,3)
                                                    alors dans le cas ou il y n'y a pas d'autre pions a eat 

                                                    self.list_index_dame_black = [(4,3), None, None, None]
                                                    self.list_eat_dame_black = (3,2)
                                                    self.list_row_col_main[0] = (3,2)

                                                    self.list_row_col_main = [(3,2), None, None, None]

                                                    cela nous permet dans la fonction assign_tuple()

                                                    si click in self.list_row_col_main donc en (3,2)
                                                    alors self.list_row_col_main.index(self.other_click)
                                                     car (3,2) est dans l'index 0, self.list_row_col_main[0] = (3,2)


                                                    si index 0 alors self.list_index_dame_black[0] = (4,3)
                                                    new = self.list_index_dame_white[0] on assigne new a (4,3)
                                                    
                                                    self.mat[new[0]][new[1]] = 0
                                                    donc le pion (4,3) sera = 0
                                                    
                                                    #"""

                                    if (int(row)-i,int(col)+i) in self.game.list_white or (int(row)-i,int(col)+i) in self.game.list_dame_white:
                                            value = (int(row)-i,int(col)+i)
                                            id_eat_black = 1
                                            if  int(row)-i>=0 and int(col)+i<=7: 
                                                self.tuple = value


                                                if (self.tuple[0]-1,self.tuple[1]+1) in self.game.list_empty:

                                                    self.list_index_dame_black[id_eat_black] = (self.tuple[0],self.tuple[1])
                                                    self.list_eat_dame_black.append((self.tuple[0]-1,self.tuple[1]+1))
                                                    self.list_row_col_main[id_eat_black] = (self.tuple[0]-1,self.tuple[1]+1)

                                    if (int(row)+i,int(col)+i) in self.game.list_white or (int(row)+i,int(col)+i) in self.game.list_dame_white :
                                                value = (int(row)+i,int(col)+i)
                                                id_eat_black = 2
                                                if  int(row)+i<=7 and int(col)+i<=7: 
                                                    self.tuple = value

                                                    if (self.tuple[0]+1,self.tuple[1]+1) in self.game.list_empty:
                                                        self.list_index_dame_black[id_eat_black] = (self.tuple[0],self.tuple[1])
                                                        self.list_eat_dame_black.append((self.tuple[0]+1,self.tuple[1]+1))
                                                        self.list_row_col_main[id_eat_black] = (self.tuple[0]+1,self.tuple[1]+1)
                                    
                                    if (int(row)+i,int(col)-i) in self.game.list_white or (int(row)+i,int(col)-i) in self.game.list_dame_white :
                                               
                                                value = (int(row)+i,int(col)-i)
                                                
                                                print(value,'l_654')
                                                id_eat_black = 3
                                                if  int(row)+i<=7 and int(col)-i>=0: 
                                                    self.tuple = value

                                                    if (self.tuple[0]+1,self.tuple[1]-1) in self.game.list_empty:
                                                        self.list_index_dame_black[id_eat_black] = (self.tuple[0],self.tuple[1])
                                                        self.list_eat_dame_black.append((self.tuple[0]+1,self.tuple[1]-1))
                                                        self.list_row_col_main[id_eat_black] = (self.tuple[0]+1,self.tuple[1]-1)
                        
                        
                                            
                                
                                                                    
    def valid_eat_moove_dam_white(self):
            
            id_eat = None
            if self.turn is None and self.selected in self.game.list_dame_white:
                self.val = []
                counter = 0
                self.list_index_dame_white = [None] * 4
                self.list_row_col_main = [None]*4
                for row in str(self.selected[0]):
                    for col in str(self.selected[1]):
                        for i in range(1,7):
 
                                    if (int(row)-i,int(col)-i) in self.game.list_black or (int(row)-i,int(col)-i) in self.game.list_dame_black:
                                            value = (int(row)-i,int(col)-i)
                                            id_eat = 0
                                            
                                            if  int(row)-i>=0 and int(col)-i>=0: 
                                                self.tuple = value
                                                if (self.tuple[0]-1,self.tuple[1]-1) in self.game.list_empty:
                                                    self.list_index_dame_white[id_eat] = (self.tuple[0],self.tuple[1])
                                                    self.list_eat_dame_white.append((self.tuple[0]-1,self.tuple[1]-1))
                                                    self.list_row_col_main[id_eat] = (self.tuple[0]-1,self.tuple[1]-1)

                                    if (int(row)-i,int(col)+i) in self.game.list_black or (int(row)-i,int(col)+i) in self.game.list_dame_black:
                                            value = (int(row)-i,int(col)+i)
                                            id_eat = 1
                                            if  int(row)-i>=0 and int(col)+i<=7: 
                                                self.tuple = value
                                                self.dame_movements = []
                                                if (self.tuple[0]-1,self.tuple[1]+1) in self.game.list_empty:
                                                    self.list_index_dame_white[id_eat] = (self.tuple[0],self.tuple[1])
                                                    self.list_eat_dame_white.append((self.tuple[0]-1,self.tuple[1]+1))
                                                    self.list_row_col_main[id_eat] = (self.tuple[0]-1,self.tuple[1]+1)

                                    if (int(row)+i,int(col)+i) in self.game.list_black or (int(row)+i,int(col)+i) in self.game.list_dame_black :
                                                value = (int(row)+i,int(col)+i)
                                                id_eat = 2
                                                if  int(row)+i<=7 and int(col)+i<=7: 
                                                    self.tuple = value
                                                    self.dame_movements = []
                                                    if (self.tuple[0]+1,self.tuple[1]+1) in self.game.list_empty:
                                                        self.list_index_dame_white[id_eat] = (self.tuple[0],self.tuple[1])
                                                        self.list_eat_dame_white.append((self.tuple[0]+1,self.tuple[1]+1))
                                                        self.list_row_col_main[id_eat] = (self.tuple[0]+1,self.tuple[1]+1)
                                            
                                    if (int(row)+i,int(col)-i) in self.game.list_black or (int(row)+i,int(col)-i) in self.game.list_dame_black :
                                                value = (int(row)+i,int(col)-i)
                                                id_eat = 3
                                                if  int(row)+i<=7 and int(col)-i>=0: 
                                                    self.tuple = value
                                                    self.dame_movements = []
                                                    if (self.tuple[0]+1,self.tuple[1]-1) in self.game.list_empty:
                                                        self.list_index_dame_white[id_eat] = (self.tuple[0],self.tuple[1])
                                                        self.list_eat_dame_white.append((self.tuple[0]+1,self.tuple[1]-1))
                                                        self.list_row_col_main[id_eat] = (self.tuple[0]+1,self.tuple[1]-1)

                        
    def eat(self,screen,row,col):
            
            if len(self.white_piece_eat_movement_list)>0 or  len(self.black_movement_list)>0:
                self.click(screen,row,col)
                # cette fonction permet de re eat si il y a l'opportunité
                
            elif len(self.list_eat_dame_white)>0 or len(self.list_eat_dame_black)>0:
                self.click(screen,row,col)


    def assign_tuple(self): 
        new = None
        #explication de l'utilisation en l_615-640
        if self.selected in self.game.list_dame_white:
            if self.other_click in self.list_row_col_main:

                i = self.list_row_col_main.index(self.other_click)

                if i == 0:
                    new = self.list_index_dame_white[0]
                if i == 1:
                    new = self.list_index_dame_white[1]
                if i == 2:
                    new = self.list_index_dame_white[2]
                if i == 3:
                    new = self.list_index_dame_white[3]

        if self.selected in self.game.list_dame_black:
            if self.other_click in self.list_row_col_main:
                print(self.list_row_col_main)
                i = self.list_row_col_main.index(self.other_click)
                print("i:", i)
                if i == 0:
                    new = self.list_index_dame_black[0]
                if i == 1:
                    new = self.list_index_dame_black[1]
                if i == 2:
                    new = self.list_index_dame_black[2]
                if i == 3:
                    new = self.list_index_dame_black[3]
     
        
        return new
            
         
        
        
            
        
            

