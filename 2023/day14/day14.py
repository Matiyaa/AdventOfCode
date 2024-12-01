def main():
    grid = tuple(open("input", "r").read().splitlines())

    def cycle(grid):
        for _ in range(4):
            grid = tuple(map(''.join, zip(*grid)))
            grid = tuple(['#'.join([''.join(sorted(tuple(group), reverse=True)) for group in row.split('#')]) for row in grid])
            grid = tuple([row[::-1] for row in grid])
        return grid

    grid_p1 = tuple(map(''.join, zip(*grid)))
    grid_p1 = ['#'.join([''.join(sorted(list(group), reverse=True)) for group in row.split('#')]) for row in grid_p1]
    grid_p1 = tuple(map(''.join, zip(*grid_p1)))

    load_p1 = sum(row.count('O') * (len(grid_p1) - r) for r, row in enumerate(grid_p1))

    seen = {grid}
    array = [grid]
    iter = 0

    while True:
        iter += 1
        grid = cycle(grid)

        if grid in seen:
            break

        seen.add(grid)
        array.append(grid)

    first = array.index(grid)
    grid = array[(1000000000 - first) % (iter - first) + first]
    load_p2 = sum(row.count('O') * (len(grid) - r) for r, row in enumerate(grid))

    print(f'Part 1 answer: {load_p1}')
    print(f'Part 2 answer: {load_p2}')


if __name__ == "__main__":
    main()