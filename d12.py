from collections import defaultdict


def parse_input(d):
    cavesystem = defaultdict(list)
    for line in d:
        a, b = line.strip().split("-")
        cavesystem[a].append(b)
        cavesystem[b].append(a)
    return cavesystem


def find_paths(current, visited):
    paths = 0
    for next_cave in cavesystem[current]:
        if next_cave == 'end':
            paths += 1
        elif next_cave.isupper() or next_cave not in visited:
            paths += find_paths(next_cave, visited + (next_cave, ))
    return paths


if __name__ == '__main__':
    with open("input/12.txt") as f:
        raw = f.readlines()
        cavesystem = parse_input(raw)

    print(find_paths('start', ('start', )))
