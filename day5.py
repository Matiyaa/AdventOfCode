import re


almanac = open('day5_input.txt', 'r')
seeds = []
maps = []
maps_counter = -1

for line in almanac:
    seed_pattern = re.compile(r'^seeds:')
    if seed_pattern.match(line):
        seeds = [int(num) for num in re.findall(r'\b\d+\b', line)]
    elif line == '\n':
        pass
    elif line.endswith('map:\n'):
        maps_counter += 1
        maps.append([])
    else:
        map_list = line.split()
        a = int(map_list[0])
        b = int(map_list[1])
        c = int(map_list[2])
        maps[maps_counter].append((range(a, a + c), range(b, b + c)))

seeds_pairs = []

for i in range(0, len(seeds), 2):
    seeds_pairs.append(range(seeds[i], seeds[i] + seeds[i + 1]))

for mapped in maps:
    for i in range(0, len(seeds)):
        for tup in mapped:
            if seeds[i] in tup[1]:
                transform_seed = seeds[i] - tup[1].start
                seeds[i] = tup[0].start + transform_seed
                break

print(f'Part 1 answer: {min(seeds)}')
