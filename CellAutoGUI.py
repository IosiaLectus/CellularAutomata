#Setup GUI with pygame

import pygame, sys
from CellularAutomata import Automata1D
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()

WIDTH = 960
HEIGHT = 540
SIZE = 120
RULE = 30

FPS = 5

#Run a 1-d cellular automaton with 'size' cells and rule 'rule'.
def run_1DAutomata(screen, size, rule):

    # Create the cellular automaton object
    Aut = Automata1D(size,rule)
    # Given the screen size and the size of the automaton, decide the size of each cell in pixels.
    dt = WIDTH/Aut.size
    # Create a live cell in the center
    Aut.populate(int(size/2))
    # Display the automaton in the top 85% of the screen, reserving the rest for buttons
    display_height = 0.85 * HEIGHT

    # This stores a map of cells to be displayed on the screen
    grid = []
    
    # change the caption
    caption = '1-Dimensional Cellular Automaton: Rule %u' %(rule)
    pygame.display.set_caption(caption)

    # Setup the loop
    should_continue = True  
    running = True  
    while should_continue:
        # Get events and respond accordingly
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if running:
            # Get the list of current cells, and append them at the bottom of our grid
            grid.append(list(Aut.present))
            # If the grid is too tall to fit in the available space, cut of the topmost layer of cells
            if len(grid)> display_height/dt:
                grid = list(grid[1:])
            # Draw the cells to the screen
            screen.fill(WHITE)
            for i in range(0,len(grid)):
                for j in range(0,Aut.size):
                    if grid[i][j] == 1:
                        pygame.draw.rect(screen,BLACK,(j*dt,i*dt,dt,dt),0)

            # Step the automaton
            Aut.step()

	# Update display and increment the clock
        pygame.display.update()
        clock.tick(FPS)

#Display a menu (not yet implemented).
def display_menu(screen):
    # For now, just run, just run a 1-d cellular automaton
    run_1DAutomata(screen, SIZE, RULE)

#Actually do stuff
def main():
    # Initialize pygame etc.
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

    #Open the main menu
    display_menu(DISPLAYSURF)
            
if __name__ == "__main__":
    main()
