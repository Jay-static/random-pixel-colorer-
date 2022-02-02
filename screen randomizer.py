###This program creates a window and then assigns each pixel a selected color randomly

import pygame, random,

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

#init pygame
pygame.display.init

#variables
box_side = 1

#asigns each pixel a color randomly
def random_screen():
    b = 1
    c = 1
    screen_size = screen_x * screen_y
    while screen_size > 0:
        a = random.randint(1,6)
        if b < screen_x:
            if a == 1:
                pygame.draw.rect(screen, BLACK, pygame.Rect(b,c,box_side,box_side))
            elif a == 2:
                pygame.draw.rect(screen, NAVY, pygame.Rect(b,c,box_side,box_side))
            elif a == 3:
                pygame.draw.rect(screen, LAVENDER, pygame.Rect(b,c,box_side,box_side))
            elif a == 4:
                pygame.draw.rect(screen, POWDER_BLUE, pygame.Rect(b,c,box_side,box_side))
            elif a == 5:
                pygame.draw.rect(screen, CYAN, pygame.Rect(b,c,box_side,box_side))
            elif a == 6:
                pygame.draw.rect(screen, LIGHT_YELLOW2, pygame.Rect(b,c,box_side,box_side))
            screen_size -= 1
            b += box_side
        else:

            b = 0
            c += box_side
            screen_size -= 1       

#main loop#
while True:
    screen
    random_screen()
    pygame.display.flip()
    



