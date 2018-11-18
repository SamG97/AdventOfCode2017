def get_input():
    with open("data/day19.txt") as f:
        data = [[char for char in line.strip("\n").ljust(200)] for line in f]
    return data


def find_path(directions):
    column_size = len(directions[0])
    row_size = len(directions)
    column = directions[0].index("|")
    row = 0
    direction = [1, 0]
    path = ""
    while True:
        if not (0 <= column < column_size or 0 <= row < row_size) or directions[row][column] == " ":
            return path
        symbol = directions[row][column]
        if symbol not in ["|", "-", "+"]:
            path += symbol
        if symbol == "+":
            if direction[0] == 0:
                if row > 0 and directions[row - 1][column] == "|":
                    direction = [-1, 0]
                elif row < row_size - 1 and directions[row + 1][column] == "|":
                    direction = [1, 0]
                else:
                    print("I'm confused")
                    print([row, column])
                    break
            else:
                if column > 0 and directions[row][column - 1] == "-":
                    direction = [0, -1]
                elif column < column_size - 1 and directions[row][column + 1] == "-":
                    direction = [0, 1]
                else:
                    print("I'm confused")
                    print([row, column])
                    break
        row += direction[0]
        column += direction[1]


def find_steps(directions):
    column_size = len(directions[0])
    row_size = len(directions)
    column = directions[0].index("|")
    row = 0
    direction = [1, 0]
    steps = 0
    while True:
        if not (0 <= column < column_size or 0 <= row < row_size) or directions[row][column] == " ":
            return steps
        steps += 1
        if directions[row][column] == "+":
            if direction[0] == 0:
                if row > 0 and directions[row - 1][column] == "|":
                    direction = [-1, 0]
                elif row < row_size - 1 and directions[row + 1][column] == "|":
                    direction = [1, 0]
                else:
                    print("I'm confused")
                    print([row, column])
                    break
            else:
                if column > 0 and directions[row][column - 1] == "-":
                    direction = [0, -1]
                elif column < column_size - 1 and directions[row][column + 1] == "-":
                    direction = [0, 1]
                else:
                    print("I'm confused")
                    print([row, column])
                    break
        row += direction[0]
        column += direction[1]


if __name__ == "__main__":
    map_input = get_input()
    print(find_steps(map_input))