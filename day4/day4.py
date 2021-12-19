PUZZLE_INPUT = "puzzle_input.txt"


class Number:
    def __init__(self, num):
        self.value = num
        self.is_marked = False


class Board:
    def __init__(self, rows):
        self.rows = [[Number(val) for val in map(int, row.split())] for row in rows]

    @property
    def columns(self):
        return [[row[i] for row in self.rows] for i, row in enumerate(self.rows)]

    def mark(self, num):
        for row in self.rows:
            for number in row:
                if number.value == num:
                    number.is_marked = True

    def is_complete(self):
        if any(all(n.is_marked for n in row) for row in self.rows):
            return True
        elif any(all(n.is_marked for n in column) for column in self.columns):
            return True
        else:
            return False

    def sum_unmarked(self):
        return sum([sum(n.value for n in row if not n.is_marked) for row in self.rows])

    def __repr__(self):
        return "\n".join(" ".join(f"{n.value:02}" for n in row) for row in self.rows) + "\n"


def part1(boards, draw_order):
    for called_num in draw_order:
        for board in boards:
            board.mark(called_num)
            if board.is_complete():
                return called_num * board.sum_unmarked()


def part2(boards, draw_order):
    for called_num in draw_order:
        for board in boards:
            board.mark(called_num)
            num_complete = len([b for b in boards if b.is_complete()])
            if num_complete == len(boards):
                return called_num * board.sum_unmarked()


def create_boards(input_lines):
    game_boards = []
    board_rows = []
    for line in input_lines:
        if line == "":
            game_boards.append(Board(board_rows))
            board_rows = []
        else:
            board_rows.append(line)
    game_boards.append(Board(board_rows))
    return game_boards


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        called_nums = list(map(int, f.readline().split(",")))
        f.readline()
        rest = [line.rstrip() for line in f.readlines()]

    print(part1(create_boards(rest), called_nums))
    print(part2(create_boards(rest), called_nums))
