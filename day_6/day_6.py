def get_puzzle_answer(inp, msg_len):
    for i, _ in enumerate(inp):
        tmp = [*inp][i - msg_len : i]
        curr_message = set(tmp)

        if len(curr_message) == msg_len:
            return i


if __name__ == "__main__":
    with open("input.txt") as f:
        inp = f.read()

    print(f"Puzzle 1 answer: {get_puzzle_answer(inp, msg_len=4)}")
    print(f"Puzzle 2 answer: {get_puzzle_answer(inp, msg_len=14)}")
