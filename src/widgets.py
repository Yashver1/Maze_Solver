from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Window")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

        print("closing window...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)


class Cell():
    def __init__(self, start_point, length_x, length_y, window):
        self.__x1, self.__y1 = start_point.x, start_point.y
        self.__x2, self.__y2 = (self.__x1+length_x), (self.__y1+length_y)
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.__w = window
        self.center_x, self.center_y = (
            self.__x1+self.__x2)/2, (self.__y1 + self.__y2)/2

    def draw(self, fill_color):
        if self.has_top_wall:
            self.__w.draw_line(
                Line(Point(self.__x1, self.__y1),
                     Point(self.__x2, self.__y1)),
                fill_color)
        if self.has_right_wall:
            self.__w.draw_line(
                Line(Point(self.__x2, self.__y1),
                     Point(self.__x2, self.__y2)),
                fill_color)
        if self.has_bottom_wall:
            self.__w.draw_line(
                Line(Point(self.__x2, self.__y2),
                     Point(self.__x1, self.__y2)),
                fill_color)
        if self.has_left_wall:
            self.__w.draw_line(
                Line(Point(self.__x1, self.__y2),
                     Point(self.__x1, self.__y1)),
                fill_color)

    def erase(self, fill_color):
        if not self.has_top_wall:
            self.__w.draw_line(
                Line(Point(self.__x1, self.__y1),
                     Point(self.__x2, self.__y1)),
                fill_color)
        if not self.has_right_wall:
            self.__w.draw_line(
                Line(Point(self.__x2, self.__y1),
                     Point(self.__x2, self.__y2)),
                fill_color)
        if not self.has_bottom_wall:
            self.__w.draw_line(
                Line(Point(self.__x2, self.__y2),
                     Point(self.__x1, self.__y2)),
                fill_color)
        if not self.has_left_wall:
            self.__w.draw_line(
                Line(Point(self.__x1, self.__y2),
                     Point(self.__x1, self.__y1)),
                fill_color)

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        x, y = to_cell.center_x, to_cell.center_y
        self.__w.draw_line(
            Line(Point(self.center_x, self.center_y), Point(x, y)), color)
