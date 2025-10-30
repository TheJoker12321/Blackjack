from core.deck import shuffle_by_suit, build_standard_deck
from core.game_logic import run_full_game

if __name__ == "__main__":
    shuffled_deck = shuffle_by_suit(build_standard_deck())
    player = {"hand": []}
    dealer = {"hand": []}
    run_full_game(shuffled_deck, player, dealer)