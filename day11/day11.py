import itertools

PUZZLE_INPUT = "puzzle_input.txt"


def part1(grid):
    flashes = 0
    for _ in range(100):
        # increase everything by 1
        for (i, row) in enumerate(grid):
            for (j, _) in enumerate(row):
                grid[i][j] += 1

        # for anything > 9, increase all neighbours (incl. diagonals) by 1 + chain reactions
        def _flash_if_applicable(x, y, flashes_this_round):
            if grid[x][y] > 9 and ((x, y) not in flashes_this_round):
                flashes_this_round.add((x, y))
                ns = get_neighbours(grid, x, y)
                for (X, Y) in ns:
                    grid[X][Y] += 1
                    _flash_if_applicable(X, Y, flashes_this_round)

        fs_this_round = set()
        for (i, row) in enumerate(grid):
            for (j, _) in enumerate(row):
                _flash_if_applicable(i, j, fs_this_round)

        # for anything > 9, set to 0 and increase flashes by 1
        for (i, row) in enumerate(grid):
            for (j, value) in enumerate(row):
                if value > 9:
                    flashes += 1
                    grid[i][j] = 0

    return flashes


def part2(grid):
    step_num = 0
    while True:
        step_num += 1

        # increase everything by 1
        for (i, row) in enumerate(grid):
            for (j, _) in enumerate(row):
                grid[i][j] += 1

        # for anything > 9, increase all neighbours (incl. diagonals) by 1 + chain reactions
        def _flash_if_applicable(x, y, flashes_this_round):
            if grid[x][y] > 9 and ((x, y) not in flashes_this_round):
                flashes_this_round.add((x, y))
                ns = get_neighbours(grid, x, y)
                for (X, Y) in ns:
                    grid[X][Y] += 1
                    _flash_if_applicable(X, Y, flashes_this_round)

        fs_this_round = set()
        for (i, row) in enumerate(grid):
            for (j, _) in enumerate(row):
                _flash_if_applicable(i, j, fs_this_round)

        if len(fs_this_round) == (len(grid) * len(grid[0])):
            return step_num

        # for anything > 9, set to 0
        for (i, row) in enumerate(grid):
            for (j, value) in enumerate(row):
                if value > 9:
                    grid[i][j] = 0


def get_neighbours(grid, i, j):
    ns = [(i+x, j+y) for (x, y) in itertools.product([-1, 0, +1], [-1, 0, +1]) if not x == y == 0]
    ns_inside_grid = [(x, y) for (x, y) in ns if (0 <= x < len(grid)) and (0 <= y < len(grid[0]))]
    return ns_inside_grid


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = [list(map(int, line.rstrip())) for line in f.readlines()]

    # print(part1(puzzle_input))
    print(part2(puzzle_input))
