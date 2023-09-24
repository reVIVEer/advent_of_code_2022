def is_touching(head_coords, tail_coords):
    if (
        abs(head_coords["row"] - tail_coords["row"]) <= 1
        and abs(head_coords["column"] - tail_coords["column"]) <= 1
    ):
        return True
    else:
        return False


def get_tail_journey_distance(inp, n_knots):
    knots_pos = [{"row": 1, "column": 1} for i in range(n_knots)]
    knots_journey = [
        [(knots_pos[i]["row"], knots_pos[i]["column"])] for i in range(n_knots)
    ]

    for step in inp:
        dir, dist = step[0], int(step[2:])

        for i in range(dist):
            for j in range(n_knots):
                if j == 0:
                    if dir == "R":
                        knots_pos[j]["column"] += 1
                    elif dir == "L":
                        knots_pos[j]["column"] -= 1
                    elif dir == "U":
                        knots_pos[j]["row"] += 1
                    elif dir == "D":
                        knots_pos[j]["row"] -= 1
                else:
                    head = knots_pos[j - 1]
                    tail = knots_pos[j]

                    if is_touching(head, tail) is False:
                        if tail["row"] == head["row"]:
                            if tail["column"] < head["column"]:
                                tail["column"] += 1
                            elif tail["column"] > head["column"]:
                                tail["column"] -= 1
                        elif tail["column"] == head["column"]:
                            if tail["row"] < head["row"]:
                                tail["row"] += 1
                            elif tail["row"] > head["row"]:
                                tail["row"] -= 1
                        elif (tail["row"] != head["row"]) and (
                            tail["column"] != head["column"]
                        ):
                            if (tail["row"] < head["row"]) and (
                                tail["column"] < head["column"]
                            ):
                                tail["row"] += 1
                                tail["column"] += 1
                            elif (tail["row"] < head["row"]) and (
                                tail["column"] > head["column"]
                            ):
                                tail["row"] += 1
                                tail["column"] -= 1
                            elif (tail["row"] > head["row"]) and (
                                tail["column"] < head["column"]
                            ):
                                tail["row"] -= 1
                                tail["column"] += 1
                            elif (tail["row"] > head["row"]) and (
                                tail["column"] > head["column"]
                            ):
                                tail["row"] -= 1
                                tail["column"] -= 1

                knots_journey[j].append((knots_pos[j]["row"], knots_pos[j]["column"]))

    return len(set(knots_journey[-1]))


if __name__ == "__main__":
    with open("input.txt") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    print(f"Puzzle 1 answer: {get_tail_journey_distance(inp, n_knots=2)}")
    print(f"Puzzle 2 answer: {get_tail_journey_distance(inp, n_knots=10)}")
