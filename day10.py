from collections import deque


def main():
    pipe_map = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        "7": [(1, 0), (0, -1)],
        ".": [],
    }

    with open('day10_input.txt', 'r') as maze:
        grid = [line.strip() for line in maze.readlines()]

    start_row, start_column = 0, 0

    for start_row, line in enumerate(grid):
        try:
            start_column = line.index('S')
            break
        except ValueError:
            pass

    grid[start_row] = grid[start_row].replace("S", start_type(start_row, start_column, grid, pipe_map))

    row, column = start_row, start_column

    seen = set()
    queue = deque([(row, column)])

    while queue:
        row, column = queue.popleft()

        if (row, column) in seen:
            continue
        seen.add((row, column))

        for row2, column2 in valid_moves(row, column, grid, pipe_map):
            queue.append((row2, column2))

    part1 = len(seen) // 2
    print(f"Part 1 answer: {part1}")

    part2 = 0
    grid2 = ""
    for row, line in enumerate(grid):
        for column, char in enumerate(line):
            grid2 += "." if (row, column) not in seen else char
        grid2 += "\n"

    grid2 = grid2.split("\n")

    for line in grid2:
        outside = True
        startF = None
        for char in line:
            match char:
                case ".":
                    if not outside:
                        part2 += 1
                case "|":
                    outside = not outside
                case "F":
                    startF = True
                case "L":
                    startF = False
                case "-":
                    assert not startF is None
                case "7":
                    assert not startF is None
                    if not startF:
                        outside = not outside
                    startF = None
                case "J":
                    assert not startF is None
                    if startF:
                        outside = not outside
                    startF = None

    print(f"Part 2 answer: {part2}")


def start_type(row, column, grid, pipe_map):
    resource = []

    for grid_row, grid_column in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        for grid_row2, grid_column2 in pipe_map[grid[row + grid_row][column + grid_column]]:
            if grid_row + grid_row2 == 0 and grid_column + grid_column2 == 0:
                resource.append((grid_row, grid_column))
    assert len(resource) == 2

    for starts_type, moves in pipe_map.items():
        if all(move in moves for move in resource):
            return starts_type


def valid_moves(row, column, grid, pipe_map):
    pipe_type = grid[row][column]
    return [(row + row2, column + column2) for row2, column2 in pipe_map[pipe_type]]


if __name__ == '__main__':
    main()
