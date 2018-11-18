def turing():
    tape = [0]
    index = 0
    state = "A"
    for _ in range(12861455):
        if index == 0:
            tape.insert(0, 0)
            index += 1
        elif index == len(tape):
            tape.append(0)

        if state == "A":
            if tape[index] == 0:
                tape[index] = 1
                index += 1
                state = "B"
            else:
                tape[index] = 0
                index -= 1
                state = "B"
        elif state == "B":
            if tape[index] == 0:
                tape[index] = 1
                index -= 1
                state = "C"
            else:
                tape[index] = 0
                index += 1
                state = "E"
        elif state == "C":
            if tape[index] == 0:
                tape[index] = 1
                index += 1
                state = "E"
            else:
                tape[index] = 0
                index -= 1
                state = "D"
        elif state == "D":
            if tape[index] == 0:
                tape[index] = 1
                index -= 1
                state = "A"
            else:
                tape[index] = 1
                index -= 1
                state = "A"
        elif state == "E":
            if tape[index] == 0:
                tape[index] = 0
                index += 1
                state = "A"
            else:
                tape[index] = 0
                index += 1
                state = "F"
        elif state == "F":
            if tape[index] == 0:
                tape[index] = 1
                index += 1
                state = "E"
            else:
                tape[index] = 1
                index += 1
                state = "A"
        else:
            raise LookupError
    return sum(tape)


if __name__ == "__main__":
    print(turing())
