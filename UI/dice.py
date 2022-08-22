# Pygame imports
from pygame import draw as render
from pygame import display, Rect, font, init
# Personal imports
from UI.buttons.buttonmanager import add_button

import pickle

# TODO Make only in dev
with open('config', 'wb') as file:
    pickle.dump(50, file)

init()


class Dice:

    def __init__(self, screensize):
        self.color = (0, 0, 0)
        self.size = 50
        self.rectstartx = (screensize[0]/2) - (self.size/2)
        self.rectstarty = (screensize[1]/2) - (self.size/2)
        self.rectstart = (self.rectstartx, self.rectstarty)
        self.font = font.SysFont("timesnewroman", 30)
        self.text = self.__rendertext('1')
        self.textRect = self.text.get_rect()
        self.textRect
        self.textRect.center = (
            self.rectstartx + self.size // 2, self.rectstarty + self.size // 2)
        add_button("dice", (self.rectstartx, self.rectstarty), self.size)

    def draw(self, screen):
        render.rect(screen, self.color, Rect(
            self.rectstartx, self.rectstarty, self.size, self.size), 2, 3)
        screen.blit(self.text, self.textRect)
        display.flip()

    def __rendertext(self, str):
        return self.font.render(str, True, (0, 0, 0), (255, 255, 255))

    def roll(self):
        self.text = self.__rendertext('2')
        return
