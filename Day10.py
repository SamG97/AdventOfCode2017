def knot(lengths):
    n = 256
    data = [i for i in range(n)]
    index = 0
    skip = 0
    for length in lengths:
        for offset in range(int((length + 1) / 2)):
            data[(index + offset) % n], data[(index + length - 1 - offset) % n] = \
                data[(index + length - 1 - offset) % n], data[(index + offset) % n]
        index = (index + length + skip) % n
        skip += 1
    return data


def check_hash(hashed):
    return hashed[0] * hashed[1]


def hash_string(raw_input):
    lengths = parse_input(raw_input)
    sparse_hash = full_knot(lengths)
    text_hash = create_hash_string(sparse_hash)
    return text_hash


def parse_input(raw_input):
    lengths = [ord(char) for char in raw_input.strip(" ")]
    lengths.extend([17, 31, 73, 47, 23])
    return lengths


def full_knot(lengths):
    n = 256
    data = [i for i in range(n)]
    index = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            for offset in range(int((length + 1) / 2)):
                data[(index + offset) % n], data[(index + length - 1 - offset) % n] = \
                    data[(index + length - 1 - offset) % n], data[(index + offset) % n]
            index = (index + length + skip) % n
            skip += 1
    return data


def create_hash_string(sparse):
    dense_hash = [xor_hash(sparse, i) for i in range(16)]

    hash_string = ""
    for element in dense_hash:
        hash_string += hex(element)[2:].rjust(2, "0")

    return hash_string


def xor_hash(sparse, i):
    block = sparse[(16 * i):(16 * (i + 1))]
    xor = 0
    for element in block:
        xor ^= element
    return xor


if __name__ == "__main__":
    lens = [157, 222, 1, 2, 177, 254, 0, 228, 159, 140, 249, 187, 255, 51, 76, 30]
    hashed_list = knot(lens)
    string_input = "157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30"
    text_hash = hash_string(string_input)
    print(text_hash)
