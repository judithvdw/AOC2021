def larger_measurements(window):
    i = 1
    total = 0
    for _ in data[1:len(data) - window + 1]:
        if sum(data[i:i + window]) > sum(data[i - 1:i - 1 + window]):
            total += 1
        i += 1
    return total


if __name__ == '__main__':
    with open('input/1.txt') as f:
        data = f.readlines()
        data = [int(x) for x in data]

        print(f"part 1: {larger_measurements(1)}")
        print(f"part 2: {larger_measurements(3)}")
