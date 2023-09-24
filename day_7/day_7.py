from collections import defaultdict


def get_dirs_sizes(inp):
    sizes = defaultdict(int)
    stack = []

    for c in inp:
        if c.startswith("$ ls") or c.startswith("dir"):
            continue
        if c.startswith("$ cd"):
            dest = c.split()[2]
            if dest == "..":
                stack.pop()
            else:
                path = f"{stack[-1]}_{dest}" if stack else dest
                stack.append(path)
        else:
            size, _ = c.split()
            for path in stack:
                sizes[path] += int(size)

    return sizes


if __name__ == "__main__":
    with open("input.txt") as f:
        inp = f.readlines()

    inp = [line.rstrip("\n") for line in inp]

    sizes = get_dirs_sizes(inp)

    needed_size = 30000000 - (70000000 - sizes["/"])
    for size in sorted(sizes.values()):
        if size > needed_size:
            break

    print(f"Puzzle 1 answer: {sum(n for n in sizes.values() if n <= 100000)}")
    print(f"Puzzle 2 answer: {size}")
