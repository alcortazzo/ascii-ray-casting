from field import Field


def calculate_rays(field: Field):
    for row in range(len(field.field)):
        for col in range(len(field.field[row])):
            if field.field[row][col] == "*":
                field.field[row][col] = " "

    # UP
    for row in [_ for _ in range(0, field.user_coordinates[0])][::-1]:
        if field.field[row][field.user_coordinates[1]] == "#":
            break
        field.field[row][field.user_coordinates[1]] = "*"

    # DOWN
    for row in [_ for _ in range(field.user_coordinates[0] + 1, len(field.field))]:
        if field.field[row][field.user_coordinates[1]] == "#":
            break
        field.field[row][field.user_coordinates[1]] = "*"

    # LEFT
    for col in [_ for _ in range(0, field.user_coordinates[1])][::-1]:
        if field.field[field.user_coordinates[0]][col] == "#":
            break
        field.field[field.user_coordinates[0]][col] = "*"

    # RIGHT
    for col in [_ for _ in range(field.user_coordinates[1] + 1, len(field.field[0]))]:
        if field.field[field.user_coordinates[0]][col] == "#":
            break
        field.field[field.user_coordinates[0]][col] = "*"
