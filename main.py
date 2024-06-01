from src.graphics import *
from src.maze import *

window = Window(800, 600)

maze = Maze(x1=20, y1=20,
            num_rows=15, num_cols=15,
            cell_size=20,
            win=window)

window.wait_for_close() 