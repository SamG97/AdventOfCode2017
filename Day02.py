import sys


def get_input():
    data = []
    with open("data/day2.txt") as f:
        for line in f:
            data.append([int(entry) for entry in line.strip("\n").split("	")])

    return data


def checksum(spreadsheet):
    total = 0
    for row in spreadsheet:
        min_entry = sys.maxsize
        max_entry = -sys.maxsize-1
        for col in row:
            if col > max_entry:
                max_entry = col
            if col < min_entry:
                min_entry = col
        total += max_entry - min_entry
    return total


def sum_of_divisors(spreadsheet):
    total = 0
    for row in spreadsheet:
        total += get_row_value(row)
    return total


def get_row_value(row):
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] % row[j] == 0:
                return row[i] // row[j]
            if row[j] % row[i] == 0:
                return row[j] // row[i]


if __name__ == "__main__":
    data = get_input()
    print(sum_of_divisors(data))