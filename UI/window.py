# Pygame import
import pygame

# Window settings
background_color = (244, 244, 244)
screensize = (500, 500)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Dice Sim')
screen.fill(background_color)
pygame.display.flip()


def __init__():
    # REVIEW Can be written neater
    from sys import path
    path.append('../DiceSim')
    from debug import info
    info(f"Pygame Version: {pygame.version.ver}")
    del path

    running = True

    while running:
        from UI.dice import draw
        draw()
        mousepos = pygame.mouse.get_pos()
        if ((screensize[0]/2) + 50 > mousepos[0] > (screensize[0]/2) - 50):
            # pygame.draw.rect(screen, (0, 0, 255), (150, 450, 100, 50))
            info("Moused over")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def get_screen(): return screen
def get_screen_dims(): return screensize
