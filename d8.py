def parse_data_part_1(data):
    bs = []
    for d in data:
        a, b = d.strip().split(" | ")
        bs.extend(b.split())
    return bs


def part_1(bs):
    total = 0
    for a in bs:
        if len(a) in (2, 3, 4, 7):
            total += 1
    return total


def parse_data(data):
    parsed = []
    for d in data:
        a, b = d.strip().split(" | ")
        parsed.append((a.split(), b.split()))
    return parsed


def get_3(options, one):
    options = [set(list(i)) for i in options]
    one = set(list(one))
    for option in options:
        if len(option & one) == 2:
            return "".join(option)


def get_9_6_0(options, three, one):
    options = [set(list(i)) for i in options]
    three = set(list(three))
    one = set(list(one))
    nine = ""
    six = ""
    zero = ""
    for option in options:
        if len(option & three) == 5:
            nine = "".join(option)
        elif len(option & one) == 2:
            zero = "".join(option)
        else:
            six = "".join(option)
    return nine, six, zero


def get_2_5(options, six, three):
    options = [set(list(i)) for i in options]
    six = set(list(six))
    two = ""
    five = ""
    for option in options:
        if len(option & six) == 5:
            five = "".join(option)
        elif len(option & six) == 4 and "".join(option) != three:
            two = "".join(option)
        else:
            continue
    return two, five


def get_mapping(d):
    sorted_patterns = sorted(d, key=len)
    mapping = {i: "" for i in range(10)}

    # set the easy ones:
    mapping[1] = sorted_patterns[0]
    mapping[7] = sorted_patterns[1]
    mapping[4] = sorted_patterns[2]
    mapping[8] = sorted_patterns[9]

    # others
    mapping[3] = get_3(sorted_patterns[3:6], mapping[1])
    mapping[9], mapping[6], mapping[0] = get_9_6_0(sorted_patterns[6:9], mapping[3], mapping[1])
    mapping[2], mapping[5] = get_2_5(sorted_patterns[3:6], mapping[6], mapping[3])

    flipped_mapping = {"".join(sorted(list(y))): x for x, y in mapping.items()}
    return flipped_mapping


def get_number(mapping, display):
    number_display = ""
    for number in display:
        ordered_number = "".join(sorted(list(number)))
        number_display += str(mapping[ordered_number])
    return int(number_display)


if __name__ == '__main__':

    with open("input/8.txt") as f:
        raw = f.readlines()

        bs = parse_data_part_1(raw)
        print(f"Part 1: {part_1(bs)}")

        data = parse_data(raw)
        mappings = []
        displays = []
        for d in data:
            mappings.append(get_mapping(d[0]))
            displays.append(d[1])

        total = 0
        for mapping, display in zip(mappings, displays):
            total += get_number(mapping, display)
        print(f"Part 2: {total}")
