import re


engine_schematic = open('day3_input.txt', 'r')
symbol_indexes = []
gear_indexes = []
numbers_indexes_part1 = []
numbers_indexes_part2 = []
parts_sum = 0
line_index = 0
gear_ratio_sum = 0

for line in engine_schematic:
    symbol_indexes.append([match.start() for match in re.finditer(r'[^.\w\n]', line)])
    gear_indexes.append([match.start() for match in re.finditer(r'\*', line)])

engine_schematic = open('day3_input.txt', 'r')  # refreshing iterator

for line in engine_schematic:
    is_part = False

    numbers_indexes_part1.append([(match.start(), match.end(), int(line[match.start(): match.end()])) for match in re.finditer(r'\d+', line)])
    numbers_indexes_part2.append([(match.start(), match.end() - 1, int(line[match.start(): match.end()])) for match in re.finditer(r'\d+', line)])

    if line_index == 0:
        for index_tuple in numbers_indexes_part1[line_index]:
            index_range = range(index_tuple[0] - 1, index_tuple[1] + 1)
            is_part_current = any(number in symbol_indexes[line_index] for number in index_range)
            is_part_next = any(number in symbol_indexes[line_index + 1] for number in index_range)
            is_part = is_part_current or is_part_next
            if is_part:
                parts_sum += index_tuple[2]

    elif line_index == len(symbol_indexes) - 1:
        for index_tuple in numbers_indexes_part1[line_index]:
            index_range = range(index_tuple[0] - 1, index_tuple[1] + 1)
            is_part_previous = any(number in symbol_indexes[line_index - 1] for number in index_range)
            is_part_current = any(number in symbol_indexes[line_index] for number in index_range)
            is_part = is_part_previous or is_part_current
            if is_part:
                parts_sum += index_tuple[2]

    else:
        for index_tuple in numbers_indexes_part1[line_index]:
            index_range = range(index_tuple[0] - 1, index_tuple[1] + 1)
            is_part_previous = any(number in symbol_indexes[line_index - 1] for number in index_range)
            is_part_current = any(number in symbol_indexes[line_index] for number in index_range)
            is_part_next = any(number in symbol_indexes[line_index + 1] for number in index_range)
            is_part = is_part_previous or is_part_current or is_part_next
            if is_part:
                parts_sum += index_tuple[2]

    line_index += 1

gear_list_index = 0
for gear_list in gear_indexes:
    for gear in gear_list:
        gear_ratio = 1
        gear_range = range(gear - 1, gear + 2)

        if gear_list_index == 0:
            gear_adj_current = [tup for tup in numbers_indexes_part2[gear_list_index] if tup[0] in gear_range or tup[1] in gear_range]
            gear_adj_next = [tup for tup in numbers_indexes_part2[gear_list_index + 1] if tup[0] in gear_range or tup[1] in gear_range]
            if len(gear_adj_current) + len(gear_adj_next) == 2:
                for tup in gear_adj_current:
                    gear_ratio *= tup[2]
                for tup in gear_adj_next:
                    gear_ratio *= tup[2]
                print(gear_ratio)
                gear_ratio_sum += gear_ratio

        elif gear_list_index == len(gear_indexes) - 1:
            gear_adj_previous = [tup for tup in numbers_indexes_part2[gear_list_index - 1] if tup[0] in gear_range or tup[1] in gear_range]
            gear_adj_current = [tup for tup in numbers_indexes_part2[gear_list_index] if tup[0] in gear_range or tup[1] in gear_range]
            if len(gear_adj_previous) + len(gear_adj_current) == 2:
                for tup in gear_adj_previous:
                    gear_ratio *= tup[2]
                for tup in gear_adj_current:
                    gear_ratio *= tup[2]
                gear_ratio_sum += gear_ratio

        else:
            gear_adj_previous = [tup for tup in numbers_indexes_part2[gear_list_index - 1] if tup[0] in gear_range or tup[1] in gear_range]
            gear_adj_current = [tup for tup in numbers_indexes_part2[gear_list_index] if tup[0] in gear_range or tup[1] in gear_range]
            gear_adj_next = [tup for tup in numbers_indexes_part2[gear_list_index + 1] if tup[0] in gear_range or tup[1] in gear_range]
            if len(gear_adj_previous) + len(gear_adj_current) + len(gear_adj_next) == 2:
                for tup in gear_adj_previous:
                    gear_ratio *= tup[2]
                for tup in gear_adj_current:
                    gear_ratio *= tup[2]
                for tup in gear_adj_next:
                    gear_ratio *= tup[2]
                gear_ratio_sum += gear_ratio
    gear_list_index += 1

print(f'Part 1 answer: {parts_sum}')
print(f'Part 2 answer: {gear_ratio_sum}')
