PUZZLE_INPUT = "puzzle_input.txt"


class Command:
    def __init__(self, cmd):
        parts = cmd.split()
        self.direction = parts[0]
        self.units = int(parts[1])


def part1(commands):
    position = 0
    depth = 0
    for cmd in commands:
        if cmd.direction == "forward":
            position += cmd.units
        elif cmd.direction == "down":
            depth += cmd.units
        elif cmd.direction == "up":
            depth -= cmd.units
        else:
            raise RuntimeError("Unrecognised command!")

    return depth * position


def part2(commands):
    position = 0
    depth = 0
    aim = 0
    for cmd in commands:
        if cmd.direction == "forward":
            position += cmd.units
            depth += (aim * cmd.units)
        elif cmd.direction == "down":
            aim += cmd.units
        elif cmd.direction == "up":
            aim -= cmd.units
        else:
            raise RuntimeError("Unrecognised command!")

    return depth * position


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = [Command(line) for line in f.readlines()]

    print(part1(puzzle_input))
    print(part2(puzzle_input))