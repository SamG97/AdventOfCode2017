def get_map():
    with open("data/day22.txt") as f:
        data = [[char for char in line.strip("\n")] for line in f]
    return data


def count_infection(grid):
    start = len(grid) // 2
    position = [start, start]
    direction = [-1, 0]
    infections = 0
    for _ in range(10000):
        if position[0] < 0:
            grid.insert(0, ["." for _ in range(len(grid[0]))])
            position[0] += 1
        elif position[0] >= len(grid):
            grid.append(["." for _ in range(len(grid[0]))])
        if position[1] < 0:
            for row in grid:
                row.insert(0, ".")
            position[1] += 1
        elif position[1] >= len(grid[0]):
            for row in grid:
                row.append(".")

        if grid[position[0]][position[1]] == "#":
            direction = turn_right(direction)
            grid[position[0]][position[1]] = "."
        else:
            direction = turn_left(direction)
            grid[position[0]][position[1]] = "#"
            infections += 1
        position = [position[0] + direction[0], position[1] + direction[1]]
    return infections


def turn_left(direction):
    if direction[0] == 0:
        if direction[1] == -1:
            return [1, 0]
        else:
            return [-1, 0]
    elif direction[0] == -1:
        return [0, -1]
    else:
        return [0, 1]


def turn_right(direction):
    if direction[0] == 0:
        if direction[1] == -1:
            return [-1, 0]
        else:
            return [1, 0]
    elif direction[0] == -1:
        return [0, 1]
    else:
        return [0, -1]


def count_evolved_infection(grid):
    start = len(grid) // 2
    position = [start, start]
    direction = [-1, 0]
    infections = 0
    for _ in range(10000000):
        if position[0] < 0:
            grid.insert(0, ["." for _ in range(len(grid[0]))])
            position[0] += 1
        elif position[0] >= len(grid):
            grid.append(["." for _ in range(len(grid[0]))])
        if position[1] < 0:
            for row in grid:
                row.insert(0, ".")
            position[1] += 1
        elif position[1] >= len(grid[0]):
            for row in grid:
                row.append(".")

        if grid[position[0]][position[1]] == "#":
            direction = turn_right(direction)
            grid[position[0]][position[1]] = "F"
        elif grid[position[0]][position[1]] == ".":
            direction = turn_left(direction)
            grid[position[0]][position[1]] = "W"
        elif grid[position[0]][position[1]] == "W":
            grid[position[0]][position[1]] = "#"
            infections += 1
        else:
            assert grid[position[0]][position[1]] == "F"
            direction = [-direction[0], -direction[1]]
            grid[position[0]][position[1]] = "."
        position = [position[0] + direction[0], position[1] + direction[1]]
    return infections


if __name__ == "__main__":
    grid_input = get_map()
    print(count_evolved_infection(grid_input))
