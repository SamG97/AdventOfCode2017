def get_input():
    data = []
    with open("data/day4.txt") as f:
        for line in f:
            data.append(line.strip("\n").split(" "))

    return data


def check_passphrase_list(passphrases):
    valid = 0
    for passphrase in passphrases:
        valid += check_valid_passphrase_strict(passphrase)
    return valid


def check_valid_passphrase(passphrase):
    words = []
    for word in passphrase:
        if word in words:
            return 0
        words.append(word)
    return 1


def check_valid_passphrase_strict(passphrase):
    words = []
    for word in passphrase:
        letters = {}
        for char in word:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        for other_letters in words:
            if len(letters.keys()) == len(other_letters.keys()):
                anagram = True
                for char in letters.keys():
                    if char in other_letters:
                        if letters[char] != other_letters[char]:
                            anagram = False
                            break
                    else:
                        anagram = False
                        break
                if anagram:
                    return 0
        words.append(letters)
    return 1


if __name__ == "__main__":
    values = get_input()
    print(check_passphrase_list(values))
