from widgets import Window, Line, Point, Cell
from maze import Maze



def main():
    win = Window(400,400 )
    maze = Maze(10,10,15,15,40,40,win)
    win.wait_for_close()
main()
