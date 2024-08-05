from widgets import Window, Line, Point, Cell
from maze import Maze

CELL_LENGTH = 40


def main():

    win = Window(800, 600)
    maze = Maze(10,10,15,15,40,40,win)
    
    win.wait_for_close()


main()
