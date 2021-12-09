from collections import Counter


def parse_cord(cord):
    x, y = cord.split(",")
    return int(x), int(y)


def parse_input(data):
    cords = []
    for line in data:
        a, b = line.split(" -> ")
        cords.append([parse_cord(a), parse_cord(b)])
    return cords


def check_straight(cord):
    return cord[0][0] == cord[1][0] or cord[0][1] == cord[1][1]


# @todo: make less ugly
def get_points(cord_pair):
    points = []
    for i in range(cord_pair[0][0], cord_pair[1][0] + 1):
        for j in range(cord_pair[0][1], cord_pair[1][1] + 1):
            points.append((i, j))

    for i in range(cord_pair[1][0], cord_pair[0][0] + 1):
        for j in range(cord_pair[1][1], cord_pair[0][1] + 1):
            points.append((i, j))
    return list(set(points))


def get_diagonal_points(cords):
    if cords[0][0] < cords[1][0]:
        xs = [i for i in range(cords[0][0], cords[1][0] + 1)]
    else:
        xs = [i for i in range(cords[1][0], cords[0][0] + 1)][::-1]
    if cords[0][1] < cords[1][1]:
        ys = [i for i in range(cords[0][1], cords[1][1] + 1)]
    else:
        ys = [i for i in range(cords[1][1], cords[0][1] + 1)][::-1]
    points = list(zip(xs, ys))
    return points


def get_cord_types(cords):
    straight_cords = []
    diagonal_cords = []
    for cord in cords:
        if check_straight(cord):
            straight_cords.append(cord)
        else:
            diagonal_cords.append(cord)
    return diagonal_cords, straight_cords


def part1(cords):
    all_points = []
    diagonal_cords, straight_cords = get_cord_types(cords)
    for cord in straight_cords:
        all_points.extend(get_points(cord))

    total = 0
    c = Counter(all_points)
    for count in c:
        if c[count] > 1:
            total += 1

    return total


def part2(cords):
    all_points = []
    diagonal_cords, straight_cords = get_cord_types(cords)
    for cord in straight_cords:
        all_points.extend(get_points(cord))

    for c in diagonal_cords:
        all_points.extend(get_diagonal_points(c))

    total = 0
    c = Counter(all_points)
    for count in c:
        if c[count] > 1:
            total += 1

    return total


if __name__ == '__main__':
    with open("input/5.txt") as f:
        raw = f.readlines()

    cords = parse_input(raw)

    print(f"part 1: {part1(cords)}")
    print(f"part 2: {part2(cords)}")
