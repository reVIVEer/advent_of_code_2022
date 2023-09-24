def get_puzzle1_answer(pairs):
    n_fully_overlapping_pairs = 0

    for pair in pairs:
        range1, range2 = pair.split(",")
        r1_begin, r1_end = [int(i) for i in range1.split("-")]
        r2_begin, r2_end = [int(i) for i in range2.split("-")]

        r1_set = set([i for i in range(r1_begin, r1_end + 1)])
        r2_set = set([i for i in range(r2_begin, r2_end + 1)])
        overlapping_sections = r1_set.intersection(r2_set)

        if overlapping_sections == r1_set or overlapping_sections == r2_set:
            n_fully_overlapping_pairs += 1

    return n_fully_overlapping_pairs


def get_puzzle2_answer(pairs):
    n_any_overlapping_pairs = 0

    for pair in pairs:
        range1, range2 = pair.split(",")
        r1_begin, r1_end = [int(i) for i in range1.split("-")]
        r2_begin, r2_end = [int(i) for i in range2.split("-")]

        r1_set = set([i for i in range(r1_begin, r1_end + 1)])
        r2_set = set([i for i in range(r2_begin, r2_end + 1)])
        overlapping_sections = r1_set.intersection(r2_set)

        if len(overlapping_sections) != 0:
            n_any_overlapping_pairs += 1

    return n_any_overlapping_pairs


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    print(f"Puzzle 1 answer: {get_puzzle1_answer(inp)}")
    print(f"Puzzle 2 answer: {get_puzzle2_answer(inp)}")
