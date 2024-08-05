from widgets import Cell, Line, Point, Window
import time
import random


class Maze():
    def __init__(self, x, y,
                 num_cols, num_rows,
                 cell_len_y, cell_len_x,
                 window=None, seed=None
                 ):
        self.x = x
        self.y = y
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_len_y = cell_len_y
        self.cell_len_x = cell_len_x
        self.w = window
        self.seed = seed
        self._create_maze()
        self._break_entrance_and_exit()
        self.create_paths()
        print(self.find_path())

    def _create_maze(self):
        self._cells = [
            [
                Cell(
                    Point(self.x + j * self.cell_len_x,
                          self.y + i * self.cell_len_y),
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

    def _draw_cell(self, cell, remove=False):
        if self.w is None:
            return
        if not remove:
            cell.draw("black")
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
        self._draw_cell(self.entrance, remove=True)
        self.exit.has_bottom_wall = False
        self._draw_cell(self.exit, remove=True)

    def create_paths(self):
        random.seed(self.seed)
        visited = [[0 for j in range(self.num_cols)]
                   for i in range(self.num_rows)]
        self._break_walls_r(0, 0, visited)

    def _break_walls_r(self, vert, hori, visited):
        visited[vert][hori] = 1
        while True:
            neighbours = self._add_neighbours(vert, hori, visited)
            if len(neighbours) == 0:
                return
            else:
                dir = random.choice(neighbours)
                next_vert, next_hori = self._move(dir, vert, hori)
                self._break_wall(
                    self._cells[vert][hori], self._cells[next_vert][next_hori],
                    dir
                )
                self._break_walls_r(next_vert, next_hori, visited)

    def _add_neighbours(self, vert, hori, visited, can_break=True):
        neighbours = []
        cell = self._cells[vert][hori]

        if vert-1 >= 0 and visited[vert-1][hori] == 0:
            if can_break or not cell.has_top_wall:
                neighbours.append(1)

        if hori+1 <= self.num_cols-1 and visited[vert][hori+1] == 0:
            if can_break or not cell.has_right_wall:
                neighbours.append(2)

        if vert+1 <= self.num_rows-1 and visited[vert+1][hori] == 0:
            if can_break or not cell.has_bottom_wall:
                neighbours.append(3)

        if hori-1 >= 0 and visited[vert][hori-1] == 0:
            if can_break or not cell.has_left_wall:
                neighbours.append(4)

        return neighbours

    def _break_wall(self, cell, next_cell, dir):
        if dir == 1:
            cell.has_top_wall = False
            next_cell.has_bottom_wall = False

        elif dir == 2:
            cell.has_right_wall = False
            next_cell.has_left_wall = False

        elif dir == 3:
            cell.has_bottom_wall = False
            next_cell.has_top_wall = False

        elif dir == 4:
            cell.has_left_wall = False
            next_cell.has_right_wall = False

        self._draw_cell(cell, remove=True)
        self._draw_cell(next_cell, remove=True)

    def _move(self, dir, vert, hori):
        if dir == 1:
            return vert-1, hori

        elif dir == 2:
            return vert, hori+1

        elif dir == 3:
            return vert+1, hori

        elif dir == 4:
            return vert, hori-1

    def find_path(self):
        visited = [[0 for j in range(self.num_cols)]
                   for i in range(self.num_rows)]
        return self._solve(0, 0, visited)

    def _solve(self, vert, hori, visited):
        self._refresh()
        visited[vert][hori] = 1
        neighbours = self._add_neighbours(vert, hori, visited, can_break=False)

        if vert == self.num_rows-1 and hori == self.num_cols-1:
            return True

        for dir in neighbours:
            next_vert, next_hori = self._move(dir, vert, hori)
            self._cells[vert][hori].draw_move(
                self._cells[next_vert][next_hori])
            success = self._solve(next_vert, next_hori, visited)
            if success:
                return success
            else:
                self._cells[vert][hori].draw_move(
                    self._cells[next_vert][next_hori], undo=True)

        return False
