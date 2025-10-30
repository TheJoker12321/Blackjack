def ask_player_action() -> str:
    choose = input("Press H to hit or S to pass the turn to the dealer: ")
    while choose != "H" and choose != "S":
        print("try again")
        choose = input("Press H to continue playing or S to pass the turn to the dealer: ")
    return choose
