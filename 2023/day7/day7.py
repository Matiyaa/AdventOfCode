from collections import Counter


def main():
    winnings_part1 = 0
    winnings_part2 = 0
    hands_log = open('day7_input.txt', 'r').read().strip()
    hands_log = hands_log.split('\n')
    hands = []

    for line in hands_log:
        hand, bid = line.split()
        hands.append((hand, bid))

    hands = sorted(hands, key=lambda line: strength(line[0], False))

    for i, (hand, bid) in enumerate(hands):
        winnings_part1 += (i + 1) * int(bid)

    print(f'Part 1 answer: {winnings_part1}')

    hands = sorted(hands, key=lambda line: strength(line[0], True))

    for i, (hand, bid) in enumerate(hands):
        winnings_part2 += (i + 1) * int(bid)

    print(f'Part 2 answer: {winnings_part2}')


def strength(hand, part2):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1) if part2 else chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    count = Counter(hand)

    if part2:
        target = list(count.keys())[0]
        for k in count:
            if k != '1':
                if count[k] > count[target] or target == '1':
                    target = k
        assert target != '1' or list(count.keys()) == ['1']
        if '1' in count and target != '1':
            count[target] += count['1']
            del count['1']
        assert '1' not in count or list(count.keys()) == ['1'], f'{count} {hand}'

    if list(count.values()) == [5]:
        return 10, hand
    elif sorted(count.values()) == [1, 4]:
        return 9, hand
    elif sorted(count.values()) == [2, 3]:
        return 8, hand
    elif sorted(count.values()) == [1, 1, 3]:
        return 7, hand
    elif sorted(count.values()) == [1, 2, 2]:
        return 6, hand
    elif sorted(count.values()) == [1, 1, 1, 2]:
        return 5, hand
    elif sorted(count.values()) == [1, 1, 1, 1, 1]:
        return 4, hand
    else:
        assert False, f'{count} {hand} {sorted(count.values())}'


if __name__ == '__main__':
    main()
