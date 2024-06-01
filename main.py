from src.graphics import *
import random

window = Window(800, 600)

c1 = Cell(random.randint(0, 800), random.randint(0, 600), window)
c2 = Cell(random.randint(0, 800), random.randint(0, 600), window)

c1.draw()
c2.draw()

c2.draw_move(c1)

window.wait_for_close() 