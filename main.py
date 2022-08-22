# Pygame imports
from pygame import version
# Personal imports
from UI.window import update
# Degbug imports
# from logging import info, basicConfig, DEBUG
# basicConfig(level=DEBUG,
#             format='%(name)s - %(levelname)s : %(message)s')

# Game loop
while True:
    if not update():  # Check if the window is closed
        break
