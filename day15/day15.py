import math

PUZZLE_INPUT = "puzzle_input.txt"


def part1(grid):
    return shortest_path_v2(grid)


def part2(grid):
    def wrap(n):
        while n >= 10:
            n -= 9
        return n

    s = len(grid)
    full_map = [
        [wrap(grid[x % s][y % s] + (x-(x % s))//s + (y-(y % s))//s) for y in range(s*5)]
        for x in range(s*5)
    ]
    # with open("example_full_map.txt", "r") as f:
    #     expected_full_map = [[int(c) for c in line.rstrip()] for line in f.readlines()]
    # assert full_map == expected_full_map

    return shortest_path_v2(full_map)


# def shortest_path(grid):  # FIXME: this works, but is very slow for larger inputs - the one below is faster, but broken...
#     start = (0, 0)
#     target = (len(grid) - 1, len(grid[0]) - 1)
#
#     unvisited_nodes = {(x, y) for x in range(len(grid)) for y in range(len(grid[0]))}
#     distances = {(x, y): math.inf for (x, y) in unvisited_nodes}
#     distances[start] = 0
#
#     current_node = start
#     while target in unvisited_nodes:
#         unvisited_neighbours = [n for n in get_neighbours(current_node, grid) if n in unvisited_nodes]
#         for (x, y) in unvisited_neighbours:
#             distances[(x, y)] = min(distances[(x, y)], (distances[current_node] + grid[x][y]))
#         unvisited_nodes.remove(current_node)
#
#         distance_to_nearest_unvisited_node = math.inf
#         for node in unvisited_nodes:
#             if distances[node] < distance_to_nearest_unvisited_node:
#                 current_node = node
#                 distance_to_nearest_unvisited_node = distances[node]
#
#     return distances[target]


def shortest_path_v2(grid):  # FIXME: gives right answer for example, but 7 too high for puzzle input...
    start = (0, 0)
    target = (len(grid) - 1, len(grid[0]) - 1)

    unvisited_nodes = [(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]
    distances = {(x, y): math.inf for (x, y) in unvisited_nodes}

    distances[start] = 0
    for node in unvisited_nodes:
        for (x, y) in get_neighbours(node, grid):
            distances[(x, y)] = min(distances[(x, y)], (distances[node] + grid[x][y]))

    return distances[target]


def get_neighbours(pos, grid):  # doesn't include diagonals
    x, y = pos
    ns = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(x, y) for (x, y) in ns if 0 <= x < len(grid) and 0 <= y < len(grid[0])]


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = [[int(c) for c in line.rstrip()] for line in f.readlines()]

    print(part1(puzzle_input))
    print(part2(puzzle_input))
