# Pygame import
import pygame
# Personal imports
from UI.dice import Dice
from UI.buttons.buttonmanager import click
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


def update():
    die.draw(screen)  # Draws the die
    die.roll()
    if pygame.mouse.get_pressed()[0] == True:
        mousepos = pygame.mouse.get_pos()
        click(mousepos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def get_screen(): return screen
def get_screen_dims(): return screensize
