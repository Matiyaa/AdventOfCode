def main():
    rules = []
    sequences = []
    right_order = []
    wrong_order = []
    answer_p1 = 0
    answer_p2 = 0

    with open("input", "r") as file:
        lines = file.readlines()
        for line in lines:
            if '|' in line:
                rules.append(list(map(int, line.strip().split('|'))))
            if ',' in line:
                sequences.append(list(map(int, line.split(','))))

    for sequence in sequences:
        correct = True
        for rule in rules:
            if (rule[0] in sequence) and (rule[1] in sequence):
                if not sequence.index(rule[0]) < sequence.index(rule[1]):
                    correct = False



        if correct:
            right_order.append(sequence)
        else:
            wrong_order.append(sequence)

    for sequence in right_order:
        answer_p1 += sequence[len(sequence) // 2]

    right_order = []
    amount = len(wrong_order)
    while len(right_order) < amount:
        for sequence in wrong_order:
            correct = True
            for rule in rules:
                if (rule[0] in sequence) and (rule[1] in sequence):
                    if not sequence.index(rule[0]) < sequence.index(rule[1]):
                        correct = False
                        sequence.insert(sequence.index(rule[0]), sequence.pop(sequence.index(rule[1])))

            if correct:
                right_order.append(sequence)
                wrong_order.remove(sequence)

    for sequence in right_order:
        answer_p2 += sequence[len(sequence) // 2]

    print(f"Part 1 answer: {answer_p1}")
    print(f"Part 2 answer: {answer_p2}")

if __name__ == "__main__":
    main()
