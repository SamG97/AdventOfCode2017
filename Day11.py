def get_input():
    with open("data/day11.txt") as f:
        data = [move for move in f.readline().strip("\n").split(",")]
    return data


def find_distance(moves):
    steps_north = 0
    steps_east = 0
    move_interpretations = {"n": [2, 0], "ne": [1, 1], "se": [-1, 1], "s": [-2, 0], "sw": [-1, -1], "nw": [1, -1]}
    for move in moves:
        step = move_interpretations[move]
        steps_north += step[0]
        steps_east += step[1]

    return distance_from_point(steps_north, steps_east)


def distance_from_point(north, east):
    shortest_steps_vertical = 0
    shortest_steps_horizontal = 0
    while shortest_steps_horizontal < abs(east):
        shortest_steps_horizontal += 1
        if shortest_steps_vertical < abs(north):
            shortest_steps_vertical += 1
        else:
            shortest_steps_vertical -= 1

    assert (abs(north) - shortest_steps_vertical) % 2 == 0

    return shortest_steps_horizontal + (abs(north) - shortest_steps_vertical) // 2


def find_max_distance(moves):
    steps_north = 0
    steps_east = 0
    move_interpretations = {"n": [2, 0], "ne": [1, 1], "se": [-1, 1], "s": [-2, 0], "sw": [-1, -1], "nw": [1, -1]}
    maximum_distance = 0
    for move in moves:
        step = move_interpretations[move]
        steps_north += step[0]
        steps_east += step[1]
        current_distance = distance_from_point(steps_north, steps_east)
        if current_distance > maximum_distance:
            maximum_distance = current_distance

    return maximum_distance


if __name__ == "__main__":
    movements = get_input()
    print(find_max_distance(movements))
