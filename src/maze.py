from widgets import Cell,Line,Point,Window
import time
import random


class Maze():
    def __init__(self,x,y,num_cols,num_rows,cell_len_y,cell_len_x,window=None):
        self.x = x
        self.y = y
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_len_y = cell_len_y
        self.cell_len_x = cell_len_x
        self.w = window

        self._create_maze()
        self._break_entrance_and_exit()

    def _create_maze(self):
        self._cells = [
            [
                Cell(
                    Point(self.x + i * self.cell_len_x, self.y + j * self.cell_len_y),
                    self.cell_len_x,
                    self.cell_len_y,
                    self.w
                )
                for j in range(self.num_cols)
            ]
            for i in range(self.num_rows)
        ]

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(self._cells[i][j])

    def _draw_cell(self,cell,remove=False):
        if self.w is None:
            return
        if not remove:
            cell.draw("red")
        else:
            cell.erase("#d9d9d9")
        self._refresh()

    def _refresh(self):
        self.w.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.entrance = self._cells[0][0]
        self.exit = self._cells[self.num_rows-1][self.num_cols-1]
        self.entrance.has_top_wall = False
        self._draw_cell(self.entrance,remove=True)
        self.exit.has_bottom_wall = False
        self._draw_cell(self.exit,remove=True)

    def _create_paths(self):



        
