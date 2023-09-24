import math


def get_puzzle_answers(inp):
    visible_trees = 0
    scenic_scores = []

    for trees_idx, trees in enumerate(inp):
        for tree_idx, tree in enumerate(trees):
            if (
                tree_idx == 0
                or trees_idx == 0
                or tree_idx == len(trees) - 1
                or trees_idx == len(inp) - 1
            ):
                visible_trees += 1
                continue

            up = [int(inp[i][tree_idx]) for i in range(trees_idx)]
            up.reverse()
            down = [
                int(inp[i][tree_idx])
                for i in range(trees_idx, len(inp))
                if i != trees_idx
            ]
            left = [int(inp[trees_idx][i]) for i in range(tree_idx)]
            left.reverse()
            right = [
                int(inp[trees_idx][i])
                for i in range(tree_idx, len(trees))
                if i != tree_idx
            ]

            if (
                int(tree) > max(up)
                or int(tree) > max(down)
                or int(tree) > max(left)
                or int(tree) > max(right)
            ):
                visible_trees += 1

            tree_scenic_score = []
            directions = [up, down, left, right]
            for dir in directions:
                dir_sum = 0
                for t in dir:
                    if int(tree) > t:
                        dir_sum += 1
                    elif int(tree) <= t:
                        dir_sum += 1
                        break
                tree_scenic_score.append(dir_sum)

            scenic_scores.append(math.prod(tree_scenic_score))

    return visible_trees, scenic_scores


if __name__ == "__main__":
    with open("input.txt") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    visible_trees, scenic_scores = get_puzzle_answers(inp)

    print(f"Puzzle 1 answer: {visible_trees}")
    print(f"Puzzle 2 answer: {max(scenic_scores)}")
