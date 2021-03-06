#Setup GUI with pygame

import pygame, sys
from CellularAutomata import Automata1D, Automata2D
from pygame.locals import *
from copy import copy
from FindConwaysLife import *

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GRAY = (205,205,205)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

clock = pygame.time.Clock()

# Screen width and height
WIDTH = 1440
HEIGHT = 810
# Conway's game of life
CONWAYS_LIFE = FindConwaysLife()

#Set 2d default settings
rule2d = CONWAYS_LIFE
n_states2d = 2
size2d = 60

#Set 1d default settings
rule1d = 30
n_states1d = 2
size1d = 120

COLORS = [BLACK,WHITE,RED,GREEN,BLUE]

FPS = 5

# Get an integer as input from the user
def getInt(screen, msg):

    ret = 0
    retstring = '%u' %(ret)

    display_font = pygame.font.SysFont('FreeSans.otf',45)

    # Make the displays
    msg_display = display_font.render(msg,True,WHITE,BLACK)
    msg_display_rect = msg_display.get_rect()

    int_display = display_font.render(retstring,True,WHITE,BLACK)
    int_display_rect = int_display.get_rect()

    w_button = (WIDTH - msg_display_rect.width)/2
    h_button = (HEIGHT - msg_display_rect.height - int_display_rect.height)/3
    msg_display_rect.topleft = (w_button, h_button)
    int_display_rect.topleft = (w_button, 2*h_button + msg_display_rect.height)

    # Setup the loop
    should_continue = True  
    while should_continue:
        # Get events and respond accordingly
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Get user input and update output accordingly
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    # Run a 1-d cellular automaton
                    return ret
                if event.key == K_BACKSPACE:
                    # Run a 1-d cellular automaton
                    x = (ret - (ret%10))/10
                    retstring = '%u' %(x)
                if event.key == K_0:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '0'
                if event.key == K_1:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '1'
                if event.key == K_2:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '2'
                if event.key == K_3:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '3'
                if event.key == K_4:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '4'
                if event.key == K_5:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '5'
                if event.key == K_6:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '6'
                if event.key == K_7:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '7'
                if event.key == K_8:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '8'
                if event.key == K_9:
                    # Run a 1-d cellular automaton
                    retstring = retstring + '9'

        #Update variables
        ret = int(retstring)
        retstring = '%u' %(ret)

        int_display = display_font.render(retstring,True,WHITE,BLACK)
        int_display_rect = int_display.get_rect()
        int_display_rect.topleft = (w_button, 2*h_button + msg_display_rect.height)

        #Fill screen, draw displays
        screen.fill(LIGHT_GRAY)

        screen.blit(msg_display, msg_display_rect)
        screen.blit(int_display, int_display_rect)

	# Update display and increment the clock
        pygame.display.update()
        clock.tick(FPS)

# Equally space buttons within some rectangle. Currently not working
def layout_buttons(buttons, hmin, hmax, wmin, wmax, horizontal=False):

    # total number of buttons
    n_buttons = len(buttons)
    # height and width spacings
    dw = wmax - wmin
    dh = hmax - hmin
    # list of sizes of the buttons the buttons
    wlist = [buttons[i].width for i in range(0,n_buttons)]
    hlist = [buttons[i].height for i in range(0,n_buttons)]
    # list of coords for the buttons
    xlist = [0 for i in range(0,n_buttons)]
    ylist = [0 for i in range(0,n_buttons)]

    wspace = (dw - sum(wlist))/(n_buttons - 1)
    wspace = (dh - sum(hlist))/(n_buttons - 1)

    if horizontal:
        for i in range(0, n_buttons):
            ylist[i] = (dh - hlist[i])/2
            xlist[i] = hspace*(i+1) + sum(hlist[0:i])
            buttons[i].topleft = (xlist[i], ylist[i])
    else:
        for i in range(0, n_buttons):
            xlist[i] = (dw - wlist[i])/2
            ylist[i] = wspace*(i+1) + sum(wlist[0:i])
            buttons[i].topleft = (xlist[i], ylist[i])

#Run a 1-d cellular automaton with 'size' cells and rule 'rule'.
def run_1DAutomata(screen, size, rule, n_states=2):

    button_font = pygame.font.SysFont('FreeSans.otf',25)

    # Create the cellular automaton object
    Aut = Automata1D(size, rule, n_states)
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

    step_button = button_font.render("Step",True,WHITE,BLACK)
    step_button_rect = step_button.get_rect()
    step_button_rect.topleft = (0.75 * WIDTH, 0.88 * HEIGHT)
    
    # change the caption
    caption = '1-Dimensional Cellular Automaton: Rule %u' %(rule)
    pygame.display.set_caption(caption)

    # Setup the loop
    should_continue = True  
    running = True  
    while should_continue:
        step_now = running
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
                elif step_button_rect.collidepoint(event.pos) and not running:
                    step_now = True
                elif menu_button_rect.collidepoint(event.pos):
                    return
        if step_now:
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
        screen.blit(step_button, step_button_rect)

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

#Change the settings for the cellular automaton
def settings(screen):

    button_font = pygame.font.SysFont('FreeSans.otf',25)

    # Make some buttons
    rule2d_button = button_font.render("Change rule for 2d automaton (Wolfram Code)",True,WHITE,BLACK)
    rule2d_button_rect = rule2d_button.get_rect()

    rule2db_button = button_font.render("Change rule for 2d automaton (MCell)",True,WHITE,BLACK)
    rule2db_button_rect = rule2db_button.get_rect()

    rule1d_button = button_font.render("Change rule for 1d automaton",True,WHITE,BLACK)
    rule1d_button_rect = rule1d_button.get_rect()

    size1d_button = button_font.render("Set 1d automaton size",True,WHITE,BLACK)
    size1d_button_rect = size1d_button.get_rect()

    size2d_button = button_font.render("Set 2d automaton size",True,WHITE,BLACK)
    size2d_button_rect = size2d_button.get_rect()

    num_states_1d_button = button_font.render("Set number of 1d automaton states",True,WHITE,BLACK)
    num_states_1d_button_rect = num_states_1d_button.get_rect()

    num_states_2d_button = button_font.render("Set number of 2d automaton states",True,WHITE,BLACK)
    num_states_2d_button_rect = num_states_2d_button.get_rect()

    back_button = button_font.render("Back to menu",True,WHITE,BLACK)
    back_button_rect = back_button.get_rect()

    w_button = (WIDTH - rule2d_button_rect.width)/2
    h_button = (HEIGHT - rule2d_button_rect.height - rule1d_button_rect.height - size1d_button_rect.height - size2d_button_rect.height - rule2db_button_rect.height - back_button_rect.height - num_states_2d_button_rect.height - num_states_1d_button_rect.height)/9
    rule1d_button_rect.topleft = (w_button, h_button)
    rule2d_button_rect.topleft = (w_button, 2*h_button + rule2d_button_rect.height)
    rule2db_button_rect.topleft = (w_button, 3*h_button + rule2d_button_rect.height + rule1d_button_rect.height)
    size1d_button_rect.topleft = (w_button, 4*h_button + rule2d_button_rect.height + rule2db_button_rect.height + rule1d_button_rect.height)
    size2d_button_rect.topleft = (w_button, 5*h_button + rule2d_button_rect.height + rule2db_button_rect.height + rule1d_button_rect.height + size1d_button_rect.height)
    num_states_1d_button_rect.topleft = (w_button, 6*h_button + rule2d_button_rect.height + rule2db_button_rect.height + rule1d_button_rect.height + size1d_button_rect.height + size2d_button_rect.height)
    num_states_2d_button_rect.topleft = (w_button, 7*h_button + rule2d_button_rect.height + rule2db_button_rect.height + rule1d_button_rect.height + size1d_button_rect.height + size2d_button_rect.height + num_states_1d_button_rect.height)
    back_button_rect.topleft = (w_button, 8*h_button + rule2d_button_rect.height + rule2db_button_rect.height + rule1d_button_rect.height + size1d_button_rect.height + size2d_button_rect.height + num_states_1d_button_rect.height + num_states_2d_button_rect.height)

    # Setup the loop
    should_continue = True  
    while should_continue:
        # Get events and respond accordingly
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYUP:
                if event.key == K_m:
                    return

            elif event.type == MOUSEBUTTONUP:
                if back_button_rect.collidepoint(event.pos):
                    # Go back to the main menu
                    return
                elif rule1d_button_rect.collidepoint(event.pos):
                    # update rule1d with user input
                    global rule1d
                    rule1d = getInt(screen,'Enter new rule:')
                elif rule2d_button_rect.collidepoint(event.pos):
                    # update rule2d with user input
                    global rule2d
                    rule2d = getInt(screen,'Enter new rule:')
                elif rule2db_button_rect.collidepoint(event.pos):
                    # update rule2d by computing a wolfram code from a MCell style rule
                    global rule2d
                    birth_int = getInt(screen,'Enter birth string:')
                    survival_int = getInt(screen,'Enter survival string:')

                    birth = []
                    # Get a list of birth states
                    while birth_int > 0:
                        app = birth_int % 10
                        birth.append(app)
                        birth_int = birth_int - app
                        birth_int = birth_int/10

                    survival = []
                    # Get a list of survival states
                    while survival_int > 0:
                        app = survival_int % 10
                        survival.append(app)
                        survival_int = survival_int - app
                        survival_int = survival_int/10

                    rule2d = ConvertRule(birth, survival)
                elif size1d_button_rect.collidepoint(event.pos):
                    # update size1d with user input
                    global size1d
                    size1d = getInt(screen,'Enter size:')
                elif size2d_button_rect.collidepoint(event.pos):
                    # update size2d with user input
                    global size2d
                    size2d = getInt(screen,'Enter size:')
                elif num_states_1d_button_rect.collidepoint(event.pos):
                    # update number of 1d states with user input
                    global n_states1d
                    n_states1d = getInt(screen,'Enter an integer between 2 and 5:')
                    while not (n_states1d >1 and n_states1d<6):
                        n_states1d = getInt(screen, 'Invalid input, please enter an integer between 1 and 5')
                elif num_states_2d_button_rect.collidepoint(event.pos):
                    # update number of 1d states with user input
                    global n_states2d
                    n_states2d = getInt(screen,'Enter an integer between 2 and 5:')
                    while not (n_states2d >1 and n_states2d<6):
                        n_states2d = getInt(screen, 'Invalid input, please enter an integer between 1 and 5')

        #Fill screen, draw button
        screen.fill(LIGHT_GRAY)

        screen.blit(rule2d_button, rule2d_button_rect)
        screen.blit(rule2db_button, rule2db_button_rect)
        screen.blit(rule1d_button, rule1d_button_rect)
        screen.blit(size1d_button, size1d_button_rect)
        screen.blit(size2d_button, size2d_button_rect)
        screen.blit(num_states_1d_button, num_states_1d_button_rect)
        screen.blit(num_states_2d_button, num_states_2d_button_rect)
        screen.blit(back_button, back_button_rect)

	# Update display and increment the clock
        pygame.display.update()
        clock.tick(FPS)

# Display a menu
def display_menu(screen):

    button_font = pygame.font.SysFont('FreeSans.otf',45)

    # Make some buttons
    cell_at_oned_button = button_font.render("Start 1-d cellular automaton",True,WHITE,BLACK)
    cell_at_oned_button_rect = cell_at_oned_button.get_rect()

    cell_at_twod_button = button_font.render("Start 2-d cellular automaton",True,WHITE,BLACK)
    cell_at_twod_button_rect = cell_at_twod_button.get_rect()

    settings_button = button_font.render("Settings",True,WHITE,BLACK)
    settings_button_rect = settings_button.get_rect()

    w_button = (WIDTH - cell_at_oned_button_rect.width)/2
    h_button = (HEIGHT - cell_at_oned_button_rect.height - cell_at_twod_button_rect.height - settings_button_rect.height)/4
    cell_at_oned_button_rect.topleft = (w_button, h_button)
    cell_at_twod_button_rect.topleft = (w_button, 2*h_button + cell_at_oned_button_rect.height)
    settings_button_rect.topleft = (w_button, 3*h_button + cell_at_oned_button_rect.height + cell_at_twod_button_rect.height)

    rect_list = [cell_at_oned_button_rect, cell_at_twod_button_rect, settings_button_rect]
    #layout_buttons(rect_list, 0, HEIGHT, 0, WIDTH)
    

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
                    run_1DAutomata(screen, size1d, rule1d, n_states1d)

            elif event.type == MOUSEBUTTONUP:
                if cell_at_oned_button_rect.collidepoint(event.pos):
                    # Run a 1-d cellular automaton
                    run_1DAutomata(screen, size1d, rule1d, n_states1d)
                elif cell_at_twod_button_rect.collidepoint(event.pos):
                    # Run a 2-d cellular automaton
                    run_2DAutomata(screen, size2d, rule2d, n_states2d)
                elif settings_button_rect.collidepoint(event.pos):
                    # Run display settings screen
                    settings(screen)
        #Fill screen, draw button
        screen.fill(LIGHT_GRAY)
        screen.blit(cell_at_oned_button, cell_at_oned_button_rect)
        screen.blit(cell_at_twod_button, cell_at_twod_button_rect)
        screen.blit(settings_button, settings_button_rect)

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
