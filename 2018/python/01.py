import sys


def parse_line(line):
    sign = line[0]
    n = int(line[1:])

    if sign == "+":
        return n
    return -n


if __name__ == "__main__":
    part = 2

    with open("../inputs/01.txt", "r") as f:
        changes = [parse_line(line) for line in f]

    if part == 1:
        print(sum(changes))

    else:
        freq = 0
        seen = {0}
        iteration = 1

        while True:
            for c in changes:
                freq += c

                if freq in seen:
                    print(f"On iteration {iteration}, freq={freq} was seen for a second time")
                    sys.exit()

                seen.add(freq)

            iteration += 1
