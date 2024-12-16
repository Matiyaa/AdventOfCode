from itertools import product


def main() -> None:
    OPERATIONS = ["+", "*"]
    PART2_OPERATION = ["||"] + OPERATIONS
    with open('input') as f:
        lines = f.readlines()

    result_p1 = 0
    result_p2 = 0

    for line in lines:
        line = line.strip().split(': ')
        target = int(line[0])
        values = list(map(int, line[1].split(' ')))

        correct = is_valid_equation(target, values, OPERATIONS)

        result_p1 += target if correct else 0

        if not correct:
            correct = is_valid_equation(target, values, PART2_OPERATION)
            result_p2 += target if correct else 0


    print(f'Part 1 answer: {result_p1}')
    print(f'Part 2 answer: {result_p1 + result_p2}')

def is_valid_equation(target: int, values: list[int], operations:list[str]) -> bool:
    operations_num = len(values) - 1
    all_operations_combinations = list(product(operations, repeat=operations_num))

    for operation_combination in all_operations_combinations:
        result = values[0]
        for number, operation in zip(values[1:], operation_combination):
            if operation == '||':
                result = int(str(result) + str(number))
            else:
                result = eval(f'{result}{operation}{number}')

            if result > target:
                break
        if result == target:
            return True

    return False

if __name__ == '__main__':
    main()
