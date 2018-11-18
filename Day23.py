import math


def get_instructions():
    with open("data/day23.txt") as f:
        data = [line.strip("\n") for line in f]
    return data


def execute_instructions(instructions):
    index = 0
    multiplications = 0
    end = len(instructions)
    memory = {}
    while True:
        if not 0 <= index < end:
            return multiplications
        current_instruction = instructions[index]
        parts = current_instruction.split(" ")
        opcode = parts[0]
        operands = parts[1:]
        operands_values = []
        for operand in operands:
            if operand.isnumeric() or (len(operand) > 0 and operand[1:].isnumeric()):
                operands_values.append(int(operand))
            else:
                if operand not in memory:
                    memory[operand] = 0
                operands_values.append(memory[operand])
        if opcode == "jnz":
            if operands_values[0] != 0:
                index += operands_values[1]
            else:
                index += 1
        else:
            if opcode == "set":
                memory[operands[0]] = operands_values[1]
            elif opcode == "sub":
                memory[operands[0]] = memory[operands[0]] - operands_values[1]
            elif opcode == "mul":
                memory[operands[0]] = memory[operands[0]] * operands_values[1]
                multiplications += 1
            else:
                print("Unknown command " + opcode + " found")
                raise LookupError
            index += 1


def execute_python():
    h = 0

    b = 57 * 100 + 100000
    c = b + 17000
    while True:
        f = False
        for d in range(2, int(math.sqrt(b)) + 1):
            if b % d == 0:
                f = True
                break
        if f:
            h += 1
        if b == c:
            return h
        b += 17


if __name__ == "__main__":
    instructions_list = get_instructions()
    print(execute_python())
