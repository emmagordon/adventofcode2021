import re

PUZZLE_INPUT = "puzzle_input.txt"


def part1(dots, folds):
    first_fold = folds[0]
    visible_dots_after_fold = do_fold(dots, first_fold)
    return len(visible_dots_after_fold)


def part2(dots, folds):
    for fold in folds:
        dots = do_fold(dots, fold)

    output = ""
    max_x = max(x for x, y in dots)
    max_y = max(y for x, y in dots)
    for j in range(max_y+1):
        for i in range(max_x+1):
            output += "#" if (i, j) in dots else "."
        output += "\n"

    return output


def do_fold(dots, fold):
    fold_axis = fold[0]
    fold_pos = fold[1]

    visible_dots_after_fold = set()
    if fold_axis == "y":
        for dot in dots:
            if dot[1] < fold_pos:
                visible_dots_after_fold.add(dot)
            else:
                visible_dots_after_fold.add((dot[0], 2*fold_pos-dot[1]))
    else:
        for dot in dots:
            if dot[0] < fold_pos:
                visible_dots_after_fold.add(dot)
            else:
                visible_dots_after_fold.add((2*fold_pos-dot[0], dot[1]))

    return visible_dots_after_fold


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]

    _dots = set()
    _folds = []
    for line in lines:
        if line == "":
            continue
        elif line.startswith("fold"):
            axis, n = re.match(r"fold along ([xy])=(\d+)", line).groups()
            _folds.append((axis, int(n)))
        else:
            _dots.add(tuple(map(int, line.split(","))))

    print(part1(_dots, _folds))
    print(part2(_dots, _folds))
