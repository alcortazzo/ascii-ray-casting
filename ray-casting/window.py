import curses

from ui import UserInterface
from field import Field
from rays import calculate_rays


class Window:
    def __init__(self) -> None:
        curses.initscr()

        curses.noecho()
        curses.curs_set(False)
        curses.endwin()

        curses.wrapper(self.window)

    def check_size(self, num_rows: int, num_cols: int) -> bool:
        if (num_cols < 36) or (num_rows < 15):
            return False
        else:
            return True

    def show_ui(self, stdscr, ui: UserInterface):
        for row in range(len(ui.ui)):
            for col in range(len(ui.ui[row])):
                if (row == len(ui.ui) - 1) and (col == len(ui.ui[row]) - 1):
                    continue
                to_print = ui.ui[row][col] if isinstance(ui.ui[row][col], str) else " "
                stdscr.addstr(row, col, to_print)
        stdscr.refresh()

    def show_field(self, stdscr, field: Field):
        for row in range(len(field.field)):
            for col in range(len(field.field[row])):
                stdscr.addstr(row + field.top_indent, col + field.left_indent, field.field[row][col])
        stdscr.refresh()

    def window(self, stdscr):
        stdscr.clear()

        num_rows, num_cols = stdscr.getmaxyx()
        if not self.check_size(num_rows=num_rows, num_cols=num_cols):
            raise Exception("Window is too small.")

        ui = UserInterface(num_rows=num_rows, num_cols=num_cols)
        ui.initialize_borders()
        ui.initialize_text()
        self.show_ui(stdscr, ui)

        field = Field(ui=ui.ui)
        self.show_field(stdscr, field)

        started = False
        while True:
            if started:
                calculate_rays(field=field)
            self.show_field(stdscr, field)

            key = stdscr.getch()

            if key == ord("w") or key == curses.KEY_UP:
                field.move_user("up")
            elif key == ord("s") or key == curses.KEY_DOWN:
                field.move_user("down")
            elif key == ord("a") or key == curses.KEY_LEFT:
                field.move_user("left")
            elif key == ord("d") or key == curses.KEY_RIGHT:
                field.move_user("right")
            elif key == ord("e"):
                started = True
            elif key == ord("r"):
                field.reset_field()
                started = False
            elif key == ord(" "):
                field.create_wall()
            elif key == ord("q"):
                raise Exception("Quit")
