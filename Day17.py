def spin_lock(jumps):
    memory = [0]
    current_position = 1
    for i in range(1, 2018):
        current_position = (current_position + jumps) % len(memory) + 1
        memory.insert(current_position, i)
    return memory[(current_position + 1) % len(memory)]


def long_spin_lock(jumps):
    current_position = 1
    value_at_1 = -1
    for i in range(1, 50000001):
        current_position = (current_position + jumps) % i + 1
        if current_position == 1:
            value_at_1 = i
    return value_at_1


if __name__ == "__main__":
    print(long_spin_lock(369))
