def get_cleaned_input(inp):
    stacks_config, steps = inp[: inp.index("") - 1], inp[inp.index("") + 1 :]

    stacks_config_alt = []
    for row in stacks_config:
        stacks_config_alt.append([row[i : i + 3] for i in range(0, len(row), 4)])

    transposed = [list(x) for x in zip(*stacks_config_alt)]
    cleaned_sc = [[j for j in i if j.isspace() == False] for i in transposed]
    cleaned_sc = [stack[::-1] for stack in cleaned_sc]

    return cleaned_sc, steps


def get_puzzle1_answer(inp):
    stacks_config, steps = get_cleaned_input(inp)

    for step in steps:
        n_crates_to_move, from_stack, to_stack = list(map(int, step.split()[1::2]))

        for i in range(n_crates_to_move):
            stacks_config[to_stack - 1].append(stacks_config[from_stack - 1].pop())

    crates_on_top = ""
    for i in stacks_config:
        crates_on_top += i[-1][1]

    return crates_on_top


def get_puzzle2_answer(inp):
    stacks_config, steps = get_cleaned_input(inp)

    for step in steps:
        n_crates_to_move, from_stack, to_stack = list(map(int, step.split()[1::2]))
        stacks_config[to_stack - 1].extend(
            stacks_config[from_stack - 1][-n_crates_to_move:]
        )
        del stacks_config[from_stack - 1][-n_crates_to_move:]

    crates_on_top = ""
    for i in stacks_config:
        crates_on_top += i[-1][1]

    return crates_on_top


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    print(f"Puzzle 1 answer: {get_puzzle1_answer(inp)}")
    print(f"Puzzle 2 answer: {get_puzzle2_answer(inp)}")
