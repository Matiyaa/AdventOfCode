history = open('day9_input.txt', 'r')
values = []

def differences(val_list):
    new_list = [val_list]
    diff_list = []

    for i in range(len(val_list) - 1):
        diff_list.append(val_list[i + 1] - val_list[i])

    new_list.append(diff_list)

    if not all(element == 0 for element in diff_list):
        returned = differences(diff_list)
        new_list.extend(returned[1:])

    return new_list


for line in history:
    values.append([int(x) for x in line.split()])

for i in values:
    values[values.index(i)] = differences(i)

for i in range(len(values)):
    for j in range(len(values[i]) - 1, 0, -1):
        temp_val = values[i][j][-1] + values[i][j-1][-1]
        values[i][j - 1].append(temp_val)

for i in range(len(values)):
    for j in range(len(values[i]) - 1, 0, -1):
        temp_val = values[i][j - 1][0] - values[i][j][0]
        values[i][j - 1].insert(0, temp_val)

sum_of_last_elements = sum(sublist[0][-1] for sublist in values)
sum_of_first_elements = sum(sublist[0][0] for sublist in values)

print(f'Part 1 answer: {sum_of_last_elements}')
print(f'Part 2 answer: {sum_of_first_elements}')