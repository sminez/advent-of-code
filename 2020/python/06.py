FNAME = "../inputs/06.txt"


def part1(groups):
    print(sum(len(set("".join(g))) for g in groups))


def part2(groups):
    total = 0

    for g in groups:
        shared = set(g[0])
        for other in g[1:]:
            shared = shared.intersection(other)
        total += len(shared)

    print(total)


GROUPS = [g.split() for g in open(FNAME, "r").read().split("\n\n")]
part1(GROUPS)
part2(GROUPS)
