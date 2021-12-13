def parse_input(raw):
    raw_dots, raw_instructions = raw.split("\n\n")

    dots = set()
    for dot in raw_dots.split("\n"):
        x, y = dot.split(',')
        dots.add((int(x), int(y)))

    instructions = []
    for instruction in raw_instructions.split("\n"):
        axis, line = instruction.split(" ")[2].split("=")
        instructions.append((axis, int(line)))

    return dots, instructions


def fold(instruction, dots):
    axis = instruction[0]
    line = instruction[1]
    new_locations = set()
    for dot in dots:
        if axis == "x":
            if dot[0] > line:
                new_dot = (line * 2 - dot[0], dot[1])
                new_locations.add(new_dot)
            else:
                new_locations.add(dot)
        elif axis == "y":
            if dot[1] > line:
                new_dot = (dot[0], line * 2 - dot[1])
                new_locations.add(new_dot)
            else:
                new_locations.add(dot)
    return new_locations


def print_code(dots):
    x_max = max([i[0] for i in dots]) + 1
    y_max = max([i[1] for i in dots]) + 1
    t = [[" "] * x_max for i in range(y_max)]
    for x, y in dots:
        t[y][x] = "\u2588"
    for line in t:
        print("".join([str(i) for i in line]))


if __name__ == '__main__':
    with open("input/13.txt") as f:
        raw = f.read()
        dots, instructions = parse_input(raw)

    print(f"Part 1: {len(fold(instructions[0], dots))}")

    for instruction in instructions:
        dots = fold(instruction, dots)

    print(f"Part 2:")
    print_code(dots)
