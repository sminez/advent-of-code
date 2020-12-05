FNAME = "../inputs/01.txt"


def get_compliments(values, target):
    return [target - val for val in values]


def part1(values):
    compliments = get_compliments(values, 2020)
    a, b = set(values).intersection(compliments)
    print(f"{a} x {b} = {a * b}")


def part2(values):
    for a in values:
        compliments = get_compliments(values, 2020 - a)
        possible_match = set(values).intersection(compliments)
        if possible_match:
            b, c = possible_match
            print(f"{a} x {b} x {c} = {a * b * c}")
            return


VALUES = [int(line.strip()) for line in open(FNAME, "r")]
part1(VALUES)
part2(VALUES)
