import bisect


def main():
    ranges, ids = (part.splitlines() for part in open("input", "r").read().strip().split("\n\n"))

    ranges = [tuple(map(int, r.split('-'))) for r in ranges]
    ids = [int(id) for id in ids]

    merged = []
    for s, e in sorted(ranges):
        if not merged or s > merged[-1][1] + 1:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    starts = [s for s, _ in merged]
    fresh = 0

    for x in ids:
        i = bisect.bisect_right(starts, x) - 1
        if i >= 0 and merged[i][0] <= x <= merged[i][1]:
            fresh += 1

    print(f"Part 1 answer: {fresh}")
    print(f"Part 2 answer: {sum(e - s + 1 for s, e in merged)}")


if __name__ == '__main__':
    main()
