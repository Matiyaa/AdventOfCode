from functools import reduce
import operator


race_log = open('day6_input.txt', 'r')
times = list(map(int, race_log.readline().split()[1:]))
distances = list(map(int, race_log.readline().split()[1:]))
race_time = int(''.join(map(str, times)))
race_distance = int(''.join(map(str, distances)))


def race_won(time, distance, time_held):
    if time_held * (time - time_held) > distance:
        return True
    else:
        return False


ways_to_win_part1 = [0 for i in times]
for i in range(len(times)):
    for j in range(times[i]):
        if race_won(times[i], distances[i], j):
            ways_to_win_part1[i] += 1

ways_to_win_part2 = 0
for i in range(race_time):
    if race_won(race_time, race_distance, i):
        ways_to_win_part2 += 1

print(f'Part 1 answer: {reduce(operator.mul, ways_to_win_part1, 1)}')
print(f'Part 2 answer: {ways_to_win_part2}')
