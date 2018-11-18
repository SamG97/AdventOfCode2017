def get_input():
    data = {}
    with open("data/day7.txt") as f:
        for line in f:
            parts = line.strip("\n").split(" ")
            name = parts[0]
            weight = int(parts[1].strip("(").strip(")"))
            children = [parts[i].strip(",") for i in range(3, len(parts))]
            data[name] = {"weight": weight, "children": children}
    return data


def find_bottom(tower):
    order = order_nodes(tower)
    return order[0]


def balance_weights(tower):
    weights = {}
    order = order_nodes(tower)
    order.reverse()
    for node in order:
        if len(tower[node]["children"]) == 0:
            weights[node] = tower[node]["weight"]
        else:
            child_weights = [weights[child] for child in tower[node]["children"]]
            if child_weights[0] * len(child_weights) != sum(child_weights):
                first_value = child_weights[0]
                different_value = -1
                different_index = 0
                index = 0
                for child in child_weights:
                    if child != first_value:
                        if different_value == -1:
                            different_value = child
                            different_index = index
                        else:
                            difference = different_value - first_value
                            wrong_child_weight = tower[tower[node]["children"][0]]["weight"]
                            return wrong_child_weight + difference
                    index += 1
                difference = different_value - first_value
                wrong_child_weight = tower[tower[node]["children"][different_index]]["weight"]
                return wrong_child_weight - difference

            weights[node] = sum(child_weights) + tower[node]["weight"]


def order_nodes(tower):
    order = []
    finished = []
    evaluating = []
    unknown = [entry for entry in tower.keys()]
    while len(unknown) > 0:
        node = unknown[0]
        visit(node, order, finished, evaluating, unknown, tower)
    order.reverse()
    return order


def visit(node, order, finished, evaluating, unknown, tower):
    if node in finished:
        return
    if node in evaluating:
        print("Error")
        return

    unknown.remove(node)
    evaluating.append(node)
    for child in tower[node]["children"]:
        visit(child, order, finished, evaluating, unknown, tower)
    evaluating.remove(node)
    finished.append(node)
    order.append(node)


if __name__ == "__main__":
    tower_description = get_input()
    print(balance_weights(tower_description))
