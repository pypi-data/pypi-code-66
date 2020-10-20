
import curses
from typing import Union


class Grid:
    def __init__(self, rows:int, columns:int, screen,
                 x:int = 0, y:int = 0,
                 width:Union[int, str] = "auto",
                 height:Union[int, str] = "auto"):
        self.rows:int = rows
        self.columns:int = columns
        self.screen:int = screen
        self.x:int = x
        self.y:int = y
        self.width:int = width
        self.height:int = height

    def get_x_coords(self) -> list[int]:
        width = self.get_width()
        step = int(width / self.columns)
        return [x for x in range(self.x, step * self.columns, step)]

    def get_y_coords(self) -> list[int]:
        height = self.get_height()
        step = int(height / self.rows)
        return [y for y in range(self.y, step * self.rows, step)]

    def get_corners(self) -> tuple[int, int, int, int]:
        x1, y1, = self.x, self.y
        x2 = self.get_width()
        y2 = self.get_height()
        return x1, y1, x2, y2

    def get_width(self) -> int:
        if self.width == "auto":
            return self.screen.getmaxyx()[1]
        else:
            return self.width

    def get_height(self) -> int:
        if self.height == "auto":
            return self.screen.getmaxyx()[0]
        else:
            return self.height

    def get_dimensions(self) -> tuple[int, int]:
        return self.get_width(), self.get_height()

    def get_cell_width(self) -> int:
        ...

    def get_cell_height(self) -> int:
        ...

    def debug_draw_outline(self):
        width, height = self.get_dimensions()
        cell_x_coords = self.get_x_coords()
        cell_y_coords = self.get_y_coords()

        for x in range(self.x, self.get_width()):
            for y in range(self.y, self.get_height()):
                # Corners
                if x == self.x and y == self.y:
                    self.screen.addstr(y, x, '┌')
                elif x == self.x + width and y == self.y:
                    self.screen.addstr(y, x, '┐')
                elif x == self.x and y == self.y + height:
                    self.screen.addstr(y, x, '└')
                elif x == self.x + width and y == self.y + height:
                    self.screen.addstr(y, x, '┘')
                # Top cross beams
                elif x in cell_x_coords and y == self.y:
                    self.screen.addstr(y, x, '┬')
                # Bottom cross beams
                elif x in cell_x_coords and y == self.y + height:
                    self.screen.addstr(y, x, '┴')
                # Left cross beams
                elif y in cell_y_coords and x == self.x:
                    self.screen.addstr(y, x, '├')
                # Right cross beams
                elif y in cell_y_coords and x == self.x + width:
                    self.screen.addstr(y, x, '┤')
                # Center cross beams
                elif x in cell_x_coords and y in cell_y_coords:
                    self.screen.addstr(y, x, '┼')
                # Top or bottom edges
                elif y == self.y or y == self.y + height:
                    self.screen.addstr(y, x, '─')
                # Left or right edges
                elif x == self.x or x == self.x + width:
                    self.screen.addstr(y, x, '│')
                # Center vertical lines
                elif x in cell_x_coords:
                    self.screen.addstr(y, x, '│')
                # Center horizontal lines
                elif y in cell_y_coords:
                    self.screen.addstr(y, x, '─')


class Cell:
    def __init__(self):
        ...



