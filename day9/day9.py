from functools import reduce

PUZZLE_INPUT = "puzzle_input.txt"


def part1(heights):
    risk_level = 0
    for i, row in enumerate(heights):
        for j, num in enumerate(row):
            if all(heights[x][y] > num for (x, y) in get_neighbours(heights, i, j)):
                risk_level += num+1
    return risk_level


def part2(heights):
    basin_sizes = []
    visited = [[value == 9 for value in row] for row in heights]
    while not all(is_marked for row in visited for is_marked in row):
        positions_in_basin = []
        for i, row in enumerate(visited):
            for j, already_visited in enumerate(row):
                if not already_visited:
                    positions_in_basin = get_basin_positions(visited, i, j)
                    break
            if positions_in_basin:
                break
        for (i, j) in positions_in_basin:
            visited[i][j] = True
        basin_sizes.append(len(positions_in_basin))

    largest_3_basins = sorted(basin_sizes, reverse=True)[:3]
    product = reduce(lambda x, acc: x*acc, largest_3_basins, 1)
    return product


def get_basin_positions(visited, i, j, basin_positions=None):
    if basin_positions is None:
        basin_positions = set()

    if (i, j) in basin_positions:
        return basin_positions
    else:
        basin_positions.add((i, j))

    for (x, y) in get_neighbours(visited, i, j):
        if not visited[x][y]:
            basin_positions.update(get_basin_positions(visited, x, y, basin_positions))

    return basin_positions


def get_neighbours(two_d_array, i, j):
    ns = []
    if i != 0:
        ns.append((i-1, j))
    if i != (len(two_d_array) - 1):
        ns.append((i+1, j))
    if j != 0:
        ns.append((i, j-1))
    if j != (len(two_d_array[0]) - 1):
        ns.append((i, j+1))
    return ns


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = [[int(c) for c in line.rstrip()] for line in f.readlines()]

    print(part1(puzzle_input))
    print(part2(puzzle_input))
