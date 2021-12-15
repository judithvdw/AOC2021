from collections import defaultdict


def parse_input(raw):
    polymer = defaultdict(int)
    polymer_str = raw[0].strip()
    for i in range(len(polymer_str) - 1):
        polymer[polymer_str[i:i + 2]] += 1

    rules = {}
    for line in raw[2:]:
        k, v = line.strip().split(" -> ")
        rules[k] = v
    return polymer, rules, polymer_str[-1]


def grow_polymer(polymer, rules):
    new_polymer = defaultdict(int)
    for pair, num in polymer.items():
        insert = rules[pair]
        new_polymer[pair[0] + insert] += num
        new_polymer[insert + pair[1]] += num
    return new_polymer


def elemental_decomposition(polymer):
    decomposed = defaultdict(int)
    for k, v in polymer.items():
        decomposed[k[0]] += v
    return decomposed


def run(polymer, rules, last, i):
    for _ in range(i):
        polymer = grow_polymer(polymer, rules)

    decomposed = elemental_decomposition(polymer)
    decomposed[last] += 1
    return max(decomposed.values()) - min(decomposed.values())


if __name__ == '__main__':
    with open("input/14.txt") as f:
        raw = f.readlines()
        polymer, rules, last = parse_input(raw)

    print(f"Part 1: {run(polymer, rules, last, 10)}")
    print(f"Part 2: {run(polymer, rules, last, 40)}")
