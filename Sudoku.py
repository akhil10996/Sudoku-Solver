
#importing libraries
import pygame

# initialising font
pygame.font.init()

#Window
screen= pygame.display.set_mode((600,600))

#Title 
pygame.display.set.caption("Sudoku Backtracking Solver")

x= 0
y=0
dif = 600/9
val=0

#default sudoku board
grid =[ 
        [7, 8, 0, 4, 0, 0, 1, 2, 0], 
        [6, 0, 0, 0, 7, 5, 0, 0, 9], 
        [0, 0, 0, 6, 0, 1, 0, 7, 8], 
        [0, 0, 7, 0, 4, 0, 2, 6, 0], 
        [0, 0, 1, 0, 5, 0, 9, 3, 0], 
        [9, 0, 4, 0, 6, 0, 0, 0, 5], 
        [0, 7, 0, 3, 0, 0, 0, 1, 2], 
        [1, 2, 0, 0, 0, 7, 4, 0, 0], 
        [0, 4, 9, 2, 0, 6, 0, 0, 7] 

]
 # Loading fonts for future use
 font1= pygame.font.SysFont("comicsans", 40)
 font2 = pygame.font.SysFont("comicsans", 20)

 def get_cord(pos):
     global x
     x = pos[0]//dif
     global
     y= pos[1]//dif
     