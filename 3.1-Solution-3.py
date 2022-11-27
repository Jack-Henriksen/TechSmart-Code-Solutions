"""
LESSON: 3.1 - Lines
EXERCISE: Code Your Own

TITLE: Discord Logo (Sort Of)
DESCRIPTION: Discord Logo made with Pygame.
"""
import pygame as pg
pg.init()
blurple = (114, 137, 217)
window = pg.display.set_mode([500, 500])

pg.draw.line(window, blurple, (400, 20), (450, 200), 15)
pg.draw.line(window, blurple, (450, 200), (300, 170), 15)
pg.draw.line(window, blurple, (300, 170), (150, 200), 15)
pg.draw.line(window, blurple, (150, 200), (200, 20), 15)
pg.draw.line(window, blurple, (200, 20), (400, 20), 15)
pg.draw.line(window, blurple, (230, 70), (280, 70), 40)
pg.draw.line(window, blurple, (330, 70), (380, 70), 40)


pg.display.flip()
input("Press enter to close the window")

#Blurple Color RGB: (114, 137, 217)

