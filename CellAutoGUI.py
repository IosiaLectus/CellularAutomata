#Setup GUI with pygame

import pygame, sys
from CellularAutomata import Automata1D
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)

Aut = Automata(1999,1)
Aut.setRule(30)

Width = 4000
Height = 5000

dt = Width/Aut.n

FPS = 5

clock = pygame.time.Clock()

def display_menu():
    screen = pygame.display.set_mode((Width, Height))

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption('This is not a text box!')
    DISPLAYSURF.fill(WHITE)
    Aut.populate(600)
    grid = []
    
    while True:
        grid.append(list(Aut.present))
        if len(grid)>Height/dt:
            grid = list(grid[1:])
        DISPLAYSURF.fill(WHITE)
        for i in range(0,len(grid)):
            for j in range(0,Aut.n):
                if grid[i][j] == 1:
                    pygame.draw.rect(DISPLAYSURF,BLACK,(j*dt,i*dt,dt,dt),0)
        Aut.step()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(FPS)
            
if __name__ == "__main__":
    main()
