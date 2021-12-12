from collections import OrderedDict, Counter
from math import prod


def low_point(cord, heightmap):
    x, y = cord
    all_options = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    actual_options = [option for option in all_options if option in heightmap]
    for option in actual_options:
        if heightmap[option] <= heightmap[cord]:
            return False
    return True


def get_low_points(heightmap):
    low_points = {}
    for cord, n in heightmap.items():
        if n == 0 or low_point(cord, heightmap):
            low_points[cord] = n
    return low_points


def get_map(raw):
    d = {}
    for i, line in enumerate(raw):
        for j, num in enumerate(line.strip()):
            d[(i, j)] = int(num)
    return d


def part_2(heightmap, low):
    ordered_heightmap = OrderedDict(sorted(heightmap.items(), key=lambda x: x[1]))
    basin_mapping = {k: k for k, v in low.items()}

    for k, v in ordered_heightmap.items():
        if k in basin_mapping:
            continue
        elif v == 9:
            break
        else:
            x, y = k
            all_options = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            actual_options = {option: heightmap[option] for option in all_options if option in heightmap}
            small = min(actual_options, key=actual_options.get)
            basin_mapping[k] = basin_mapping[small]

    c = Counter(basin_mapping.values())

    return prod(sorted(dict(c).values(), reverse=True)[:3])


if __name__ == '__main__':
    with open('input/9.txt') as f:
        raw = f.readlines()
        heightmap = get_map(raw)

    low = get_low_points(heightmap)
    print(f"Part 1: {sum(low.values()) + len(low)}")
    print(f"Part 2: {part_2(heightmap, low)}")
