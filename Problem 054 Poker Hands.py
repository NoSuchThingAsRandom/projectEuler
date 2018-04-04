# Functions for determining hands
def royal_flush(cards):
    if straight_flush(cards) == 14:
        return card_values["A"]
    return 0


def straight_flush(cards):
    if flush(cards) != 0:
        return straight(cards)
    return 0


def four(cards):
    card_sort = sort(cards)
    compare = card_sort[0]
    for x in range(1, len(card_sort) - 1):
        if card_sort[x] != compare:
            return 0
    return compare


def full_house(cards):
    card_sort = sort(cards)
    if card_sort[0] == card_sort[1]:
        if card_sort[0] == card_sort[2]:
            if card_sort[3] == card_sort[4]:  # Two pair at end
                return card_sort[0]
        elif card_sort[3] == card_sort[4]:
            return card_sort[4]
    return 0


def flush(cards):
    suit = cards[0][1]
    for c in cards:
        if suit != c[1]:
            return 0
    return sort(cards).reverse()


def straight(cards):
    card_sort = sort(cards)
    compare = card_sort[0]
    for i in card_sort:
        if compare != i:
            return 0
        compare += 1
    return card_sort[4]


def three(cards):
    current = 1
    for c in cards:
        for x in range(current, len(cards)):
            if card_values[c[0]] == card_values[cards[x][0]]:
                for y in range((x + 1), len(cards)):
                    if card_values[c[0]] == card_values[cards[y][0]]:
                        return card_values[c[0]]
        current += 1
    return 0


def two_pair(cards):
    card_sort = sort(cards)
    values = []
    spare = 0
    pairs = 0
    for x in range(0, len(card_sort) - 1):
        if card_sort[x] == card_sort[x + 1]:
            pairs += 1
            values.append(card_sort[x])
    if pairs == 2:
        values.sort()
        for c in card_sort:
            if c != values[0] or c != values[1]:
                spare = c
                break
        values.reverse()
        values.append(spare)
        return values
    return 0


def pair(cards):
    current = 1
    for c in cards:
        for x in range(current, len(cards)):
            if card_values[c[0]] == card_values[cards[x][0]]:
                card_sort = sort(cards)
                card_sort.remove(card_values[c[0]])
                card_sort.remove(card_values[c[0]])
                card_sort.append(card_values[c[0]])
                card_sort.reverse()
                return card_sort
        current += 1
    return 0


def high(cards):
    card_sort = sort(cards)
    card_sort.reverse()
    return card_sort


def sort(cards):
    values = []
    for c in cards:
        values.append(card_values[c[0]])
    values.sort()
    return values


hands = []  # Stores all hands
# Lookup dictionaries
card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,
               "A": 14}

testHand = [royal_flush, straight_flush, four, full_house, flush, straight, three, two_pair, pair, high]


# Actual program
def read_hands(name):
    global hands
    file = open(name, "r")
    for line in file:
        hands.append(line.replace("\n", "").split(" "))
    file.close()


def hand_value(hand):
    hand_type = 0
    for func in testHand:
        score = func(hand)
        if score != 0:
            return [hand_type, score]
        hand_type += 1


def debug():
    print(hand_value([["T", "H"], ["K", "H"], ["Q", "H"], ["A", "H"], ["J", "H"]]))  # Royal Flush
    print(hand_value([["T", "H"], ["7", "H"], ["6", "H"], ["9", "H"], ["8", "H"]]))  # Straight Flush
    print(hand_value([["9", "H"], ["7", "H"], ["7", "D"], ["7", "C"], ["7", "S"]]))  # Four of a kind
    print(hand_value([["9", "H"], ["9", "H"], ["9", "D"], ["7", "C"], ["7", "S"]]))  # Full House
    print(hand_value([["2", "H"], ["9", "H"], ["3", "H"], ["7", "H"], ["J", "H"]]))  # Flush
    print(hand_value([["2", "H"], ["6", "H"], ["3", "D"], ["4", "H"], ["5", "H"]]))  # Straight
    print(hand_value([["9", "H"], ["7", "H"], ["7", "D"], ["6", "C"], ["7", "S"]]))  # Three of a kind
    print(hand_value([["9", "H"], ["7", "H"], ["7", "D"], ["6", "C"], ["9", "S"]]))  # Two Pairs
    print(hand_value([["9", "H"], ["7", "H"], ["7", "D"], ["6", "C"], ["T", "S"]]))  # Pair
    print(hand_value([["9", "H"], ["7", "H"], ["2", "D"], ["6", "C"], ["Q", "S"]]))  # High


def run():
    read_hands("Problem 054 poker hands.txt")
    wins = 0

    for h in hands:
        p1 = h[:5]
        p2 = h[5:]

        p1_score = hand_value(p1)
        p2_score = hand_value(p2)

        if p1_score[0] < p2_score[0]:
            wins += 1
            print(str(p1) + "     :       " + str(p1_score))
            print(str(p2) + "     :       " + str(p2_score))
            print("WIN")
            print()

        elif p1_score[0] == p2_score[0]:
            for x in range(0, len(p1_score[1])):
                if p1_score[1][x] > p2_score[1][x]:
                    wins += 1
                    print(str(p1) + "     :       " + str(p1_score))
                    print(str(p2) + "     :       " + str(p2_score))
                    print("WIN")
                    print()
                    break
                elif p1_score[1][x] < p2_score[1][x]:
                    break
    print("Wins: " + str(wins))


run()
