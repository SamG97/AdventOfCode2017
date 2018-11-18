import queue


def create_graph():
    adjacency_list = {}
    with open("data/day12.txt") as f:
        for line in f:
            interpret_line(line, adjacency_list)
    return adjacency_list


def interpret_line(line, adjacency):
    parts = line.strip("\n").split(" ")
    node = int(parts[0])
    connections = [int(connection.strip(",")) for connection in parts[2:]]
    adjacency[node] = connections


def find_subgraph_size(start, adjacency):
    nodes_in_graph = []
    nodes_to_explore = queue.Queue()
    nodes_to_explore.put(start)
    while not nodes_to_explore.empty():
        node = nodes_to_explore.get()
        if node in nodes_in_graph:
            continue
        nodes_in_graph.append(node)
        for connection in adjacency[node]:
            if connection not in nodes_in_graph:
                nodes_to_explore.put(connection)
    return len(nodes_in_graph)


def find_number_of_subgraphs(adjacency):
    nodes_found = []
    number_of_groups = 0
    for node in adjacency.keys():
        if node in nodes_found:
            continue
        nodes_found.extend(find_subgraph(node, adjacency))
        number_of_groups += 1
    return number_of_groups


def find_subgraph(start, adjacency):
    nodes_in_graph = []
    nodes_to_explore = queue.Queue()
    nodes_to_explore.put(start)
    while not nodes_to_explore.empty():
        node = nodes_to_explore.get()
        if node in nodes_in_graph:
            continue
        nodes_in_graph.append(node)
        for connection in adjacency[node]:
            if connection not in nodes_in_graph:
                nodes_to_explore.put(connection)
    return nodes_in_graph


if __name__ == "__main__":
    graph = create_graph()
    print(find_number_of_subgraphs(graph))
