def get_input():
    with open("data/day5.txt") as f:
        data = [int(line.strip("\n")) for line in f]
    return data


def find_number_of_cycles(jumps):
    last_instruction_index = len(jumps) - 1
    cycles = 0
    index = 0
    while 0 <= index <= last_instruction_index:
        cycles += 1
        next_jump = jumps[index]
        jumps[index] += 1
        index += next_jump
    return cycles


def find_number_of_cycles2(jumps):
    last_instruction_index = len(jumps) - 1
    cycles = 0
    index = 0
    while 0 <= index <= last_instruction_index:
        cycles += 1
        next_jump = jumps[index]
        if next_jump >= 3:
            jumps[index] -= 1
        else:
            jumps[index] += 1
        index += next_jump
    return cycles


if __name__ == "__main__":
    instructions = get_input()
    print(find_number_of_cycles2(instructions))
