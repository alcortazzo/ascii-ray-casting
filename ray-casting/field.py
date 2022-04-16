class Field:
    def __init__(self, ui: list) -> None:
        self.calculate_indents(ui)
        self.initialize_field()
        self.initialize_user()

    def calculate_indents(self, ui) -> None:
        self.left_indent = self.right_indent = self.top_indent = self.bottom_indent = 0
        for row in range(len(ui)):
            if not isinstance(ui[row][2], int):
                if self.bottom_indent and self.right_indent:
                    break
                else:
                    continue
            for col in range(len(ui[row])):
                if isinstance(ui[row][col], int):
                    if not self.top_indent and not self.left_indent:
                        self.top_indent = row
                        self.left_indent = col
                    self.bottom_indent = row
                    self.right_indent = col

    def initialize_field(self) -> None:
        self.field = [
            [" " for col in range(self.right_indent - self.left_indent + 1)]
            for row in range(self.bottom_indent - self.top_indent + 1)
        ]

    def initialize_user(self) -> None:
        self.field[len(self.field) // 2][len(self.field[0]) // 2] = "O"
        self.user_coordinates = (len(self.field) // 2, len(self.field[0]) // 2)

    # TODO: Refactor this method
    def move_user(self, direction: str) -> None:
        if direction == "up":
            if self.user_coordinates[0] > 0 and self.field[self.user_coordinates[0] - 1][self.user_coordinates[1]] != "#":
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = " "
                self.user_coordinates = (self.user_coordinates[0] - 1, self.user_coordinates[1])
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = "O"
        elif direction == "down":
            if self.user_coordinates[0] < len(self.field) - 1 and self.field[self.user_coordinates[0] + 1][self.user_coordinates[1]] != "#":
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = " "
                self.user_coordinates = (self.user_coordinates[0] + 1, self.user_coordinates[1])
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = "O"
        elif direction == "left":
            if self.user_coordinates[1] > 0 and self.field[self.user_coordinates[0]][self.user_coordinates[1] - 1] != "#":
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = " "
                self.user_coordinates = (self.user_coordinates[0], self.user_coordinates[1] - 1)
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = "O"
        elif direction == "right":
            if self.user_coordinates[1] < len(self.field[0]) - 1 and self.field[self.user_coordinates[0]][self.user_coordinates[1] + 1] != "#":
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = " "
                self.user_coordinates = (self.user_coordinates[0], self.user_coordinates[1] + 1)
                self.field[self.user_coordinates[0]][self.user_coordinates[1]] = "O"

    # TODO: Refactor this method
    def create_wall(self) -> None:
        self.field[self.user_coordinates[0]][self.user_coordinates[1]] = "#"
        if self.user_coordinates[0] < len(self.field) - 1 and self.field[self.user_coordinates[0] + 1][self.user_coordinates[1]] != "#":
            self.user_coordinates = (self.user_coordinates[0] + 1, self.user_coordinates[1])
            self.field[self.user_coordinates[0]][self.user_coordinates[1]] = "O"
        elif self.user_coordinates[0] > 0 and self.field[self.user_coordinates[0] - 1][self.user_coordinates[1]] != "#":
            self.user_coordinates = (self.user_coordinates[0] - 1, self.user_coordinates[1])
            self.field[self.user_coordinates[0]][self.user_coordinates[1]] = "O"
