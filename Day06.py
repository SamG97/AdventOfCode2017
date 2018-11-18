def redistribute(memory):
    cycles_possible = 0
    states_seen = [memory[:]]
    n = len(memory)
    while True:
        cycles_possible += 1
        max_blocks = max(memory)
        max_index = memory.index(max_blocks)
        memory[max_index] = 0
        index = max_index
        for _ in range(max_blocks):
            index = (index + 1) % n
            memory[index] += 1

        for previous_state in states_seen:
            if previous_state == memory:
                return cycles_possible

        states_seen.append(memory[:])


def number_of_cycles_in_loop(memory):
    cycles_possible = 0
    states_seen = [memory[:]]
    n = len(memory)
    while True:
        cycles_possible += 1
        max_blocks = max(memory)
        max_index = memory.index(max_blocks)
        memory[max_index] = 0
        index = max_index
        for _ in range(max_blocks):
            index = (index + 1) % n
            memory[index] += 1

        loop_offset = 0
        for previous_state in states_seen:
            if previous_state == memory:
                return cycles_possible - loop_offset
            loop_offset += 1

        states_seen.append(memory[:])


if __name__ == "__main__":
    mem = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
    print(number_of_cycles_in_loop(mem))
