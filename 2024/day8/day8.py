from collections import defaultdict
from math import gcd


def main() -> None:
    antennas = defaultdict(list)
    grid = []
    unique_antinode_p1 = set()
    unique_antinode_p2 = set()

    with open('input') as f:
        for line in f:
            grid.append(list(line.strip()))

    for row, line in enumerate(grid):
        for column, character in enumerate(line):
            if character != '.':
                antennas[character].append([row, column])

    row_lim = len(grid)
    col_lim = len(grid[0])

    for positions in antennas.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                antenna_1 = positions[i]
                unique_antinode_p2.add(tuple(antenna_1))

                antenna_2 = positions[j]
                unique_antinode_p2.add(tuple(antenna_2))

                dx, dy = antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1]

                candidates = [
                    [antenna_1[0] - dx, antenna_1[1] - dy],
                    [antenna_2[0] + dx, antenna_2[1] + dy],
                ]

                for candidate in candidates:
                    if 0 <= candidate[0] < row_lim and 0 <= candidate[1] < col_lim:
                        d1 = abs(candidate[0] - antenna_1[0]) + abs(candidate[1] - antenna_1[1])
                        d2 = abs(candidate[0] - antenna_2[0]) + abs(candidate[1] - antenna_2[1])

                        if d1 == 2 * d2 or d2 == 2 * d1:
                            unique_antinode_p1.add(tuple(candidate))
                            unique_antinode_p2.add(tuple(candidate))

                x, y = antenna_1
                step_x, step_y = dx // gcd(dx, dy), dy // gcd(dx, dy)

                while (x, y) != (antenna_2[0], antenna_2[1]):
                    unique_antinode_p2.add((x, y))
                    x += step_x
                    y += step_y

                x, y = antenna_1

                while 0 <= x < row_lim and 0 <= y < col_lim:
                    unique_antinode_p2.add((x, y))
                    x -= dx
                    y -= dy

                x, y = antenna_2

                while 0 <= x < row_lim and 0 <= y < col_lim:
                    unique_antinode_p2.add((x, y))
                    x += dx
                    y += dy


    print(f'Part 1 answer: {len(unique_antinode_p1)}')
    print(f'Part 2 answer: {len(unique_antinode_p2)}')


if __name__ == '__main__':
    main()
