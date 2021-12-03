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


def get_power_consumption(report):
    gamma = gamma_rate(report)
    print(gamma)
    epsilon = epsilon_rate(gamma)
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    with open("3.txt") as f:
        binary = f.readlines()
        binary = [[int(i) for i in b.strip()] for b in binary]

test = "111100100011"
print(get_power_consumption(binary))