from collections import Counter

def parse_input(raw):
    polymer = raw[0].strip()
    rules = {}
    for line in raw[2:]:
        k, v = line.strip().split(" -> ")
        rules[k] = v
    return polymer, rules

def grow_polymer(polymer):
    new_polymer = ""
    for i in range(len(polymer) -1):
        pair = polymer[i:i+2]
        insert = rules[pair]
        new_polymer += polymer[i] + insert
    new_polymer += polymer[-1]
    return new_polymer


if __name__ == '__main__':
    with open("input/14.txt") as f:
        raw = f.readlines()
        polymer, rules = parse_input(raw)
        print(polymer, rules)

    print(len(polymer))
    for i in range(20):
        polymer = grow_polymer(polymer)
        c = Counter(polymer)
        print(i, c.most_common())
