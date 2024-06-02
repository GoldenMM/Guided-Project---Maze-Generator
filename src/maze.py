from src.graphics import *
import time

class Maze():
    '''A maze class which holds a grid of cells and the logic to draw them'''
    
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size,
        win = None, # Defaults to None for testing purposes
    ):
        # Check if all values are positive
        if x1 < 0 or y1 < 0 or num_rows < 0 or num_cols < 0 or cell_size < 0:
            raise ValueError("All values must be positive")
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        self._cells = []
        
        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self) -> None:
        '''Populate the cells in the maze.'''
        for x in range(self._num_cols):
            col = []
            for y in range(self._num_rows):
                cell = Cell(
                    self._x1 + x * self._cell_size,
                    self._y1 + y * self._cell_size,
                    self._cell_size,
                    self._win
                )
                col.append(cell)
            self._cells.append(col)
        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._draw_cell(x, y)
    
    def _draw_cell(self, i, j) -> None:
        '''Draw a cell at a given index'''
        if self._win: # If a window is provided, draw the cell
            self._cells[i][j].draw()
            self._animate()
    
    def _animate(self) -> None:
        self._win.redraw()
        time.sleep(0.05)
        
    def _break_entrance_and_exit(self) -> None:
        '''Break the entrance and exit walls'''
        self._cells[0][0].break_wall('top')
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].break_wall('bottom')
        self._draw_cell(self._num_cols-1, self._num_rows-1)