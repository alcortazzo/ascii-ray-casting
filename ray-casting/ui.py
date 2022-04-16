TEXT_UI: list = ["move character: W,A,S,D", "create wall block: C", "start: E | quit: Q"]


class UserInterface:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.ui = [[col for col in range(num_cols)] for row in range(num_rows)]

    def initialize_borders(self):
        row_num = len(self.ui)
        for row in range(row_num):
            col_num = len(self.ui[row])
            for col in range(col_num):
                if (col in [0, col_num - 1, col_num - 2]) or (row in [0, row_num - 1]):
                    self.ui[row][col] = " "
                elif (col in [1, col_num - 3]) or (row in [1, row_num - 2, row_num - 6]):
                    self.ui[row][col] = "#"

    def initialize_text(self):
        x1 = len(self.ui) - 5
        y1 = 2
        x2 = len(self.ui) - 3
        y2 = len(self.ui[0][0]) - 5

        line = 0
        for string in TEXT_UI:
            cursor = 1
            for letter in string:
                self.ui[x1 + line][y1 + cursor] = letter
                cursor += 1
            line += 1
