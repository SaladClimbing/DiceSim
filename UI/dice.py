# Pygame imports
from pygame import draw as render
from pygame import display, Rect
from UI.window import get_screen, get_screen_dims
import pickle

color = (0, 0, 0)
screensize = get_screen_dims()
size = 50

# TODO Make only in dev
with open('config', 'wb') as file:
    pickle.dump(size, file)


def draw():
    rectstartx = (screensize[0]/2) - (size/2)
    rectstarty = (screensize[1]/2) - (size/2)

    render.rect(get_screen(), color, Rect(
        rectstartx, rectstarty, size, size), 2, 3)
    display.flip()
