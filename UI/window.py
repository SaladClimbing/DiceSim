# Pygame import
import pygame
# Personal imports
from UI.dice import Dice
from UI.buttons.buttonmanager import clicked
from data.datahandler import getdh
# Debug imports
#from logging import info, basicConfig, DEBUG
# basicConfig(level=DEBUG,
#            format='%(name)s - %(levelname)s : %(message)s')

# region Window settings
background_color = (244, 244, 244)
screensize = (500, 500)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Dice Sim')
screen.fill(background_color)
pygame.display.flip()
# endregion

die = Dice(screensize)
dh = getdh()


def update():
    die.draw(screen)  # Draws the die
    if pygame.mouse.get_pressed()[0] and not dh.pressed:
        mousepos = pygame.mouse.get_pos()
        clicked(mousepos)
        dh.pressed = True
    elif not pygame.mouse.get_pressed()[0]:
        dh.pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def get_screen(): return screen
def get_screen_dims(): return screensize
