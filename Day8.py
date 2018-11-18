def make_allocations():
    memory = {}
    with open("data/day8.txt") as f:
        for line in f:
            parts = line.strip("\n").split(" ")
            updating_register = parts[0]
            condition_register = parts[4]
            condition_operator = parts[5]
            condition_check = int(parts[6])
            if updating_register not in memory:
                memory[updating_register] = 0
            if condition_register not in memory:
                memory[condition_register] = 0
            if condition_operator == ">":
                condition_passed = memory[condition_register] > condition_check
            elif condition_operator == "<":
                condition_passed = memory[condition_register] < condition_check
            elif condition_operator == "==":
                condition_passed = memory[condition_register] == condition_check
            elif condition_operator == "!=":
                condition_passed = memory[condition_register] != condition_check
            elif condition_operator == "<=":
                condition_passed = memory[condition_register] <= condition_check
            elif condition_operator == ">=":
                condition_passed = memory[condition_register] >= condition_check
            else:
                print("Unknown operator encountered: " + condition_operator)
                raise LookupError

            if condition_passed:
                updating_value = int(parts[2])
                updating_operator = parts[1]
                if updating_operator == "inc":
                    memory[updating_register] += updating_value
                else:
                    memory[updating_register] -= updating_value
    return memory


def find_max_memory(memory):
    return max(memory.values())


def max_memory_during_allocations():
    memory = {}
    max_value = 0
    with open("data/day8.txt") as f:
        for line in f:
            parts = line.strip("\n").split(" ")
            updating_register = parts[0]
            condition_register = parts[4]
            condition_operator = parts[5]
            condition_check = int(parts[6])
            if updating_register not in memory:
                memory[updating_register] = 0
            if condition_register not in memory:
                memory[condition_register] = 0
            if condition_operator == ">":
                condition_passed = memory[condition_register] > condition_check
            elif condition_operator == "<":
                condition_passed = memory[condition_register] < condition_check
            elif condition_operator == "==":
                condition_passed = memory[condition_register] == condition_check
            elif condition_operator == "!=":
                condition_passed = memory[condition_register] != condition_check
            elif condition_operator == "<=":
                condition_passed = memory[condition_register] <= condition_check
            elif condition_operator == ">=":
                condition_passed = memory[condition_register] >= condition_check
            else:
                print("Unknown operator encountered: " + condition_operator)
                raise LookupError

            if condition_passed:
                updating_value = int(parts[2])
                updating_operator = parts[1]
                if updating_operator == "inc":
                    memory[updating_register] += updating_value
                else:
                    memory[updating_register] -= updating_value

                if memory[updating_register] > max_value:
                    max_value = memory[updating_register]
    return max_value


if __name__ == "__main__":
    mem = make_allocations()
    print(find_max_memory(mem))
    print(max_memory_during_allocations())
