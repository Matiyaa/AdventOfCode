def solver(grid, pos):
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_pos = pos
    curr_move = 0
    visited = set()

    while True:
        visited.add(curr_pos)
        next_pos = (curr_pos[0] + DIRECTIONS[curr_move][0], curr_pos[1] + DIRECTIONS[curr_move][1])


        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            return len(visited)

        if grid[next_pos[0]][next_pos[1]] == "#":
            curr_move = (curr_move + 1) % 4
        else:
            curr_pos = next_pos


def looper(grid, pos):
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_pos = pos
    curr_move = 0
    visited = set()

    while True:
        next_pos = (curr_pos[0] + DIRECTIONS[curr_move][0], curr_pos[1] + DIRECTIONS[curr_move][1])
        if (curr_pos, curr_move) in visited:
            return True

        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            return False

        if grid[next_pos[0]][next_pos[1]] == "#":
            curr_move = (curr_move + 1) % 4
        else:
            visited.add((curr_pos, curr_move))
            curr_pos = next_pos


def main():
    grid = []

    with open("input") as f:
        for line in f:
            grid.append(list(line.strip()))
            if "^" in line:
                start_pos = (len(grid) - 1, line.index("^"))

    part1 = solver(grid, start_pos)
    part2 = 0

    print(f"Part 1 answer: {part1}")

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                continue
            grid[row][col] = "#"
            part2 += 1 if looper(grid, start_pos) else 0
            grid[row][col] = "."

    print(f"Part 2 answer: {part2}")

if __name__ == "__main__":
    main()
