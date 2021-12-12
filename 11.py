def get_map(raw):
    d = {}
    for i, line in enumerate(raw):
        for j, num in enumerate(line.strip()):
            d[(i, j)] = int(num)
    return d


def increment_neighbours(nine, dmap):
    x, y = nine
    neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]
    actual_neighbours = [option for option in neighbours if option in dmap]
    for neighbour in actual_neighbours:
        if dmap[neighbour] != 0:
            dmap[neighbour] += 1
    return dmap


def do_step(dmap):
    dmap = {k: v + 1 for k, v in dmap.items()}
    flashes = 0
    nines = [k for k, v in dmap.items() if v > 9]
    while len(nines) > 0:
        for nine in nines:
            flashes += 1
            dmap[nine] = 0
            dmap = increment_neighbours(nine, dmap)
        nines = [k for k, v in dmap.items() if v > 9]
    return dmap, flashes


with open('input/11.txt') as f:
    raw = f.readlines()
    dumbo_map = get_map(raw)
    STEPS = 1000
    flashes = 0
    for i in range(1, STEPS):
        dumbo_map, flashed = do_step(dumbo_map)
        flashes += flashed
        if flashed == 100:
            print(f"part 2: {i}")
            break
        if i == 100:
            print(f"Part 1: {flashes}")
