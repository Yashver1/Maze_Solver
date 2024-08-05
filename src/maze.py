from widgets import Cell,Line,Point,Window
import time


class Maze():
    def __init__(self,x,y,num_cols,num_rows,cell_len_y,cell_len_x,window):
        self.x = x
        self.y = y
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_len_y = cell_len_y
        self.cell_len_x = cell_len_x
        self.w = window

        self._create_maze()

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

    def _draw_cell(self,cell):
        cell.draw("red")
        self._refresh()

    def _refresh(self):
        self.w.redraw()
        time.sleep(0.05)


        
