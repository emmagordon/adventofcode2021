import re

PUZZLE_INPUT = "puzzle_input.txt"


class TargetArea:
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def __repr__(self):
        return f"TargetArea({self.x_min}, {self.x_max}, {self.y_min}, {self.y_max})"


def part1(t):
    # x and y motion are independent, so we only need consider y
    # y decreases by 1 each step, therefore up/down from y_pos of 0 to peak and back to 0 again are symmetrical
    # e.g. for initial y_vel of 3, we will go up 3, 2, 1, (0) then down -1, -2, -3 to get to y_pos = 0 again
    # and first y_pos below 0 will be at -y_vel-1
    # if this is lower than y_min, then we have overshot
    # i.e. to find the highest peak, find the largest initial y_vel for which -y_vel-1 is >= y_min
    # (which is -y_min - 1)
    y_vel = -t.y_min - 1
    return sum(range(y_vel, 0, -1))


def part2(t):
    # search bounds given by velocities that would overshoot the target
    # search y between -y_min and the y_vel from part1 (which gives the highest peak)
    # for each y value, search x between 0 and x_max
    # in above search, keep going over steps until we are below y_min (at this point have overshot)
    initial_velocity_values = set()
    for y in range(t.y_min, -t.y_min):
        for x in range(0, t.x_max+1):
            y_vel = y
            x_vel = x
            y_pos = 0
            x_pos = 0
            while y_pos >= t.y_min:
                x_pos += x_vel
                y_pos += y_vel
                if (t.x_min <= x_pos <= t.x_max) and (t.y_min <= y_pos <= t.y_max):
                    initial_velocity_values.add((x, y))
                    break
                x_vel += (1 if x_vel < 0 else (-1 if x_vel > 0 else 0))
                y_vel -= 1
    return len(initial_velocity_values)


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        puzzle_input = f.readline().rstrip()

    m = re.match(r"target area: x=(-*\d+)\.\.(-*\d+), y=(-*\d+)\.\.(-*\d+)", puzzle_input)
    target_area = TargetArea(*map(int, m.groups()))

    print(part1(target_area))
    print(part2(target_area))
