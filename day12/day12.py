from collections import defaultdict
PUZZLE_INPUT = "puzzle_input.txt"


def part1(route_table):
    paths_to_end = find_paths_from_start_to_end(route_table)
    return len(paths_to_end)


def find_paths_from_start_to_end(routes, path_so_far=None):
    if path_so_far is None:
        path_so_far = ["start"]

    current_position = path_so_far[-1]
    if current_position == "end":
        return [path_so_far]

    options = routes[current_position]
    paths = []
    for option in options:
        if (option not in path_so_far) or (option.isupper()):
            paths += find_paths_from_start_to_end(routes, (path_so_far[::] + [option]))
    return paths


def part2(route_table):
    paths_to_end = find_paths_from_start_to_end_v2(route_table)
    return len(paths_to_end)


def find_paths_from_start_to_end_v2(routes, path_so_far=None):
    if path_so_far is None:
        path_so_far = ["start"]

    current_position = path_so_far[-1]
    if current_position == "end":
        return [path_so_far]

    options = routes[current_position]
    paths = []
    for option in options:
        lower_case_nodes_so_far = [node for node in path_so_far if node.islower()]
        any_lower_case_node_already_visited_twice = len(set(lower_case_nodes_so_far)) != len(lower_case_nodes_so_far)
        valid_option = (
                (option not in path_so_far)
                or (option.isupper())
                or (option != "start" and not any_lower_case_node_already_visited_twice)
        )
        if valid_option:
            paths += find_paths_from_start_to_end_v2(routes, (path_so_far[::] + [option]))
    return paths


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        links = [line.rstrip().split("-") for line in f.readlines()]

    link_table = defaultdict(list)
    for (a, b) in links:
        link_table[a].append(b)
        link_table[b].append(a)

    # print(part1(link_table))
    print(part2(link_table))
