PUZZLE_INPUT = "puzzle_input.txt"
CORRECT_NUMBERS = {
    "cf": "1",
    "acf": "7",
    "bcdf": "4",
    "acdeg": "2",
    "acdfg": "3",
    "abdfg": "5",
    "abcefg": "0",
    "abdefg": "6",
    "abcdfg": "9",
    "abcdefg": "8",
}


def part1(notes):
    count = 0
    unique_num_segments = [2, 3, 4, 7]  # 1, 4, 7, 8
    for line in notes:
        segments, outputs = line.split(" | ")
        count += sum(1 for out in outputs.split(" ") if len(out) in unique_num_segments)
    return count


def part2(notes):
    total = 0
    for line in notes:
        segments, outputs = line.split(" | ")
        lookup = find_mapping(segments.split(" "))
        total += int("".join(CORRECT_NUMBERS["".join(sorted(lookup[c] for c in code))] for code in outputs.split(" ")))
    return total


def find_mapping(codes):
    cf = [c for c in codes if len(c) == 2][0]
    acf = [c for c in codes if len(c) == 3][0]
    bcdf = [c for c in codes if len(c) == 4][0]
    abcdefg = [c for c in codes if len(c) == 7][0]

    a = [char for char in acf if char not in cf][0]
    eg = "".join(char for char in abcdefg if char not in a+bcdf)
    bd = "".join(char for char in bcdf if char not in cf)

    mapping = {a: "a"}
    for code in [c for c in codes if len(c) == 6]:
        missing_char = [c for c in abcdefg if c not in code][0]
        if missing_char in bd:
            d = missing_char
            b = [char for char in bd if char != d][0]
            mapping.update({b: "b", d: "d"})
        elif missing_char in cf:
            c = missing_char
            f = [char for char in cf if char != c][0]
            mapping.update({c: "c", f: "f"})
        elif missing_char in eg:
            e = missing_char
            g = [char for char in eg if char != e][0]
            mapping.update({e: "e", g: "g"})
        else:
            raise RuntimeError("ooops...!")
    return mapping


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]

    # print(part1(lines))
    print(part2(lines))
