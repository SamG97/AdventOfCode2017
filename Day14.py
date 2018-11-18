import queue
from Day10 import hash_string


def find_filled_blocks(hash_key):
    total_blocks = 0
    for i in range(128):
        hashed = hash_string(hash_key + "-" + str(i))
        total_blocks += parse_hash(hashed)
    return total_blocks


def parse_hash(hash_value):
    hex_string = "0x" + hash_value
    dec_value = int(hex_string, 16)
    bin_string = "{0:b}".format(dec_value)
    filled_spaces = 0
    for char in bin_string:
        if char == "1":
            filled_spaces += 1
    return filled_spaces


def find_blocks(hash_key):
    grid = [parse_hash2(hash_string(hash_key + "-" + str(i))) for i in range(128)]
    number_of_blocks = 0
    while True:
        row_index = -1
        col_index = -1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    row_index = i
                    col_index = j
                    break
            if row_index != -1:
                break
        if row_index == -1:
            return number_of_blocks

        number_of_blocks += 1
        remove_block(grid, row_index, col_index)


def parse_hash2(hash_value):
    hex_string = "0x" + hash_value
    dec_value = int(hex_string, 16)
    bin_string = "{0:b}".format(dec_value).zfill(128)

    bin_array = [int(char) for char in bin_string]
    return bin_array


def remove_block(grid, row, col):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_remove = queue.Queue()
    grid[row][col] = 0
    to_remove.put((row, col))
    while not to_remove.empty():
        location = to_remove.get()
        row_index = location[0]
        col_index = location[1]
        for (i, j) in deltas:
            if row_index + i not in range(len(grid)) or col_index + j not in range(len(grid[0])):
                continue
            if grid[row_index + i][col_index + j] == 1:
                grid[row_index + i][col_index + j] = 0
                to_remove.put((row_index + i, col_index + j))


if __name__ == "__main__":
    key = "wenycdww"
    print(find_blocks(key))
