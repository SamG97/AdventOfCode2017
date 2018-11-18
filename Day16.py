def get_instructions():
    with open("data/day16.txt") as f:
        data = [instruction for instruction in f.readline().strip("\n").split(",")]
    return data


def execute_instructions(instructions, starting_order):
    programs = starting_order
    for line in instructions:
        if line[0] == "s":
            programs = rotate(programs, int(line[1:]))
        elif line[0] == "x":
            positions = line[1:].split("/")
            a = int(positions[0])
            b = int(positions[1])
            programs[a], programs[b] = programs[b], programs[a]
        elif line[0] == "p":
            positions = line[1:].split("/")
            a = programs.index(positions[0])
            b = programs.index(positions[1])
            programs[a], programs[b] = programs[b], programs[a]
    return programs


def rotate(l, n):
    return l[-n:] + l[:-n]


def find_order_after_one(instructions):
    programs = [chr(i) for i in range(97, 113)]
    programs = execute_instructions(instructions, programs)
    final_string = ""
    for program in programs:
        final_string += program
    return final_string


def find_order_after_billion(instructions):
    programs = [chr(i) for i in range(97, 113)]
    known_programs = []
    for i in range(1000000000):
        if make_string(programs) in known_programs:
            loop_start = known_programs.index(make_string(programs))
            return known_programs[(1000000000 % (i - loop_start)) + loop_start]
        else:
            known_programs.append(make_string(programs))
            programs = execute_instructions(instructions, programs)
    return make_string(programs)


def make_string(programs):
    final_string = ""
    for program in programs:
        final_string += program
    return final_string


if __name__ == "__main__":
    commands = get_instructions()
    print(find_order_after_billion(commands))
