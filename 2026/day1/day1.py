def main():
    input = open("input", "r").read().splitlines()

    pos = 50
    zeros = 0
    clicks = 0

    for instruction in input:
        rotation = int(instruction[1:])
        full = rotation // 100
        rem = rotation % 100
        old_pos = pos

        if instruction[0] == 'L':
            pos = (pos - rotation) % 100
            k0 = old_pos % 100
            if k0 == 0:
                k0 = 100

            extra = 1 if rem >= k0 else 0

        else:
            pos = (pos + rotation) % 100

            k0 = (100 - old_pos) % 100
            if k0 == 0:
                k0 = 100

            extra = 1 if rem >= k0 else 0

        clicks += full + extra
        zeros += pos == 0

    print(f"Part 1 answer: {zeros}")
    print(f"Part 2 answer: {clicks}")

if __name__ == "__main__":
    main()
