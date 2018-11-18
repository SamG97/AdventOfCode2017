import queue


def score_generators(starting_a, starting_b):
    a = starting_a
    b = starting_b
    total_score = 0
    mask = (1 << 16) - 1
    for _ in range(40000000):
        a = generate_next_value(a, 16807)
        b = generate_next_value(b, 48271)
        if (a & mask) == (b & mask):
            total_score += 1
    return total_score


def generate_next_value(current_value, factor):
    return (current_value * factor) % 2147483647


def score_picky_generators(starting_a, starting_b):
    a = starting_a
    b = starting_b
    total_score = 0
    mask = (1 << 16) - 1
    a_queue = queue.Queue()
    b_queue = queue.Queue()
    pairs_generated = 0
    while pairs_generated < 5000000:
        a = generate_next_value(a, 16807)
        b = generate_next_value(b, 48271)
        if a & 0b11 == 0:
            a_queue.put(a)
        if b & 0b111 == 0:
            b_queue.put(b)
        while not (a_queue.empty() or b_queue.empty()):
            pairs_generated += 1
            testing_a = a_queue.get()
            testing_b = b_queue.get()
            if (testing_a & mask) == (testing_b & mask):
                total_score += 1
    return total_score


def test(starting_a, starting_b):
    a = starting_a
    b = starting_b
    total_score = 0
    mask = (1 << 16) - 1
    for _ in range(5000000):
        a = generate_next_value(a, 16807)
        while a & 0b11 > 0:
            a = generate_next_value(a, 16807)
        b = generate_next_value(b, 48271)
        while b & 0b111 > 0:
            b = generate_next_value(b, 48271)
        if (a & mask) == (b & mask):
            total_score += 1
    return total_score


if __name__ == "__main__":
    print(test(873, 583))
