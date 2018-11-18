def get_input():
    with open("data/day9.txt") as f:
        data = f.readline()
    return data


def score_stream(stream):
    total_score = 0
    next_score = 0
    index = 0
    n = len(stream)
    is_garbage = False
    while index < n:
        char = stream[index]
        if is_garbage:
            if char == "!":
                index += 1
            elif char == ">":
                is_garbage = False
        else:
            if char == "{":
                next_score += 1
                total_score += next_score
            elif char == "}":
                next_score -= 1
            elif char == "<":
                is_garbage = True
        index += 1
    return total_score


def count_garbage(stream):
    total_garbage_characters = 0
    index = 0
    n = len(stream)
    is_garbage = False
    while index < n:
        char = stream[index]
        if is_garbage:
            if char == "!":
                index += 1
            elif char == ">":
                is_garbage = False
            else:
                total_garbage_characters += 1
        else:
            if char == "<":
                is_garbage = True
        index += 1
    return total_garbage_characters


if __name__ == "__main__":
    raw_stream = get_input()
    print(count_garbage(raw_stream))
