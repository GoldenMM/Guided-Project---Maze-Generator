from tkinter import Tk, BOTH, Canvas
cell_size = 20

class Window():
    ''' A simple window class that uses tkinter to create a window with a canvas.'''
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title = "Maze Generator"
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self) -> None:
        ''' Redraw the window.'''
        self.__canvas.update_idletasks()
        self.__canvas.update()

    def wait_for_close(self) -> None:   
        ''' Wait for the window to close.'''
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self) -> None:
        ''' Close the window.'''
        self.is_running = False
        
    def draw_line(self, line, color="black") -> None:
        ''' Draw a line on the canvas.'''
        line.draw(self.__canvas, color)
        
class Point():
    ''' A simple point class that holds an x and y value.'''
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
class Line():
    ''' A simple line class that holds two points.'''
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        
    def draw(self, canvas, color="black"):
        ''' Draw the line on the canvas.'''
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)
        
class Cell():
    '''A simple cell with a position and walls'''
    def __init__(self, x, y, window) -> None:
        self._x1 = x - cell_size // 2
        self._y1 = y - cell_size // 2
        self._x2 = x + cell_size // 2
        self._y2 = y + cell_size // 2
        self._x = x
        self._y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self._window = window
    
    def draw(self) -> None:
        '''Draw the cell on the canvas.'''
        if self.walls['top']:
            self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.walls['right']:
            self._window.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.walls['bottom']:
            self._window.draw_line(Line(Point(self._x2, self._y2), Point(self._x1, self._y2)))
        if self.walls['left']:
            self._window.draw_line(Line(Point(self._x1, self._y2), Point(self._x1, self._y1)))

    def draw_move(self, to_cell, undo=False) -> None:
        if undo:
            color = "grey"
        else:
            color = "red"
        self._window.draw_line(Line(Point(self._x, self._y), Point(to_cell._x, to_cell._y)), color=color)