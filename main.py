import pygame
from sys import exit
import random

pygame.init()

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("random position move to")

bgColor = (50, 50, 50)

x_af, y_af = (0, 0)
x_sto, y_sto = (0, 300)
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (300, 200))

def random_player_pos_x():
    x_bef = random.randint(0, 600)
    return x_bef
def random_player_pos_y():
    y_bef = random.randint(0, 600)
    return y_bef

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(bgColor)

    if x_sto == x_af and y_sto == y_af:
        x_sto = random_player_pos_x()
        y_sto = random_player_pos_y()
    else:
        if x_af < x_sto:
            x_af += 1
        elif x_af > x_sto:
            x_af -= 1
        if y_af < y_sto:
            y_af += 1
        elif y_af > y_sto:
            y_af -= 1
    
    screen.blit(player_img, (x_af, y_af))

    pygame.display.update()


exit()
