

import pygame 
import os 


WIDTH, HEIGHT = 600, 600
row,col = 8,8
SQUARE_SIZE = WIDTH//row
RADIUS = 30
RADIUS_FUTURE_POSITION = 10
BLACK = (0,0, 0)
WHITE = (255, 255, 255)
GREY = (128,128,128)
BLUE = (16,1,65)


GREEN = (19,132,20)
BROWN =(46,41,41)

path = 'image'

piece_black = pygame.image.load(os.path.join(path,'pion_noir.png'))
piece_white = pygame.image.load(os.path.join(path,'pion_blanc.png'))
        

# Scale the image
piece_black = pygame.transform.scale(piece_black, (SQUARE_SIZE, SQUARE_SIZE))
piece_white = pygame.transform.scale(piece_white, (SQUARE_SIZE, SQUARE_SIZE))


