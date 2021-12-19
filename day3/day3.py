from collections import Counter
import operator

PUZZLE_INPUT = "puzzle_input.txt"


def part1(diagnostics):
    num_bits = len(diagnostics[0])
    epsilon = ""
    gamma = ""
    for bit in range(num_bits):
        counts = Counter(d[bit] for d in diagnostics)
        if counts["1"] > counts["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def part2(diagnostics):
    oxygen = finder(diagnostics, operator.ge)
    co2 = finder(diagnostics, operator.lt)
    return oxygen * co2


def finder(diagnostics, op, i=0):
    if len(diagnostics) == 1:
        return int(diagnostics[0], 2)

    counts = Counter(d[i] for d in diagnostics)
    if op(counts["1"], counts["0"]):
        return finder([d for d in diagnostics if d[i] == "1"], op, i+1)
    else:
        return finder([d for d in diagnostics if d[i] == "0"], op, i+1)


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = [l.rstrip() for l in f.readlines()]

    print(part1(puzzle_input))
    print(part2(puzzle_input))
