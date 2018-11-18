def get_components():
    with open("data/day24.txt") as f:
        data = [[int(port) for port in component.strip("\n").split("/")] for component in f]
    return data


def find_strongest_bridge(current_bridge, remaining_pieces, current_port, highest_strength):
    best_bridge = current_bridge
    for piece in remaining_pieces:
        if current_port in piece:
            potential_bridge = current_bridge[:]
            potential_bridge.append(piece)
            other_port = piece[1] if current_port == piece[0] else piece[0]
            potential_remaining_pieces = remaining_pieces[:]
            potential_remaining_pieces.remove(piece)
            finished_potential_bridge = find_strongest_bridge(potential_bridge, potential_remaining_pieces, other_port,
                                                              highest_strength)
            score = score_bridge(finished_potential_bridge)
            if score > highest_strength:
                best_bridge = finished_potential_bridge
                highest_strength = score
    return best_bridge


def score_bridge(bridge):
    score = 0
    for piece in bridge:
        score += piece[0]
        score += piece[1]
    return score


def find_longest_bridge(current_bridge, remaining_pieces, current_port, highest_strength, highest_length):
    best_bridge = current_bridge
    for piece in remaining_pieces:
        if current_port in piece:
            potential_bridge = current_bridge[:]
            potential_bridge.append(piece)
            other_port = piece[1] if current_port == piece[0] else piece[0]
            potential_remaining_pieces = remaining_pieces[:]
            potential_remaining_pieces.remove(piece)
            finished_potential_bridge = find_longest_bridge(potential_bridge, potential_remaining_pieces, other_port,
                                                            highest_strength, highest_length)
            score = score_bridge(finished_potential_bridge)
            if len(finished_potential_bridge) > highest_length:
                best_bridge = finished_potential_bridge
                highest_strength = score
                highest_length = len(finished_potential_bridge)
            elif len(finished_potential_bridge) == highest_length and score > highest_strength:
                best_bridge = finished_potential_bridge
                highest_strength = score
    return best_bridge


if __name__ == "__main__":
    components = get_components()
    strongest_bridge = find_longest_bridge([], components, 0, 0, 0)
    print(score_bridge(strongest_bridge))
