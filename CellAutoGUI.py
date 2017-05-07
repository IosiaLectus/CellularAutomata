#Setup GUI with pygame

import pygame, sys
from CellularAutomata import Automata1D, Automata2D
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GRAY = (205,205,205)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

clock = pygame.time.Clock()

WIDTH = 1440
HEIGHT = 810
SIZE = 60
RULE = 251043649666805698923307029
STATES = 2
#Special rules
SPECIAL1 = 115792089237316195423570985008687907853610267032561502502939405359422902370582
# Rules that produce behaviour similar to Conway's game of life
LIFE_LIKE1 = 3121748551042842093571244711680280772127638873342896181933539037900840921746291282334660294445170887313256105169567155377323718410239403643922560
LIFE_LIKE2 = 3121796387206642884643857416353388816364758858874716286199733047244606563193329744673035888249711427712341048321888349917378690566361405647808640
LIFE_LIKE3 = 205454759090497442639052309945232436214865822284380363200347133833515823847409191219264074201015001590380158520753898239949933374880133468736771876992
LIFE_LIKE4 = 3121748550316003369275635227966723160929773800693073915431708268582463553108296554833454127312789959259510100096341992684407471235049015936947816
LIFE_LIKE5 = 3121796386479804160348247932600429198970499307010478992561837746418013872513971932782371638727206770958880840759000767848926760520120736189284352
LIFE_LIKE6 = 726838724464839811763263258735123865184586998611241671908905457650522586198267251210724490087484537107000710513277144975870888020699264
# Haven't yet succesfully identified the rule for Conway's game of life
CONWAYS_LIFE = 47634829485252037513200973884082471888288955642325528262910887637847274372981720534370017768342996036219492316860704401273651054628223608960
RULE30 = 30

COLORS = [BLACK,WHITE,RED,GREEN,BLUE]

FPS = 5

#Run a 1-d cellular automaton with 'size' cells and rule 'rule'.
def run_1DAutomata(screen, size, rule, n_states=2):

    button_font = pygame.font.SysFont('FreeSans.otf',25)

    # Create the cellular automaton object
    Aut = Automata1D(size,rule, n_states)
    # Given the screen size and the size of the automaton, decide the size of each cell in pixels.
    dt = WIDTH/Aut.size
    # Create a live cell in the center
    Aut.populate(int(size/2))
    # Display the automaton in the top 85% of the screen, reserving the rest for buttons
    display_height = 0.85 * HEIGHT

    # This stores a map of cells to be displayed on the screen
    grid = []

    # Make some buttons
    start_stop_button = button_font.render("Start/Stop",True,WHITE,BLACK)
    start_stop_button_rect = start_stop_button.get_rect()
    start_stop_button_rect.topleft = (0.15 * WIDTH, 0.88 * HEIGHT)

    clear_button = button_font.render("Clear",True,WHITE,BLACK)
    clear_button_rect = clear_button.get_rect()
    clear_button_rect.topleft = (0.35 * WIDTH, 0.88 * HEIGHT)

    menu_button = button_font.render("Menu",True,WHITE,BLACK)
    menu_button_rect = menu_button.get_rect()
    menu_button_rect.topleft = (0.55 * WIDTH, 0.88 * HEIGHT)
    
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
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    running = not running
                elif event.key == K_c:
                    Aut = Automata1D(size,rule,n_states)
                    Aut.populate(int(size/2))
                    grid = []
                    screen.fill(LIGHT_GRAY)
                elif event.key == K_m:
                    return
            elif event.type == MOUSEBUTTONUP:
                if start_stop_button_rect.collidepoint(event.pos):
                    running = not running
                elif clear_button_rect.collidepoint(event.pos):
                    Aut = Automata1D(size,rule,n_states)
                    Aut.populate(int(size/2))
                    grid = []
                    screen.fill(LIGHT_GRAY)
                elif menu_button_rect.collidepoint(event.pos):
                    return
        if running:
            # Get the list of current cells, and append them at the bottom of our grid
            grid.append(list(Aut.present))
            # If the grid is too tall to fit in the available space, cut of the topmost layer of cells
            if len(grid)> display_height/dt:
                grid = list(grid[1:])
            # Draw the cells to the screen
            screen.fill(LIGHT_GRAY)
            for i in range(0,len(grid)):
                for j in range(0,Aut.size):
                    pygame.draw.rect(screen,COLORS[grid[i][j]],(j*dt,i*dt,dt,dt),0)

            # Step the automaton
            Aut.step()

        #Draw the buttons
        screen.blit(start_stop_button, start_stop_button_rect)
        screen.blit(clear_button, clear_button_rect)
        screen.blit(menu_button, menu_button_rect)

	# Update display and increment the clock
        pygame.display.update()
        clock.tick(FPS)

#Run a 2-d square grid cellular automaton with 'size' cells and rule 'rule'.
def run_2DAutomata(screen, size, rule, n_states=2):

    button_font = pygame.font.SysFont('FreeSans.otf',25)

    # Create the cellular automaton object
    Aut = Automata2D(size,rule, n_states)
    # Populate randomly
    Aut.populateRandom(750)
    # Given the screen size and the size of the automaton, decide the size of each cell in pixels.
    dt = min(WIDTH/Aut.size, 0.85*HEIGHT/Aut.size)
    # Create a live cell in the center
    Aut.populate(int(size/2),int(size/2))
    # Display the automaton in the top 85% of the screen, reserving the rest for buttons
    display_height = 0.85 * HEIGHT

    #Find positions for grid
    width_left = (WIDTH - Aut.size*dt)/2
    height_top = (0.85*HEIGHT - Aut.size*dt)/2

    # This stores a map of cells to be displayed on the screen
    grid = [[None for i in range(0,size)] for j in range(0,size)]
    for i in range(0,size):
        for j in range(0,size):
            grid[i][j] = Rect(width_left + i*dt, height_top + j*dt,dt-1,dt-1)

    # Make some buttons
    start_stop_button = button_font.render("Start/Stop",True,WHITE,BLACK)
    start_stop_button_rect = start_stop_button.get_rect()
    start_stop_button_rect.topleft = (0.15 * WIDTH, 0.88 * HEIGHT)

    clear_button = button_font.render("Clear",True,WHITE,BLACK)
    clear_button_rect = clear_button.get_rect()
    clear_button_rect.topleft = (0.35 * WIDTH, 0.88 * HEIGHT)

    menu_button = button_font.render("Menu",True,WHITE,BLACK)
    menu_button_rect = menu_button.get_rect()
    menu_button_rect.topleft = (0.55 * WIDTH, 0.88 * HEIGHT)

    step_button = button_font.render("Step",True,WHITE,BLACK)
    step_button_rect = step_button.get_rect()
    step_button_rect.topleft = (0.75 * WIDTH, 0.88 * HEIGHT)
    
    # change the caption
    caption = '2-Dimensional Cellular Automaton: Rule %u' %(rule)
    pygame.display.set_caption(caption)

    # Setup the loop
    should_continue = True  
    running = False  
    while should_continue:
        # Get events and respond accordingly
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    running = not running
                elif event.key == K_c:
                    Aut = Automata2D(size,rule, n_states)
                elif event.key == K_m:
                    return
            elif event.type == MOUSEBUTTONUP:
                if start_stop_button_rect.collidepoint(event.pos):
                    running = not running
                elif clear_button_rect.collidepoint(event.pos):
                    Aut = Automata2D(size,rule, n_states)
                elif step_button_rect.collidepoint(event.pos) and not running:
                    Aut.step()
                elif menu_button_rect.collidepoint(event.pos):
                    return
                # Iterate through the states of a cell if it is clicked while not running
                elif running == False:
                    for i in range(0,Aut.size):
                        for j in range(0,Aut.size):
                            if grid[i][j].collidepoint(event.pos):
                                Aut.present[i][j] = (Aut.present[i][j] + 1)%Aut.cell_states

        # Draw the cells to the screen
        screen.fill(LIGHT_GRAY)
        for i in range(0,Aut.size):
            for j in range(0,Aut.size):
                rectij = grid[i][j]
                colorij = COLORS[Aut.present[i][j]]
                pygame.draw.rect(screen, colorij, rectij, 0)

        if running:
            # Step the automaton
            Aut.step()

        #Draw the buttons
        screen.blit(start_stop_button, start_stop_button_rect)
        screen.blit(clear_button, clear_button_rect)
        screen.blit(menu_button, menu_button_rect)
        screen.blit(step_button, step_button_rect)


	# Update display and increment the clock
        pygame.display.update()
        clock.tick(FPS)

#Display a menu (not yet implemented).
def display_menu(screen):

    button_font = pygame.font.SysFont('FreeSans.otf',45)

    # Make some buttons
    cell_at_oned_button = button_font.render("Start 1-d cellular automaton",True,WHITE,BLACK)
    cell_at_oned_button_rect = cell_at_oned_button.get_rect()

    cell_at_twod_button = button_font.render("Start 2-d cellular automaton",True,WHITE,BLACK)
    cell_at_twod_button_rect = cell_at_twod_button.get_rect()

    w_button = (WIDTH - cell_at_oned_button_rect.width)/2
    h_button = (HEIGHT - cell_at_oned_button_rect.height - cell_at_twod_button_rect.height)/3
    cell_at_oned_button_rect.topleft = (w_button, h_button)
    cell_at_twod_button_rect.topleft = (w_button, 2*h_button + cell_at_oned_button_rect.height)

    # Setup the loop
    should_continue = True  
    while should_continue:
        # Get events and respond accordingly
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_a:
                    # Run a 1-d cellular automaton
                    run_1DAutomata(screen, SIZE, RULE30, STATES)

            elif event.type == MOUSEBUTTONUP:
                if cell_at_oned_button_rect.collidepoint(event.pos):
                    # Run a 1-d cellular automaton
                    run_1DAutomata(screen, SIZE, RULE30, STATES)
                elif cell_at_twod_button_rect.collidepoint(event.pos):
                    # Run a 2-d cellular automaton
                    run_2DAutomata(screen, SIZE, CONWAYS_LIFE, STATES)
        #Fill screen, draw button
        screen.fill(LIGHT_GRAY)
        screen.blit(cell_at_oned_button, cell_at_oned_button_rect)
        screen.blit(cell_at_twod_button, cell_at_twod_button_rect)

	# Update display and increment the clock
        pygame.display.update()
        clock.tick(FPS)

#Actually do stuff
def main():
    # Initialize pygame etc.
    pygame.init()
    button_font = pygame.font.SysFont('FreeSans.otf',32)
    
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

    #Open the main menu
    display_menu(DISPLAYSURF)
            
if __name__ == "__main__":
    main()
