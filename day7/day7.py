from collections import Counter
import math

PUZZLE_INPUT = "puzzle_input.txt"


def part1(crab_positions):
    min_position = min(crab_positions)
    max_position = max(crab_positions)
    position_counts = Counter(crab_positions)

    least_fuel = math.inf
    for x in range(min_position, max_position+1):
        fuel = sum((abs(pos - x) * count) for (pos, count) in position_counts.items())
        if fuel < least_fuel:
            least_fuel = fuel
    return least_fuel


def part2(crab_positions):
    min_position = min(crab_positions)
    max_position = max(crab_positions)
    position_counts = Counter(crab_positions)

    least_fuel = math.inf
    for x in range(min_position, max_position+1):
        fuel = sum(
            sum(range(1, abs(pos-x)+1)) * count
            for (pos, count) in position_counts.items()
        )
        if fuel < least_fuel:
            least_fuel = fuel
    return least_fuel


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        initial_state = list(map(int, f.readline().split(",")))

    print(part1(initial_state))
    print(part2(initial_state))
