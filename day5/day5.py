from collections import Counter, namedtuple
import re

PUZZLE_INPUT = "puzzle_input.txt"

Point = namedtuple("Point", "x y")


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start = Point(int(x1), int(y1))
        self.end = Point(int(x2), int(y2))

    @property
    def is_horizontal(self):
        return self.start.y == self.end.y

    @property
    def is_vertical(self):
        return self.start.x == self.end.x

    @property
    def points(self):
        x_step = 1 if (self.end.x > self.start.x) else -1
        y_step = 1 if (self.end.y > self.start.y) else -1
        if self.is_horizontal:
            return [(x, self.start.y) for x in range(self.start.x, self.end.x+x_step, x_step)]
        elif self.is_vertical:
            return [(self.start.x, y) for y in range(self.start.y, self.end.y+y_step, y_step)]
        else:
            return [(x, self.start.y+(i*y_step)) for i, x in enumerate(range(self.start.x, self.end.x+x_step, x_step))]

    def __repr__(self):
        return f"{self.start} -> {self.end}"


def part1(lines):
    all_points = Counter()
    for line in lines:
        if line.is_vertical or line.is_horizontal:
            all_points.update(line.points)
    danger_areas = [point for (point, count) in all_points.items() if count >= 2]
    return len(danger_areas)


def part2(lines):
    all_points = Counter()
    for line in lines:
        all_points.update(line.points)
    danger_areas = [point for (point, count) in all_points.items() if count >= 2]
    return len(danger_areas)


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        _lines = [Line(*re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups()) for line in f.readlines()]

    print(part1(_lines))
    print(part2(_lines))
