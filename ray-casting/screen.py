import sys
import curses

from field import Field


class Screen:
    def __init__(self) -> None:
        self.window = curses.initscr()

        curses.noecho()
        curses.curs_set(False)
        curses.endwin()

        curses.wrapper(self.display)

    def check_size(self, num_rows: int, num_cols: int) -> bool:
        if (num_cols < 30) or (num_rows < 20):
            return False
        else:
            return True

    def show_ui(self, stdscr, field: Field):
        for row in range(len(field.field)):
            for col in range(len(field.field[row])):
                if (row == len(field.field)) - 1 and (col == len(field.field[row]) - 1):
                    continue
                to_print = field.field[row][col] if isinstance(field.field[row][col], str) else " "
                stdscr.addstr(row, col, to_print)
                stdscr.refresh()

    def display(self, stdscr):
        stdscr.clear()

        num_rows, num_cols = stdscr.getmaxyx()
        if not self.check_size(num_rows=num_rows, num_cols=num_cols):
            sys.exit()

        field = Field(num_rows=num_rows, num_cols=num_cols)
        field.create_ui()
        self.show_ui(stdscr, field)
