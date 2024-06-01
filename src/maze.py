from src.graphics import *
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        self._cells = []
        
        self._create_cells()
    
    def _create_cells(self):
        for x in range(self._num_cols):
            col = []
            for y in range(self._num_rows):
                cell = Cell(
                    self._x1 + x * self._cell_size,
                    self._y1 + y * self._cell_size,
                    self._win,
                    self._cell_size
                )
                col.append(cell)
            self._cells.append(col)
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._draw_cell(x, y)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)