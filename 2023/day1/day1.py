import re

calibration_document = open('day1_input.txt', 'r')
calibration_sum_part1 = 0
calibration_sum_part2 = 0
for line in calibration_document:
    line_part1 = line

    line = re.sub(r'one', 'one1one', line)
    line = re.sub(r'two', 'two2two', line)
    line = re.sub(r'three', 'three3three', line)
    line = re.sub(r'four', 'four4four', line)
    line = re.sub(r'five', 'five5five', line)
    line = re.sub(r'six', 'six6six', line)
    line = re.sub(r'seven', 'seven7seven', line)
    line = re.sub(r'eight', 'eight8eight', line)
    line = re.sub(r'nine', 'nine9nine', line)

    numbers_part1 = re.findall(r'\d', line_part1)
    numbers_part2 = re.findall(r'\d', line)

    if len(numbers_part1) > 1:
        calibration_sum_part1 += int(numbers_part1[0] + numbers_part1[-1])
    else:
        calibration_sum_part1 += int(numbers_part1[0] + numbers_part1[0])

    if len(numbers_part2) > 1:
        calibration_sum_part2 += int(numbers_part2[0] + numbers_part2[-1])
    else:
        calibration_sum_part2 += int(numbers_part2[0] + numbers_part2[0])

print(f'Part 1 answer: {calibration_sum_part1}')
print(f'Part 2 answer: {calibration_sum_part2}')
