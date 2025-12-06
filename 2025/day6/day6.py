import numpy as np

def main():
    input = open("input", "r").read().splitlines()
    operations = input.pop(-1).split()
    numbers = [line.split() for line in input]
    array = np.array(numbers, dtype=int)
    array = array.transpose()

    ops = np.array(operations)
    sums = np.sum(array, axis=1)
    prods = np.prod(array, axis=1)
    total = sums[ops == '+'].sum() + prods[ops == '*'].sum()

    print(f"Part 1 answer: {total}")

    H = len(input)
    W = max(len(l) for l in input)
    grid = [list(l.ljust(W)) for l in input]

    def is_blank_col(c):
        return all(grid[r][c] == ' ' for r in range(H))

    blocks = []
    blocks_sums = []
    blocks_prods = []
    start = None

    for c in range(W):
        if is_blank_col(c):
            if start is not None:
                blocks.append(list(range(start, c)))
                start = None
        else:
            if start is None:
                start = c

    if start is not None:
        blocks.append(list(range(start, W)))

    for cols in blocks:
        nums = []
        for c in reversed(cols):
            digits = [grid[r][c] for r in range(H) if grid[r][c].isdigit()]
            if digits:
                nums.append(int(''.join(digits)))
        blocks_sums.append(np.sum(nums))
        blocks_prods.append(np.prod(nums))

    sums2 = np.array(blocks_sums)
    prods2 = np.array(blocks_prods)
    total2 = sums2[ops == '+'].sum() + prods2[ops == '*'].sum()

    print(f"Part 2 answer: {total2}")


if __name__ == '__main__':
    main()
