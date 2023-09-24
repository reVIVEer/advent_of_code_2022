import math


def get_init_monkey_config(inp):
    init_config = []

    for i, line in enumerate(inp):
        if line.startswith("Monkey"):
            monkey_id = int(line[-2])
            starting_items = [
                int(x.strip()) for x in inp[i + 1].split(":")[1].split(",")
            ]
            operation_items = inp[i + 2].split("= ")[1].split(" ")
            operation = {
                "operand1": operation_items[0],
                "operator": operation_items[1],
                "operand2": operation_items[2],
            }
            test = {
                "test_div_by": int(inp[i + 3].split()[-1]),
                "test_true_monkey_id": int(inp[i + 4][-1]),
                "test_false_monkey_id": int(inp[i + 5][-1]),
            }

            monkey_config = {
                "monkey_id": monkey_id,
                "starting_items": starting_items,
                "operation": operation,
                "test": test,
            }

            init_config.append(monkey_config)

    return init_config


def get_num_inspections(inp, n_rounds):
    init_config = get_init_monkey_config(inp)
    n_inspections = [0] * len(init_config)

    for _ in range(n_rounds):
        for m_config in init_config:
            monkey_id = m_config["monkey_id"]
            operand1 = m_config["operation"]["operand1"]
            operator = m_config["operation"]["operator"]
            operand2 = m_config["operation"]["operand2"]
            test_div_by = m_config["test"]["test_div_by"]
            test_true_monkey_id = m_config["test"]["test_true_monkey_id"]
            test_false_monkey_id = m_config["test"]["test_false_monkey_id"]

            for wl in m_config["starting_items"]:
                x = wl if operand1 == "old" else int(operand1)
                y = wl if operand2 == "old" else int(operand2)
                z = x * y if operator == "*" else x + y

                # Check if part_1 or part_2 using number of rounds
                # In else block, the hardcoded value is just the product of all the test divisors
                z = math.floor(z / 3) if n_rounds == 20 else z % 9699690

                if z % test_div_by == 0:
                    init_config[test_true_monkey_id]["starting_items"].append(z)
                else:
                    init_config[test_false_monkey_id]["starting_items"].append(z)

                n_inspections[monkey_id] += 1

            m_config["starting_items"].clear()

    # get the 2 most active monkeys
    n_inspections = sorted(n_inspections, reverse=True)
    two_most_active_monkeys = n_inspections[0] * n_inspections[1]

    return two_most_active_monkeys


if __name__ == "__main__":
    with open("input.txt") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    print(f"Puzzle 1 answer: {get_num_inspections(inp, 20)}")
    print(f"Puzzle 2 answer: {get_num_inspections(inp, 10000)}")
