def find_word_in_matrix(matrix, word):
    word_len = len(word)
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if c + word_len <= cols:
                if ''.join(matrix[r][c:c+word_len]) == word:
                    count += 1
                if ''.join(matrix[r][c:c+word_len][::-1]) == word:
                    count += 1
            if r + word_len <= rows:
                if ''.join(matrix[r+i][c] for i in range(word_len)) == word:
                    count += 1
                if ''.join(matrix[r+i][c] for i in range(word_len))[::-1] == word:
                    count += 1

    for r in range(rows - word_len + 1):
        for c in range(cols - word_len + 1):
            if ''.join(matrix[r+i][c+i] for i in range(word_len)) == word:
                count += 1
            if ''.join(matrix[r+i][c+i] for i in range(word_len))[::-1] == word:
                count += 1
            if ''.join(matrix[r+i][c+word_len-1-i] for i in range(word_len)) == word:
                count += 1
            if ''.join(matrix[r+i][c+word_len-1-i] for i in range(word_len))[::-1] == word:
                count += 1

    return count


def find_x_mas_in_matrix(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    diagonal = ["MAS", "SAM"]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            first = matrix[r - 1][c - 1] + matrix[r][c] + matrix[r + 1][c + 1]
            second = matrix[r - 1][c + 1] + matrix[r][c] + matrix[r + 1][c - 1]
            if first in diagonal and second in diagonal:
                count += 1

    return count


def main():
    with open('input', 'r') as file:
        data = file.read().splitlines()
        data = [list(line) for line in data]

    word = 'XMAS'
    count_xmas = find_word_in_matrix(data, word)
    count_x_mas = find_x_mas_in_matrix(data)

    print(f"Part 1 answer: {count_xmas}")
    print(f"Part 2 answer: {count_x_mas}")

if __name__ == '__main__':
    main()