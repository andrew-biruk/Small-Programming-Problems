# A poker deck contains 52 cards.
# Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
# Each card also has a value of either 2 through 10, jack, queen, king, or ace
# (denoted 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).
# For scoring purposes card values are ordered as above, with 2 having the lowest and ace the highest value.
# The suit has no impact on value.
# A poker hand consists of five cards.

hand = "JC JC KC KC KC"
corresponding_values = hand.maketrans(dict(zip(["J", "Q", "K", "A"], ["11", "12", "13", "14"])))
hand = sorted([(int(c[:-1]), c[-1]) for c in hand.translate(corresponding_values).split()])


def is_flush(h):
    def kind_of_flash():
        return ["Flush", ["Straight Flush", "Royal Flush"][h[0][0] == 10]][bool(is_straight(h))]

    return [False, kind_of_flash()][any(all(c[1] == suit for c in h) for suit in "CDHS")]


def is_straight(h):
    return [False, "Straight"][list(range(h[0][0], h[-1][0] + 1)) == [c[0] for c in h]]


def other_combinations(h):
    values = [card[0] for card in h]
    values_combination = [values.count(v) for v in values]
    occur = {1: "High Card",
             2: "Pair",
             3: "Three of a Kind",
             4: "Four of a Kind"}
    if sorted(set(values_combination)) == [2, 3]:
        return "Full House"
    return [occur[max(values_combination)], "Two Pairs"][values_combination.count(2) == 4]


print(is_flush(hand) or is_straight(hand) or other_combinations(hand))
