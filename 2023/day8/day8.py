import ast
import math


def travel(start_node, answer_nodes, sequence, instructions):
    current_node = start_node
    steps = 0
    while current_node not in answer_nodes:
        for i in sequence:
            next_node = instructions[current_node][int(i)]
            current_node = indexes.index(next_node)
            steps += 1
            if current_node in answer_nodes:
                break

    return steps


network = open('day8_input.txt', 'r')
sequence = network.readline().strip().replace('L', '0').replace('R', '1')
network.readline()
indexes = []
instructions = []

for line in network:
    convert = line.strip().split('=')
    indexes.append(convert[0].strip())
    instruction = convert[1].replace('(', "('").replace(', ', "','").replace(')', "')")
    instructions.append(ast.literal_eval(instruction))

current_node = indexes.index('AAA')
last_node = indexes.index('ZZZ')
steps_part1 = travel(current_node, [last_node], sequence, instructions)

current_nodes = [indexes.index(i) for i in indexes if i.endswith('A')]
Z_nodes = [indexes.index(i) for i in indexes if i.endswith('Z')]
steps_part2 = []

for i in current_nodes:
    steps_part2.append(travel(i, Z_nodes, sequence, instructions))

print(f'Part 1 answer: {steps_part1}')
print(f'Part 2 answer: {math.lcm(*steps_part2)}')
