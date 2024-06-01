import unittest, unittest.mock
from graphics import *


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(10, 20)

    def test_init(self):
        self.assertEqual(self.point.x, 10)
        self.assertEqual(self.point.y, 20)

    def test_str(self):
        self.assertEqual(str(self.point), "(10, 20)")

    def test_eq(self):
        self.assertTrue(self.point == Point(10, 20))
        self.assertFalse(self.point == Point(20, 10))

class TestLine(unittest.TestCase):
    def setUp(self):
        self.window = Window(800, 600)
        self.start = Point(10, 10)
        self.end = Point(20, 20)
        self.line = Line(self.start, self.end)

    def test_init(self):
        self.assertEqual(self.line.start, self.start)
        self.assertEqual(self.line.end, self.end)

    def test_draw(self):
        with unittest.mock.patch('tkinter.Canvas.create_line') as mocked_create_line:
            self.line.draw(self.window._Window__canvas)
            mocked_create_line.assert_called_once_with(self.start.x, self.start.y, self.end.x, self.end.y, fill="black", width=2)

class TestCell(unittest.TestCase):
    def setUp(self):
        self.window = Window(800, 600)
        self.cell = Cell(10, 10, self.window)

    def test_init(self):
        self.assertEqual(self.cell.x, 10)
        self.assertEqual(self.cell.y, 10)
        self.assertEqual(self.cell.walls, {'top': True, 'right': True, 'bottom': True, 'left': True})

    def test_init_value_error(self):
        with self.assertRaises(ValueError): # Test x lower than cell_size/2
            Cell((cell_size/2) -1 , 10, self.window)
        with self.assertRaises(ValueError): # Test x higher than window.width - cell_size/2
            Cell(self.window.width - (cell_size/2) + 1, 10, self.window)
        with self.assertRaises(ValueError): # Test y lower than cell_size/2
            Cell(10, (cell_size/2) - 1, self.window)
        with self.assertRaises(ValueError): # Test y higher than window.height - cell_size/2
            Cell(10, self.window.height - (cell_size/2) + 1, self.window)
            
            
if __name__ == '__main__':
    unittest.main()