from collections import Counter

def parse_cord(cord):
    x,y = cord.split(",")
    return int(x), int(y)

def parse_input(data):
    cords = []
    for line in data:
        a, b = line.split(" -> ")
        cords.append([parse_cord(a), parse_cord(b)])
    return cords

def check_straight(cord):
    return cord[0][0] == cord[1][0] or cord[0][1] == cord[1][1]

def get_points(cord_pair):
    cords = []
    for i in range(cord_pair[0][0], cord_pair[1][0]+1):
        for j in range(cord_pair[0][1], cord_pair[1][1]+1):
            cords.append((i,j))

    for i in range(cord_pair[1][0], cord_pair[0][0]+1):
        for j in range(cord_pair[1][1], cord_pair[0][1]+1):
            cords.append((i,j))
    return list(set(cords))

def get_diagonal_cords(cords):
    pass




def get_straight_cords(cords):
    straight_cords = []
    for cord in cords:
        print(cord, check_straight(cord))
        if check_straight(cord):
            straight_cords.append(cord)
    return straight_cords

def part1(cords):
    all_points = []
    straight_cords = get_straight_cords(cords)
    for cord in straight_cords:
        all_points.extend(get_points(cord))

    total = 0
    c = Counter(all_points)
    for count in c:
        if c[count] > 1:
            total += 1

    return total

if __name__ == '__main__':
    with open("test.txt") as f:
        raw = f.readlines()

    cords = parse_input(raw)

    print(f"part 1: {part1(cords)}")

