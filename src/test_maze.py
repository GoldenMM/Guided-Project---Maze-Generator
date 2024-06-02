import unittest
from maze import *
from graphics import *

class Tests(unittest.TestCase):
    def test_init_value_error(self):
        with self.assertRaises(ValueError):
            Maze(-1, 0, 10, 10, 10)
        with self.assertRaises(ValueError):
            Maze(0, -1, 10, 10, 10)
        with self.assertRaises(ValueError):
            Maze(0, 0, -1, 10, 10)
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, -1, 10)
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, 10, -1)
    
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_cell_access(self):
        num_cols = 5
        num_rows = 5
        m4 = Maze(20, 20, num_rows, num_cols, 10)
        self.assertIsNotNone(m4._cells[0][0])
        self.assertIsNotNone(m4._cells[num_cols-1][num_rows-1])

if __name__ == "__main__":
    unittest.main()