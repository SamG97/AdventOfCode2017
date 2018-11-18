def number_of_steps(x):
    if x == 1:
        return 0

    ring = 0
    i = 1
    while x > i**2:
        i += 2
        ring += 1

    max_in_ring = (ring * 2 + 1)**2
    min_in_ring = (ring * 2 - 1)**2 + 1
    range_of_ring = max_in_ring - min_in_ring
    min_in_side = min_in_ring + int((x - min_in_ring) * 4 / range_of_ring) * 2 * ring
    side_midpoint = min_in_side + ring - 1
    return abs(side_midpoint - x) + ring


def value(n):
    memory = [[0 for _ in range(1000)] for _ in range(1000)]
    memory[500][500] = 1
    x = 501
    y = 500
    direction = 1
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    while 0 < x < 999 and 0 < y < 999:
        cell_sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                cell_sum += memory[y + i][x + j]
        memory[y][x] = cell_sum
        if cell_sum > n:
            return cell_sum
        if memory[y + dy[(direction + 1) % 4]][x + dx[(direction + 1) % 4]] == 0:
            direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]


if __name__ == "__main__":
    print(value(325489))
