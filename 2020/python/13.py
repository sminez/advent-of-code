FNAME = "../inputs/13.txt"
TEST = """939
7,13,x,x,59,x,31,19"""


def mul_inv(a, b):
    if b == 1:
        return 1
    b0, m, n = b, 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        m, n = n - q * m, m
    return n + b0 if n < 0 else n


def part1(seed, times):
    valid = [int(t) for t in times if t != "x"]
    fst = valid[0]
    bus_id, min_wait = fst, fst - seed % fst
    for v in valid[1:]:
        wait = v - seed % v
        if wait < min_wait:
            bus_id, min_wait = v, wait

    print(bus_id, min_wait, bus_id * min_wait)


def part2(times):
    # chinese remainder theorem
    total = 0
    prod = 1
    offsets = []
    for k, t in enumerate(times):
        if t == "x":
            continue
        t = int(t)
        prod *= t
        offsets.append((t, k))

    print(prod, offsets)
    for t, k in offsets:
        p = prod // t
        total += p * k * mul_inv(p, t)

    print(total % prod)


LINES = [line.strip() for line in open(FNAME, "r")]
# LINES = TEST.split()
SEED = int(LINES[0])
TIMES = LINES[1].split(",")
part1(SEED, TIMES)
part2(TIMES)
# part2("17,x,13,19".split(","))
# part2("67,7,59,61".split(","))
# part2("67,x,7,59,61".split(","))
# part2("67,7,x,59,61".split(","))
# part2("1789,37,47,1889".split(","))
