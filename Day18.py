from collections import deque


def get_instructions():
    with open("data/day18.txt") as f:
        data = [line.strip("\n") for line in f]
    return data


def execute_instructions(instructions):
    index = 0
    last_sound = None
    end = len(instructions)
    memory = {}
    while True:
        if not 0 <= index < end:
            return None
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
        if opcode == "jgz":
            if operands_values[0] > 0:
                index += operands_values[1]
            else:
                index += 1
        else:
            if opcode == "snd":
                last_sound = operands_values[0]
            elif opcode == "set":
                memory[operands[0]] = operands_values[1]
            elif opcode == "add":
                memory[operands[0]] = memory[operands[0]] + operands_values[1]
            elif opcode == "mul":
                memory[operands[0]] = memory[operands[0]] * operands_values[1]
            elif opcode == "mod":
                memory[operands[0]] = memory[operands[0]] % operands_values[1]
            elif opcode == "rcv":
                if operands_values[0] != 0:
                    return last_sound
            else:
                print("Unknown command " + opcode + " found")
                raise LookupError
            index += 1


def concurrent_execution(instructions):
    index = [0, 0]
    memory = [{"p": 0}, {"p": 1}]
    end = len(instructions)
    message_queue = [deque(), deque()]
    sent_messages = 0
    while True:
        for turn in [0, 1]:
            while True:
                if not 0 <= index[turn] < end:
                    break
                current_instruction = instructions[index[turn]]
                parts = current_instruction.split(" ")
                opcode = parts[0]
                operands = parts[1:]
                operands_values = []
                for operand in operands:
                    if operand.isnumeric() or (len(operand) > 0 and operand[1:].isnumeric()):
                        operands_values.append(int(operand))
                    else:
                        if operand not in memory[turn]:
                            memory[turn][operand] = 0
                        operands_values.append(memory[turn][operand])
                if opcode == "jgz":
                    if operands_values[0] > 0:
                        index[turn] += operands_values[1]
                    else:
                        index[turn] += 1
                else:
                    if opcode == "snd":
                        message_queue[(turn + 1) % 2].append(operands_values[0])
                        if turn == 1:
                            sent_messages += 1
                    elif opcode == "set":
                        memory[turn][operands[0]] = operands_values[1]
                    elif opcode == "add":
                        memory[turn][operands[0]] = memory[turn][operands[0]] + operands_values[1]
                    elif opcode == "mul":
                        memory[turn][operands[0]] = memory[turn][operands[0]] * operands_values[1]
                    elif opcode == "mod":
                        memory[turn][operands[0]] = memory[turn][operands[0]] % operands_values[1]
                    elif opcode == "rcv":
                        if len(message_queue[turn]) > 0:
                            memory[turn][operands[0]] = message_queue[turn].popleft()
                        else:
                            break
                    else:
                        print("Unknown command " + opcode + " found")
                        raise LookupError
                    index[turn] += 1
        if (len(message_queue[0]) == 0 and len(message_queue[1]) == 0) or not (
                    0 <= index[0] < end or 0 <= index[1] < end):
            return sent_messages


if __name__ == "__main__":
    instructions_list = get_instructions()
    print(concurrent_execution(instructions_list))
