

class game:
    def __init__(self,mat,turn,running):
          self.mat = mat
          self.count = []
          self.turn = turn
          self.moove_yes_white = False
          self.moove_yes_black = False
          self.running = running

        
    
            
    
    def sides(self):
        self.list_black = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 2]
        #mettre danns une list les coordonnées des pions noir 
        self.list_white = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 1]        
        
        self.list_empty = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] == 0]  
        
        self.list_dame_white = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] ==3]    
        
        self.list_dame_black = [(x, y) for x in range(self.mat.shape[0]) for y in range(self.mat.shape[1]) if self.mat[x][y] ==4]  

        self.list_dame = [self.list_dame_white,self.list_dame_black]
    
    

    
    def moove_compute_dame_eat(self,row,col,selected,list_kill_moove_dame,screen,state):
        
        if self.turn is None and selected in self.list_dame_white and (row, col) == (selected[0] - 2, selected[1] + 2) and selected is not None and (selected[0] - 2, selected[1] + 2) in list_kill_moove_dame[0]:
                print('cgange ')            
                self.moove_id_eat = 1
                self.eat_dame_compute(row,col,selected,screen,state)
                self.turn = 1


                    
        elif  self.turn is None and selected in self.list_dame_white  and (row, col) == (selected[0] - 2, selected[1] - 2) and selected is not None and (selected[0] - 2, selected[1] - 2) in list_kill_moove_dame[0]:
                self.moove_id_eat = 2
                self.eat_dame_compute(row,col,selected,screen,state)
                list_kill_moove_dame = None
                self.turn = 1
        
        
             
    def moove_dame_compute(self,selected,state,moove_id_no_eat):
                state = state
                if moove_id_no_eat in {1,5}:
                    print('eleel')
                    self.mat[selected[0] - 1][selected[1] + 1] = self.mat[selected[0]][selected[1]]
                    self.mat[selected[0]][selected[1]] = 0
                    
                    
                
                  
                if moove_id_no_eat in {2,6}:
                    
                    self.mat[selected[0] - 1][selected[1] - 1] = self.mat[selected[0]][selected[1]]
                    self.mat[selected[0]][selected[1]] = 0

                    
                    

                if  moove_id_no_eat in {3,7}:
                    self.mat[selected[0] + 1][selected[1] + 1] = self.mat[selected[0]][selected[1]] 
                    self.mat[selected[0]][selected[1]] = 0

                    
                    

                if moove_id_no_eat in {4,8}:                    
                    self.mat[selected[0] + 1][selected[1]- 1] = self.mat[selected[0]][selected[1]] 
                    self.mat[selected[0]][selected[1]] = 0

                    
    def eat_dame_compute(self,row,col,selected,screen,state,moove_id_eat):
                    if moove_id_eat ==1:  
                        self.mat[selected[0] - 1][selected[1] + 1] = 0

                        self.mat[selected[0] - 2][selected[1] + 2] = self.mat[selected[0]][selected[1]] 
                        self.mat[selected[0]][selected[1]] = 0

                        
                    if moove_id_eat ==2:
                        self.mat[selected[0] - 1][selected[1] - 1] = 0
                        self.mat[selected[0] - 2][selected[1] - 2] = self.mat[selected[0]][selected[1]] 
                        self.mat[selected[0]][selected[1]] = 0

    def change_turn(self):
        if self.turn == None:
                self.turn = 1
        else:
              self.turnn = None
    def winner(self):
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
        


                        
                        
                        
                        

                        
                        
            
        
