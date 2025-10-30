import random
def build_standard_deck() -> list[dict]:
    cards_suite = ["H", "C", "D", "S"]
    special_cards = ["J", "Q", "K", "A"]
    deck = []
    for i in range(2, 11):
        for j in cards_suite:
            card = {"rank": str(i), "suite": j}
            deck.append(card)
    for i in special_cards:
        for j in cards_suite:
            card = {"rank": i, "suite": j}
            deck.append(card)
    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(swaps):
        index_i = random.randint(0, len(deck) - 1)
        index_j = random.randint(0, len(deck) - 1)
        if deck[index_i]["suite"] == "H":
            while index_j % 5 != 0 or index_i == index_j:
                index_j = random.randint(0, len(deck) - 1)
        if deck[index_i]["suite"] == "C":
            while index_j % 3 != 0 or index_i == index_j:
                index_j = random.randint(0, len(deck) - 1)
        if deck[index_i]["suite"] == "D" or index_i == index_j:
            while index_j % 2 != 0:
                index_j = random.randint(0, len(deck) - 1)
        if deck[index_i]["suite"] == "S" or index_i == index_j:
            while index_j % 7 != 0:
                index_j = random.randint(0, len(deck) - 1)
        deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
    return deck
