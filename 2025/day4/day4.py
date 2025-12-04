import numpy as np
from scipy.signal import convolve2d


def main():
    input = open("input", "r").read().splitlines()
    arr = np.array([[1 if c == '@' else 0 for c in row] for row in input])

    kernel = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    neighbor_counts = convolve2d(arr, kernel, mode='same', boundary='fill', fillvalue=0)
    accessible = (arr == 1) & (neighbor_counts < 4)
    total = accessible.sum()
    arr[accessible] = 0

    print(f"Part 1 answer: {accessible.sum()}")

    while accessible.sum() > 0:
        neighbor_counts = convolve2d(arr, kernel, mode='same', boundary='fill', fillvalue=0)
        accessible = (arr == 1) & (neighbor_counts < 4)
        arr[accessible] = 0
        total += accessible.sum()

    print(f"Part 2 answer: {total}")


if __name__ == '__main__':
    main()
