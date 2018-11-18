def create_firewall():
    current_depth = 0
    firewall = []
    with open("data/day13.txt") as f:
        for line in f:
            parts = line.split(": ")
            depth = int(parts[0])
            scan = int(parts[1])
            while current_depth < depth:
                firewall.append({})
                current_depth += 1
            firewall.append({"current_position": 1, "limit": scan, "direction": 1})
            current_depth += 1
    return firewall


def find_severity(firewall):
    index = 0
    severity = 0
    while index < len(firewall):
        if firewall[index] != {} and firewall[index]["current_position"] == 1:
            severity += index * firewall[index]["limit"]
        move_scanners(firewall)
        index += 1
    return severity


def move_scanners(firewall):
    for row in firewall:
        if row == {}:
            continue
        row["current_position"] += row["direction"]
        if row["current_position"] == row["limit"]:
            row["direction"] = -1
        elif row["current_position"] == 1:
            row["direction"] = 1


def find_delay():
    delay = 0
    firewall = create_firewall()
    while is_caught(copy_firewall(firewall)):
        if delay % 100 == 0:
            print(delay)
        delay += 1
        move_scanners(firewall)
    return delay


def is_caught(firewall):
    index = 0
    while index < len(firewall):
        if firewall[index] != {} and firewall[index]["current_position"] == 1:
            return True
        move_scanners(firewall)
        index += 1
    return False


def copy_firewall(firewall):
    firewall_copy = []
    for row in firewall:
        if row == {}:
            new_row = {}
        else:
            new_row = {"current_position": row["current_position"], "limit": row["limit"],
                       "direction": row["direction"]}
        firewall_copy.append(new_row)
    return firewall_copy


if __name__ == "__main__":
    wall = create_firewall()
    print(find_delay())
