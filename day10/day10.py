PUZZLE_INPUT = "puzzle_input.txt"
OPENING_BRACES = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}


def part1(lines):
    total_score = 0
    for line in lines:
        opening_braces_stack = []
        for char in line:
            if char in ["(", "[", "{", "<"]:
                opening_braces_stack.append(char)
                continue

            try:
                opening_brace = opening_braces_stack.pop()
            except IndexError:
                opening_brace = None

            if char == ")":
                if opening_brace != "(":
                    total_score += 3
                    break
            elif char == "]":
                if opening_brace != "[":
                    total_score += 57
                    break
            elif char == "}":
                if opening_brace != "{":
                    total_score += 1197
                    break
            elif char == ">":
                if opening_brace != "<":
                    total_score += 25137
                    break
            else:
                raise RuntimeError("unexpected input string!")

    return total_score


def part2(lines):
    corresponding_closing_brace_scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in lines:
        corrupted = False
        opening_braces_stack = []
        for char in line:
            if char in ["(", "[", "{", "<"]:
                opening_braces_stack.append(char)
                continue

            try:
                opening_brace = opening_braces_stack.pop()
            except IndexError:
                opening_brace = None

            if OPENING_BRACES[char] != opening_brace:
                corrupted = True
                break

        if not corrupted:
            score = 0
            while opening_braces_stack:
                score *= 5
                opening_brace = opening_braces_stack.pop()
                score += corresponding_closing_brace_scores[opening_brace]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]  # n.b. len(scores) will always be odd


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    print(part1(puzzle_input))
    print(part2(puzzle_input))
