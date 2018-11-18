def get_rules():
    data = {}
    with open("data/day21alt.txt") as f:
        for line in f:
            line = line.strip("\n").split(" => ")
            data[line[0]] = line[1]
    return data


def find_number_of_pixels(rules, iterations):
    grid = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
    for i in range(iterations):
        size = len(grid)
        if size % 2 == 0:
            sub_grid_size = 2
        else:
            assert(size % 3 == 0)
            sub_grid_size = 3
        sub_grid_dimensions = int(size / sub_grid_size)
        new_grid = generate_empty_grid(sub_grid_dimensions * (sub_grid_size + 1))
        for row in range(sub_grid_dimensions):
            for col in range(sub_grid_dimensions):
                rows = grid[row * sub_grid_size:(row + 1) * sub_grid_size]
                pattern = [row[col * sub_grid_size:(col + 1) * sub_grid_size] for row in rows]
                if i == 4:
                    print(pattern)
                pattern_permutations = generate_pattern_permutations(pattern)
                rule = None
                for perm in pattern_permutations:
                    if perm in rules:
                        rule = rules[perm]
                        break
                if rule is None:
                    print("Could not find rule for " + str(pattern))
                    raise LookupError
                rule_rows = rule.split("/")
                rule_values = [[char for char in row2] for row2 in rule_rows]
                for rule_row in range(len(rule_rows)):
                    for rule_col in range(len(rule_rows)):
                        new_grid[row * (sub_grid_size + 1) + rule_row][col * (sub_grid_size + 1) + rule_col] \
                            = rule_values[rule_row][rule_col]
        grid = new_grid
    for row in grid: print(row)
    return count_cells(grid)


def generate_empty_grid(size):
    return [["" for _ in range(size)] for _ in range(size)]


def generate_pattern_permutations(pattern):
    perms = [pattern]
    size = len(pattern)
    rotate = {2: rotate2, 3: rotate3}
    flip = {2: flip2, 3: flip3}
    next_pattern = pattern
    for _ in range(3):
        next_pattern = rotate[size](next_pattern)
        perms.append(next_pattern)
    next_pattern = flip[size](pattern)
    perms.append(next_pattern)
    for _ in range(3):
        next_pattern = rotate[size](next_pattern)
        perms.append(next_pattern)
    encodings = []
    for perm in perms:
        encoding = ""
        for row in perm:
            for col in row:
                encoding += str(col)
            encoding += "/"
        encodings.append(encoding[:-1])
    return encodings


def rotate2(pattern):
    result = [["", ""], ["", ""]]
    result[0][0] = pattern[1][0]
    result[0][1] = pattern[0][0]
    result[1][0] = pattern[1][1]
    result[1][1] = pattern[0][1]
    return result


def flip2(pattern):
    result = [["", ""], ["", ""]]
    result[0][0] = pattern[0][1]
    result[0][1] = pattern[0][0]
    result[1][0] = pattern[1][1]
    result[1][1] = pattern[1][0]
    return result


def rotate3(pattern):
    result = [["", "", ""], ["", "", ""], ["", "", ""]]
    result[0][0] = pattern[1][0]
    result[0][1] = pattern[0][0]
    result[0][2] = pattern[0][1]
    result[1][0] = pattern[2][0]
    result[1][1] = pattern[1][1]
    result[1][2] = pattern[0][2]
    result[2][0] = pattern[2][1]
    result[2][1] = pattern[2][2]
    result[2][2] = pattern[1][2]
    return result


def flip3(pattern):
    result = [["", "", ""], ["", "", ""], ["", "", ""]]
    result[0][0] = pattern[0][2]
    result[0][1] = pattern[0][1]
    result[0][2] = pattern[0][0]
    result[1][0] = pattern[1][2]
    result[1][1] = pattern[1][1]
    result[1][2] = pattern[1][0]
    result[2][0] = pattern[2][2]
    result[2][1] = pattern[2][1]
    result[2][2] = pattern[2][0]
    return result


def count_cells(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == "#":
                count += 1
    return count


if __name__ == "__main__":
    enhancement_rules = get_rules()
    print(find_number_of_pixels(enhancement_rules, 4))
