def get_lines():
    lines = []
    with open("../inputs/14.txt", "r") as f:
        for line in f:
            action, val = line.strip().split(" = ")
            if action == "mask":
                lines.append(("mask", list(val)))
            else:
                lines.append(("mem", (int(action.split("[")[1][:-1]), int(val))))

    return lines


def resolve_floating(bits):
    if "X" not in bits:
        return [bits]

    ix = bits.index("X")
    sub_0 = [b if i != ix else "0" for i, b in enumerate(bits)]
    sub_1 = [b if i != ix else "1" for i, b in enumerate(bits)]

    return resolve_floating(sub_0) + resolve_floating(sub_1)


def part1(lines):
    mask = ["0" for _ in range(36)]
    mem = {}

    for action, val in lines:
        if action == "mask":
            mask = val
        else:
            loc, n = val
            raw = list(bin(n)[2:])
            bits = ["0" for _ in range(36 - len(raw))] + raw
            for i, m in enumerate(mask):
                if m != "X":
                    bits[i] = m
            mem[loc] = int("".join(bits), 2)

    print(sum(mem.values()))


def part2(lines):
    mask = ["0" for _ in range(36)]
    mem = {}

    for action, val in lines:
        if action == "mask":
            mask = val
        else:
            raw = list(bin(val[0])[2:])
            bits = ["0" for _ in range(36 - len(raw))] + raw
            for i, m in enumerate(mask):
                if m != "0":
                    bits[i] = m

            for loc in resolve_floating(bits):
                mem[int("".join(loc), 2)] = val[1]

    print(sum(mem.values()))


LINES = get_lines()
part1(LINES)
part2(LINES)
