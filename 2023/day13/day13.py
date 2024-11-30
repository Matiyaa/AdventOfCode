def main():
    def find_mirror_1(grid: list[str]):
        for i in range(1, len(grid)):
            above = grid[:i][::-1]
            below = grid[i:]

            above = above[:len(below)]
            below = below[:len(above)]

            if above == below:
                return i
        return 0

    def find_mirror_2(grid: list[str]):
        for i in range(1, len(grid)):
            above = grid[:i][::-1]
            below = grid[i:]

            if sum(sum(0 if a == b else 1 for a, b in zip(x,y)) for x, y in zip(above, below)) == 1:
                return i
        return 0


    answer_part1 = 0
    answer_part2 = 0

    with open('input', 'r') as f:
        lines = f.read().split('\n\n')
        for pattern in lines:
            grid = pattern.splitlines()

            row = find_mirror_1(grid)
            answer_part1 += row * 100

            col = find_mirror_1(list(zip(*grid)))
            answer_part1 += col

            row = find_mirror_2(grid)
            answer_part2 += row * 100

            col = find_mirror_2(list(zip(*grid)))
            answer_part2 += col


    print(f'Part 1 answer: {answer_part1}')
    print(f'Part 2 answer: {answer_part2}')


if __name__ == '__main__':
    main()