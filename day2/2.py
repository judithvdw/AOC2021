def part1(instructions):
    depth = 0
    forward = 0
    for direction, n in instructions:
        n = int(n)
        if direction == "forward":
            forward += n
        if direction == "up":
            depth -= n
        if direction == "down":
            depth += n
    return depth * forward


def part2(instructions):
    depth = 0
    forward = 0
    aim = 0
    for direction, n in instructions:
        n = int(n)
        if direction == "forward":
            forward += n
            depth += aim * n
        if direction == "up":
            aim -= n
        if direction == "down":
            aim += n

    return depth * forward


if __name__ == '__main__':
    with open("2.txt") as f:
        raw = f.readlines()
        instructions = [a.split() for a in raw]

    print(f"part 1: {part1(instructions)}")
    print(f"part 2: {part2(instructions)}")