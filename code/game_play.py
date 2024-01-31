

class game:
    def __init__(self,mat,running):
          self.mat = mat
           
         
          self.moove_yes_white = False
          self.moove_yes_black = False
          self.running = running
          self.moove_row_col = None
          self.selected,self.state,self.turn = None,None,None
        
    
            
    
    def sides(self):
        self.list_black = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 2]
        #mettre danns une list les coordonnées des pions noir 
        self.list_white = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 1]        
        
        self.list_empty = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 0]  
        
        self.list_dame_white = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] ==3]    
        
        self.list_dame_black = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] ==4]  

    
        
             
    def block_action(self,selected,turn,state,white_movement_list,black_movement_list,dame_movements,white_piece_eat_movement_list,black_eat_movement_list,list_eat_dame_black,list_eat_dame_white):
        self.selected = selected
        self.turn = turn
        self.state = state
        if self.turn == 1 and self.selected in self.list_white: 

            self.selected = None
            self.state = None
            self.turn = 1
        if self.turn == 1 and self.selected in self.list_dame_white: 

            self.selected = None
            self.state = None
            self.turn = 1
            
        if self.turn is None and self.selected in self.list_black: 
            self.state = None 
            self.selected = None
            self.turn = None


        if self.turn is None and self.selected in self.list_dame_black: 
            self.state = None 
            self.selected = None
            self.turn = None

        if self.turn is None and self.selected in self.list_white and self.selected not in self.list_dame_white and len(white_movement_list)==0 and len(white_piece_eat_movement_list)==0:
            self.state = None 
            self.selected = None
            self.turn = None
        if self.turn is None and self.selected in self.list_dame_white and len(list_eat_dame_white)==0 and len(dame_movements)==0:
            self.state = None 
            self.selected = None
            self.turn = None

        if self.turn ==1 and self.selected not in self.list_dame_black and self.selected in self.list_black  and black_movement_list is None and black_eat_movement_list is None:
            self.state = None 
            self.selected = None
            self.turn = 1
        
        
        if self.turn ==1 and self.selected in self.list_dame_black and len(dame_movements)==0 and len(list_eat_dame_black)==0 :
            self.state = None 
            self.selected = None
            self.turn = 1
        
    
    def winner(self,turn):
        self.list_white += self.list_dame_white
        self.list_black += self.list_dame_black
        if len(self.list_white)==0 and len(self.list_black)>0:
                winner = 'black'
                self.running = False
                print(self.running)
                print(f'the winner are {winner}')
        elif len(self.list_black)==0 and len(self.list_white)>0:
                winner = 'white'
                self.running = False
                print(self.running)
                print(f'the winner are {winner}')

   
