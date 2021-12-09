def gamma_rate(report):
    sums = [sum(i) for i in zip(*report)]
    bin = ""
    for s in sums:
        if s > len(report) // 2:
            bin += "1"
        else:
            bin += "0"
    return bin


def epsilon_rate(gamma_rate):
    return "".join([str(int(not bool(int(a)))) for a in gamma_rate])


def oxigen_generator_rating(report):
    bit_position = 0
    while len(report) > 1:
        total = sum(list(zip(*report))[bit_position])
        if total >= len(report) - total:
            report = [r for r in report if r[bit_position] == 1]
        else:
            report = [r for r in report if r[bit_position] == 0]
        bit_position += 1
    return int("".join([str(a) for a in report[0]]), 2)


def co2_scrubber_rating(report):
    bit_position = 0
    while len(report) > 1:
        total = sum(list(zip(*report))[bit_position])
        if total < len(report) - total:
            report = [r for r in report if r[bit_position] == 1]
        else:
            report = [r for r in report if r[bit_position] == 0]
        bit_position += 1
    return int("".join([str(a) for a in report[0]]), 2)


def get_power_consumption(report):
    gamma = gamma_rate(report)
    epsilon = epsilon_rate(gamma)
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    with open("input/3.txt") as f:
        binary = f.readlines()
        binary = [[int(i) for i in b.strip()] for b in binary]

print(f"part 1: {get_power_consumption(binary)}")
print(f"part 2: {oxigen_generator_rating(binary) * co2_scrubber_rating(binary)}")
