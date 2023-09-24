def get_total_priority_puzzle1(rucksacks):
    total_priority = 0

    for rucksack in rucksacks:
        first_half, second_half = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )
        common_alpha = list(set(first_half).intersection(set(second_half)))[0]
        total_priority += priority_map[common_alpha]

    return total_priority


def get_total_priority_puzzle2(rucksacks):
    total_priority = 0

    for i, _ in enumerate(rucksacks):
        if i % 3 == 0:
            first = set(rucksacks[i])
            second = set(rucksacks[i + 1])
            third = set(rucksacks[i + 2])

            common_alpha = list(first.intersection(second).intersection(third))[0]
            total_priority += priority_map[common_alpha]

    return total_priority


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.readlines()

    rucksacks = [line.rstrip("\n") for line in inp]

    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority_map = {
        alphabet: (priority + 1)
        for priority, alphabet in enumerate(alpha_lower + alpha_upper)
    }

    print(f"Puzzle 1 answer: {get_total_priority_puzzle1(rucksacks)}")
    print(f"Puzzle 1 answer: {get_total_priority_puzzle2(rucksacks)}")
