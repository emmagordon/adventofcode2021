from collections import Counter

PUZZLE_INPUT = "puzzle_input.txt"
DAYS = 256


def part1(lanternfish):
    internal_timers = Counter(lanternfish)
    for _ in range(DAYS):
        new_state = Counter()
        for timer, num_fish in internal_timers.items():
            if timer == 0:
                new_state.update({6: num_fish})
                new_state.update({8: num_fish})
            else:
                new_state.update({timer-1: num_fish})
        internal_timers = new_state

    total_fish = sum(internal_timers.values())
    return total_fish


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        initial_state = map(int, f.readline().split(","))

    print(part1(initial_state))
