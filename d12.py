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
            paths += find_paths(next_cave, visited + (next_cave,))
    return paths


def find_paths_pt2(current, visited):
    paths = 0
    for next_cave in cavesystem[current]:
        if next_cave == 'start':
            continue
        elif next_cave == 'end':
            paths += 1
        elif next_cave.isupper() or next_cave not in visited or len([i for i in visited if i.islower()]) == len(
                set([i for i in visited if i.islower()])):
            paths += find_paths_pt2(next_cave, visited + (next_cave,))
    return paths


if __name__ == '__main__':
    with open("input/12.txt") as f:
        raw = f.readlines()
        cavesystem = parse_input(raw)

    print(f"Part 1: {find_paths('start', ('start',))}")
    print(f"Part 2: {find_paths_pt2('start', ('start',))}")
