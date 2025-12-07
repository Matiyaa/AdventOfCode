def count_splits(grid):
    R, C = len(grid), len(grid[0])

    # find S
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                start_r, start_c = r, c

    prev = [False] * C
    prev[start_c] = True

    splits = 0
    for r in range(start_r + 1, R):
        cur = [False] * C

        for c in range(C):
            if grid[r][c] == "." and prev[c]:
                cur[c] = True
            elif grid[r][c] == "^" and prev[c]:
                if c - 1 >= 0:
                    cur[c - 1] = True
                if c + 1 < C:
                    cur[c + 1] = True
                splits += 1

        prev = cur

    return splits


def count_timelines(grid):
    R, C = len(grid), len(grid[0])

    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                start_r, start_c = r, c

    prev = [0] * C
    prev[start_c] = 1

    for r in range(start_r + 1, R):
        cur = [0] * C

        for c in range(C):
            if prev[c] == 0:
                continue

            if grid[r][c] == ".":
                cur[c] += prev[c]

            elif grid[r][c] == "^":
                if c - 1 >= 0:
                    cur[c - 1] += prev[c]
                if c + 1 < C:
                    cur[c + 1] += prev[c]

        prev = cur

    return sum(prev)


def main():
    input = open("input", "r").read().splitlines()
    print(f"Part 1 answer: {count_splits(input)}")
    print(f"Part 2 answer: {count_timelines(input)}")


if __name__ == '__main__':
    main()
