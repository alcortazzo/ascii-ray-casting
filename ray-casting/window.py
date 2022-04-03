import sys
import curses
import time

from ui import UserInterface


class Window:
    def __init__(self) -> None:
        curses.initscr()

        curses.noecho()
        curses.curs_set(False)
        curses.endwin()

        curses.wrapper(self.window)

    def check_size(self, num_rows: int, num_cols: int) -> bool:
        if (num_cols < 30) or (num_rows < 20):
            return False
        else:
            return True

    def show_ui(self, stdscr, ui: UserInterface):
        for row in range(len(ui.ui)):
            for col in range(len(ui.ui[row])):
                if (row == len(ui.ui)) - 1 and (col == len(ui.ui[row]) - 1):
                    continue
                to_print = ui.ui[row][col] if isinstance(ui.ui[row][col], str) else " "
                stdscr.addstr(row, col, to_print)
                stdscr.refresh()

    def window(self, stdscr):
        stdscr.clear()

        num_rows, num_cols = stdscr.getmaxyx()
        if not self.check_size(num_rows=num_rows, num_cols=num_cols):
            sys.exit()

        ui = UserInterface(num_rows=num_rows, num_cols=num_cols)
        ui.initialize_borders()
        ui.initialize_text()
        self.show_ui(stdscr, ui)
        time.sleep(10)
