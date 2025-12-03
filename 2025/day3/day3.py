def main():
    input = open("input", "r").read().splitlines()
    total = 0
    total_12 = 0

    for bank in input:
        max_left = -1
        best = -1
        k = 12 # len of subseq to find
        to_remove = len(bank) - k
        stack = []

        for ch in bank:
            d = int(ch)
            while stack and to_remove > 0 and stack[-1] < ch:
                stack.pop()
                to_remove -= 1
            stack.append(ch)

            if max_left != -1:
                cand = 10 * max_left + d
                if cand > best:
                    best = cand

            if d > max_left:
                max_left = d

        total += best
        total_12 += int(''.join(stack[:k]))

    print(f"Part 1 answer: {total}")
    print(f"Part 2 answer: {total_12}")


if __name__ == '__main__':
    main()
