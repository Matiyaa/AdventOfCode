import re


game_log = open('day2_input.txt', 'r')

game_id_sum = 0
set_power_sum = 0
cubes = {'red': 12, 'green': 13, 'blue': 14}

for game in game_log:
    game_possible = True
    log = re.findall(r'\w+', game)
    game_id = int(log[1])
    n = 3
    cubes_test = {'red': 0, 'green': 0, 'blue': 0}
    set_power = 1

    while n < len(log):
        cube = log[n]
        cube_value = int(log[n - 1])

        if cubes.get(cube) >= cube_value:
            pass
        else:
            game_possible = False
        if cubes_test.get(cube) < cube_value:
            cubes_test[cube] = cube_value
        n += 2

    if game_possible:
        game_id_sum += game_id

    for i in cubes_test.values():
        if i:
            set_power *= i

    set_power_sum += set_power

print(f'Part 1 answer: {game_id_sum}')
print(f'Part 2 answer: {set_power_sum}')
