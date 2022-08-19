# Pygame imports
from pygame import draw as render
from pygame import display, Rect
# Personal imports
from UI.buttons.buttonmanager import add_button

import pickle

# TODO Make only in dev
with open('config', 'wb') as file:
    pickle.dump(50, file)


class Dice:

    def __init__(self, screensize):
        self.color = (0, 0, 0)
        self.size = 50
        self.rectstartx = (screensize[0]/2) - (self.size/2)
        self.rectstarty = (screensize[1]/2) - (self.size/2)
        add_button("dice", (self.rectstartx, self.rectstarty), self.size)

    def draw(self, screen):
        render.rect(screen, self.color, Rect(
            self.rectstartx, self.rectstarty, self.size, self.size), 2, 3)
        display.flip()
