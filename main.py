from src.graphics import *
import random

window = Window(800, 600)

c1 = Cell(20, 100, window)
c2 = Cell(100, 100, window)

c1.draw()
c2.draw()

c2.draw_move(c1)

window.wait_for_close() 