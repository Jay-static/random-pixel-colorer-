###This program creates a window and then assigns each pixel a selected color randomly

import pygame, random

#init pygame
pygame.display.init

#SETS UP SCREEN
screen_x = 800
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))

#COLORS RGB
COLOR_1 = (0,105,10)
COLOR_2 = (5,155,20)
COLOR_3 = (10,155,40)
COLOR_4 = (20,205,80)
COLOR_5 = (40,205,160)
COLOR_6 = (80,255,255)

colors = [COLOR_1, COLOR_2, COLOR_3, COLOR_4, COLOR_5, COLOR_6]

#variables
box_side = 25
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
                quit()
        else:
            screen
            random_screen()
            pygame.display.flip()
