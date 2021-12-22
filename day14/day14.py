from collections import Counter
import functools

PUZZLE_INPUT = "puzzle_input.txt"


# Brute force
def part1(polymer):
    for _ in range(10):
        pairs = [polymer[i:i+2] for i in range(len(polymer)-1)]
        polymer = "".join([p[0]+_insertion_rules[p] for p in pairs]) + pairs[-1][1]

    char_counts = Counter(polymer)
    return max(v for v in char_counts.values()) - min(v for v in char_counts.values())


# With caching
def part2(polymer):
    @functools.lru_cache(maxsize=None)
    def count(pair, steps):
        if steps < 0:
            raise RuntimeError
        if steps == 0 or (pair not in _insertion_rules):
            return Counter()

        new_element = _insertion_rules[pair]
        counter = Counter(new_element)
        counter.update(count(pair[0] + new_element, steps - 1))
        counter.update(count(new_element + pair[1], steps - 1))
        return counter

    char_counts = Counter(polymer)
    pairs = [polymer[i:i + 2] for i in range(len(polymer) - 1)]
    for p in pairs:
        char_counts.update(count(p, steps=40))
    return max(v for v in char_counts.values()) - min(v for v in char_counts.values())


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        _starting_polymer = f .readline().rstrip()
        f.readline()
        _insertion_rules = {pair: insert for pair, insert in [line.rstrip().split(" -> ") for line in f.readlines()]}

    print(part1(_starting_polymer))
    print(part2(_starting_polymer))
