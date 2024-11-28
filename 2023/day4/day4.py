scratchcard_pile = open('day4_input.txt', 'r')
points = 0
new_pile = []
cards_total = 0

for index, scratchcard in enumerate(scratchcard_pile):
    scratchcard = scratchcard.strip().split(':')[1].split('|')
    winning_numbers, numbers = set(scratchcard[0].split()), set(scratchcard[1].split())
    counter = len(winning_numbers.intersection(numbers))
    if counter == 1:
        points += 1
    elif counter > 1:
        points += (2 ** (counter - 1))
    new_pile.append([index, counter, 1])

for card in new_pile:
    index = card[0]
    if card[1] > 0:
        for i in range(1, card[1] + 1):
            card_to_copy = index + i
            if card_to_copy <= len(new_pile) - 1:
                new_pile[card_to_copy][2] += card[2]

for card in new_pile:
    cards_total += card[2]

print(f'Part 1 answer: {points}')
print(f'Part 2 answer: {cards_total}')
