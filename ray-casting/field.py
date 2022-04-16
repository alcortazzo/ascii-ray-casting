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
            [col for col in range(self.right_indent - self.left_indent + 1)]
            for row in range(self.bottom_indent - self.top_indent + 1)
        ]

    def initialize_user(self) -> None:
        self.field[len(self.field) // 2][len(self.field[0]) // 2] = "O"
