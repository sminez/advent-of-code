FNAME = "../inputs/05.txt"


def get_pos(s, low, high, c1, c2):
    for c in s[:-1]:
        step = (high - low + 1) // 2
        if c == c1:
            high -= step
        elif c == c2:
            low += step

    return low if s[-1] == c1 else high


def get_id(s):
    row = get_pos(s[:7], 0, 127, "F", "B")
    col = get_pos(s[7:], 0, 7, "L", "R")
    return row * 8 + col


def part1(passes):
    print(max(get_id(p) for p in passes))


def part2(passes):
    ids = [get_id(p) for p in passes]
    low, high = min(ids), max(ids)
    print(set(range(low, high)).difference(ids))


PASSES = [line.strip() for line in open(FNAME, "r")]
part1(PASSES)
part2(PASSES)
