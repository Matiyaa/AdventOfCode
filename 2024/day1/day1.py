def main():
    left = []
    right = []

    with open("input", "r") as file:
        data = file.read().splitlines()

        for line in data:
            line = line.split()
            left.append(int(line[0]))
            right.append(int(line[1]))

    distances = 0
    similarities = 0

    left.sort()
    right.sort()

    for i in range(len(left)):
        distances += abs(left[i] - right[i])
        similarities += right.count(left[i]) * left[i]

    print(f"Part 1 answer: {distances}")
    print(f"Part 2 answer: {similarities}")

if __name__ == "__main__":
    main()