from core.deck import build_standard_deck, shuffle_by_suit
from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:
    count_hand = 0
    for i in hand:
        if i["rank"] == "A":
            count_hand += 1
        elif i["rank"] == "K" or i["rank"] == "Q" or i["rank"] == "J":
            count_hand += 10
        else:
            count_hand += int(i["rank"])

    return count_hand


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(4):
        if i >= 2:
            dealer["hand"].append(deck.pop(i))
        else:
            player["hand"].append(deck.pop(i))
    print(f"value of player: {calculate_hand_value(player["hand"])}")
    print(f"value of dealer: {calculate_hand_value(dealer["hand"])}")

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) < 17:
        dealer["hand"].append(deck.pop(0))
    if calculate_hand_value(dealer["hand"]) > 21:
        print("There is a disqualification")
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while calculate_hand_value(player["hand"]) <= 21:
        choose_player = ask_player_action()
        if choose_player == "H":
            player["hand"].append(deck.pop(0))
        else:
            break
    if calculate_hand_value(player["hand"]) > 21:
        print("player lose!")
    else:
        status_dealer = dealer_play(deck, dealer)
        if not status_dealer:
            print(f"dealer lose! and his value {calculate_hand_value(dealer["hand"])}")
        else:
            value_of_dealer = calculate_hand_value(dealer["hand"])
            value_of_player = calculate_hand_value(player["hand"])
            if value_of_dealer > value_of_player:
                print(f"dealer won and his value {value_of_dealer}")
            elif value_of_player > value_of_dealer:
                print(f"player won and his value {value_of_player}")
            else:
                print("the result is pass!!")




