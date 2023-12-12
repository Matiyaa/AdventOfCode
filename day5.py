import sys
from operator import itemgetter


def map_seed(seed, mapped):
    destination_starts, source_starts, _ = mapped
    return destination_starts + seed - source_starts


def map_seed_range(seed_range, map_ranges):
    seed_ranges = []
    seed_starts, seed_ends = seed_range[0], seed_range[1]

    for mapped in map_ranges:
        source_start, source_end = mapped[1], mapped[1] + mapped[2] - 1
        overlap_starts = max(seed_starts, source_start)
        overlap_ends = min(seed_ends, source_end)

        if overlap_ends >= overlap_starts:
            if seed_starts <= overlap_starts - 1:
                seed_ranges.append((seed_starts, overlap_starts - 1))

            seed_ranges.append((map_seed(overlap_starts, mapped), map_seed(overlap_ends, mapped)))

            if overlap_ends + 1 <= seed_ends:
                seed_starts = overlap_ends + 1
            else:
                seed_starts = sys.maxsize
                break

    if seed_starts <= seed_ends:
        seed_ranges.append((seed_starts, seed_ends))

    return seed_ranges


almanac = 'day5_input.txt'

with open(almanac) as almanac:
    seeds = list(map(int, almanac.readline().split()[1:]))
    almanac.readline()
    almanac.readline()
    maps = []
    map_ranges = []

    for line in almanac:
        if line == '\n':
            map_ranges.sort(key=itemgetter(1))
            maps.append(map_ranges)
            map_ranges = []
            next(almanac)
        else:
            map_ranges.append(tuple(map(int, line.split())))
    if map_ranges:
        map_ranges.sort(key=itemgetter(1))
        maps.append(map_ranges)

    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

lowest_location_part1 = sys.maxsize
for seed in seeds:
    for map_ranges in maps:
        for destination_starts, source_starts, length in map_ranges:
            if source_starts <= seed <= source_starts + length - 1:
                seed = destination_starts + seed - source_starts
                break
    lowest_location_part1 = min(seed, lowest_location_part1)

for map_ranges in maps:
    new_seed_ranges = []
    for seed_range in seed_ranges:
        new_seed_ranges += map_seed_range(seed_range, map_ranges)
    seed_ranges = new_seed_ranges

lowest_location_part2 = min(seed_range[0] for seed_range in seed_ranges)

print(f'Part 1 answer: {lowest_location_part1}')
print(f'Part 2 answer: {lowest_location_part2}')
