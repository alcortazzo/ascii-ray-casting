class Field:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.field = [[col for col in range(num_cols)] for row in range(num_rows)]

    def create_ui(self):
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if (col == 0) or (col == len(self.field[row]) - 1) or (row == 0) or (row == len(self.field) - 1):
                    self.field[row][col] = "E"
                elif (col == 1) or col == (len(self.field[row]) - 2) or (row == 1) or (row == len(self.field) - 5):
                    self.field[row][col] = "S"
