FNAME = "../inputs/02.txt"


def is_valid_for_1(line):
    min_max, char, password = line.replace(":", "").split(" ")
    c_min, c_max = [int(s) for s in min_max.split("-")]
    count = password.count(char)

    return c_min <= count <= c_max


def is_valid_for_2(line):
    n_m, char, password = line.replace(":", "").split(" ")
    n, m = [int(s) for s in n_m.split("-")]
    # indices are 1-based
    c1, c2 = password[n - 1], password[m - 1]

    return (c1 == char) ^ (c2 == char)


def part1(values):
    print(len([line for line in values if is_valid_for_1(line)]))


def part2(values):
    print(len([line for line in values if is_valid_for_2(line)]))


VALUES = [line.strip() for line in open(FNAME, "r")]
part1(VALUES)
part2(VALUES)
