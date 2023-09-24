def get_puzzle1_answer(inp):
    X = 1
    cycles_completed = 0
    nth_cycles = [20, 60, 100, 140, 180, 220]
    nth_cycles_signal_strengths = []

    for inst in inp:
        if inst[:4] == "noop":
            cycles_completed += 1
            if cycles_completed in nth_cycles:
                nth_cycles_signal_strengths.append(cycles_completed * X)
        else:
            for c in range(2):
                cycles_completed += 1
                if cycles_completed in nth_cycles:
                    nth_cycles_signal_strengths.append(cycles_completed * X)
            V = int(inst[5:])
            X += V

    return sum(nth_cycles_signal_strengths)


def get_puzzle2_answer(inp):
    X = [0, 1, 2]
    cycles_completed = 0
    crt_grid = ["."] * (40 * 6)

    for inst in inp:
        if inst[:4] == "noop":
            if cycles_completed % 40 in X:
                crt_grid[cycles_completed] = "#"
            cycles_completed += 1
        else:
            for c in range(2):
                if cycles_completed % 40 in X:
                    crt_grid[cycles_completed] = "#"
                cycles_completed += 1
            V = int(inst[5:])
            X = [x + V for x in X]

    crt_grid_but_better = [crt_grid[i : i + 40] for i in range(0, len(crt_grid), 40)]

    return crt_grid_but_better


if __name__ == "__main__":
    with open("input.txt") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    print(f"Puzzle 1 answer: {get_puzzle1_answer(inp)}")
    print("Puzzle 2 answer:")
    crt_grid = get_puzzle2_answer(inp)
    # render CRT grid and infer answer from it
    for row in crt_grid:
        print(" ".join(row))
