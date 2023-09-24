if __name__ == "__main__":
    with open("input.txt", "r") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    cal_list = []
    curr_sum = 0
    for line in inp:
        if line != "":
            curr_sum += int(line)
        elif line == "":
            cal_list.append(curr_sum)
            curr_sum = 0

    cal_list = sorted(cal_list, reverse=True)

    print(f"Puzzle 1 answer: {cal_list[0]}")
    print(f"Puzzle 2 answer: {sum(cal_list[0:3])}")
