import unittest
from maze import Maze
from widgets import Window


class Tests(unittest.TestCase):
    def test_maze_cols_rows(self):
        num_of_cols = 12
        num_of_rows = 10
        maze = Maze(0, 0, num_of_cols, num_of_rows, 0, 0)
        self.assertEqual(
            maze.num_cols, num_of_cols
        )
        self.assertEqual(
            maze.num_rows, num_of_rows
        )

    def test_maze_cell_length(self):
        num_of_cols = 0
        num_of_rows = 0
        x_length = 10
        y_length = 10
        maze = Maze(0, 0, num_of_cols, num_of_rows, x_length, y_length)
        self.assertEqual(
            x_length, maze.cell_len_x
        )
        self.assertEqual(
            y_length, maze.cell_len_y
        )

    def test_maze_create_maze(self):
        num_of_cols = 12
        num_of_rows = 10
        x_length = 10
        y_length = 10
        maze = Maze(0, 0, num_of_cols, num_of_rows, x_length, y_length)
        self.assertEqual(
            x_length, maze.cell_len_x
        )
        self.assertEqual(
            y_length, maze.cell_len_y
        )
