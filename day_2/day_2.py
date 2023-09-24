def get_round_score_puzzle1(opp_move, our_move):
    round_score = 0

    # check shape
    if our_move == "X":
        round_score += 1
    elif our_move == "Y":
        round_score += 2
    elif our_move == "Z":
        round_score += 3

    # check draw or win
    if (
        (our_move == "X" and opp_move == "A")
        or (our_move == "Y" and opp_move == "B")
        or (our_move == "Z" and opp_move == "C")
    ):
        round_score += 3
    elif (
        (our_move == "X" and opp_move == "C")
        or (our_move == "Y" and opp_move == "A")
        or (our_move == "Z" and opp_move == "B")
    ):
        round_score += 6

    return round_score


def get_round_score_puzzle2(opp_move, our_move):
    round_score = 0
    lose_map = {
        "A": {"move": "Z", "value": 3},
        "B": {"move": "X", "value": 1},
        "C": {"move": "Y", "value": 2},
    }
    draw_map = {
        "A": {"move": "X", "value": 1},
        "B": {"move": "Y", "value": 2},
        "C": {"move": "Z", "value": 3},
    }
    win_map = {
        "A": {"move": "Y", "value": 2},
        "B": {"move": "Z", "value": 3},
        "C": {"move": "X", "value": 1},
    }

    # check round rule and use appropriate shape value
    if our_move == "X":
        round_score += 0
        round_score += lose_map[opp_move]["value"]
    elif our_move == "Y":
        round_score += 3
        round_score += draw_map[opp_move]["value"]
    elif our_move == "Z":
        round_score += 6
        round_score += win_map[opp_move]["value"]

    return round_score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    total_score_puzzle1 = 0
    total_score_puzzle2 = 0

    for round in inp:
        opp_move = round[0]
        our_move = round[2]

        total_score_puzzle1 += get_round_score_puzzle1(opp_move, our_move)
        total_score_puzzle2 += get_round_score_puzzle2(opp_move, our_move)

    print(f"Puzzle 1 answer: {total_score_puzzle1}")
    print(f"Puzzle 2 answer: {total_score_puzzle2}")
