from statistics import median


def find_illegal_or_leftover(line):
    mapping = {"}": "{", ")": "(", ">": "<", "]": "["}
    opened = ""
    for char in line:
        if char not in mapping:  # and thus an opening char
            opened += char
        else:
            if mapping[char] == opened[-1]:
                opened = opened[:-1]
            else:
                return char
    return opened


def calc_scores(line):
    points_pt2 = {"{": 3, "(": 1, "<": 4, "[": 2}
    total = 0
    for char in line[::-1]:
        total *= 5
        total += points_pt2[char]
    return total


if __name__ == '__main__':
    with open("input/10.txt") as f:
        data = [i.strip() for i in f.readlines()]

    points = {"}": 1197, ")": 3, ">": 25137, "]": 57}

    illegal_or_leftover = [find_illegal_or_leftover(line) for line in data]
    print(f"Part 1: {sum(points[i] for i in illegal_or_leftover if i in points)}")

    leftover = [i for i in illegal_or_leftover if i not in points]
    print(f"Part 2: {median([calc_scores(i) for i in leftover])}")
