###This program creates a window and then assigns each pixel a selected color randomly

import pygame, random, sys

#SETS UP SCREEN
screen_x = 800
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))

#COLORS RGB
BLACK = (0,0,0)
NAVY = (0,0,128)
LAVENDER = (230,230,250)
POWDER_BLUE = (176, 224, 230)
CYAN = (0, 255, 255)
LIGHT_YELLOW2= (255, 255, 153)

colors = [BLACK, NAVY, LAVENDER, POWDER_BLUE, CYAN, LIGHT_YELLOW2]

#init pygame
pygame.display.init

#variables
box_side = 10
running = True

#asigns each pixel a color randomly
def random_screen():
    b = 1
    c = 1
    screen_size = screen_x * screen_y
    while screen_size > 0:
        a = random.randint(0,5)
        if b < screen_x:
            pygame.draw.rect(screen, colors[a], pygame.Rect(b,c,box_side,box_side))
            screen_size -= 1
            b += box_side
        else:

            b = 0
            c += box_side
            screen_size -= 1       

#main loop#
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
                pygame.quit()
                sys.exit()
        else:
            screen
            random_screen()
            pygame.display.flip()
