def main():
    image = open('day11_input.txt').read().strip()
    image = image.split('\n')
    galaxies = [[c for c in line] for line in image]
    rows = len(galaxies)
    columns = len(galaxies[0])

    empty_rows = []
    row = 0
    while row < rows:
        empty = True
        for column in range(columns):
            if galaxies[row][column] == '#':
                empty = False
        if empty:
            empty_rows.append(row)
        row += 1

    empty_columns = []
    column = 0
    while column < columns:
        empty = True
        for row in range(rows):
            if galaxies[row][column] == '#':
                empty = False
        if empty:
            empty_columns.append(column)
        column += 1

    rows = len(galaxies)
    columns = len(galaxies[0])

    galaxies_2 = []
    for row in range(rows):
        for column in range(columns):
            if galaxies[row][column] == '#':
                galaxies_2.append((row, column))

    def expand_galaxies(galaxies, empty_rows, empty_colums, part):
        new_galaxies = []
        expansion_factor = 10**6 - 1 if part == 2 else 2-1
        answer = 0
        for i, (row, column) in enumerate(galaxies):
            for j in range(i, len(galaxies)):
                row_2, column_2 = galaxies[j]
                distance = abs(row - row_2) + abs(column - column_2)
                for empty_row in empty_rows:
                    if min(row, row_2) < empty_row < max(row, row_2):
                        distance += expansion_factor
                for empty_column in empty_columns:
                    if min(column, column_2) < empty_column < max(column, column_2):
                        distance += expansion_factor
                answer += distance
        return answer

    print(f'Part 1 answer: {expand_galaxies(galaxies_2, empty_rows, empty_columns, 1)}')
    print(f'Part 2 answer: {expand_galaxies(galaxies_2, empty_rows, empty_columns, 2)}')


if __name__ == '__main__':
    main()
