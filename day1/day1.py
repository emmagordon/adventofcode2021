PUZZLE_INPUT = "puzzle_input.txt"


def part1(depths):
    prev = None
    count = 0
    for value in depths:
        if prev and (value > prev):
            count += 1
        prev = value
    return count


def part2(depths):
    windows = [sum(depths[i: i+3]) for i in range(len(depths)-2)]
    return part1(windows)


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = [int(v) for v in f.readlines()]

    print(part1(puzzle_input))
    print(part2(puzzle_input))
