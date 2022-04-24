from field import Field

RAY_SYMBOL = "+"
WALL_SYMBOL = "#"


def calculate_rays(field: Field):
    for row in range(len(field.field)):
        for col in range(len(field.field[row])):
            if field.field[row][col] == RAY_SYMBOL:
                field.field[row][col] = " "

    UP_ROWS = [_ for _ in range(0, field.user_coordinates[0])][::-1]
    DOWN_ROWS = [_ for _ in range(field.user_coordinates[0] + 1, len(field.field))]
    RIGHT_COLS = [_ for _ in range(field.user_coordinates[1] + 1, len(field.field[0]))]
    LEFT_COLS = [_ for _ in range(0, field.user_coordinates[1])][::-1]

    # UP
    for row in UP_ROWS:
        if field.field[row][field.user_coordinates[1]] == WALL_SYMBOL:
            break
        field.field[row][field.user_coordinates[1]] = RAY_SYMBOL

    # UP-LEFT
    for row, col in zip(UP_ROWS, LEFT_COLS):
        if field.field[row][col] == WALL_SYMBOL:
            break
        field.field[row][col] = RAY_SYMBOL

    # UP-RIGHT
    for row, col in zip(UP_ROWS, RIGHT_COLS):
        if field.field[row][col] == WALL_SYMBOL:
            break
        field.field[row][col] = RAY_SYMBOL

    # DOWN
    for row in DOWN_ROWS:
        if field.field[row][field.user_coordinates[1]] == WALL_SYMBOL:
            break
        field.field[row][field.user_coordinates[1]] = RAY_SYMBOL

    # DOWN-LEFT
    for row, col in zip(DOWN_ROWS, LEFT_COLS):
        if field.field[row][col] == WALL_SYMBOL:
            break
        field.field[row][col] = RAY_SYMBOL

    # DOWN-RIGHT
    for row, col in zip(DOWN_ROWS, RIGHT_COLS):
        if field.field[row][col] == WALL_SYMBOL:
            break
        field.field[row][col] = RAY_SYMBOL

    # LEFT
    for col in LEFT_COLS:
        if field.field[field.user_coordinates[0]][col] == WALL_SYMBOL:
            break
        field.field[field.user_coordinates[0]][col] = RAY_SYMBOL

    # RIGHT
    for col in RIGHT_COLS:
        if field.field[field.user_coordinates[0]][col] == WALL_SYMBOL:
            break
        field.field[field.user_coordinates[0]][col] = RAY_SYMBOL
