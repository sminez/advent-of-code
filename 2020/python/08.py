FNAME = "../inputs/08.txt"


def run(prog):
    acc = ptr = 0
    seen = set()

    while ptr < len(prog):
        if ptr in seen:
            return "LOOP", acc

        opp, arg = prog[ptr]
        seen.add(ptr)

        if opp == "nop":
            ptr += 1
        elif opp == "acc":
            acc += int(arg)
            ptr += 1
        elif opp == "jmp":
            ptr += int(arg)

    return "BOOT", acc


def part1(prog):
    print(run(prog))


def part2(prog):
    for i in range(len(prog)):
        if prog[i][0] != "acc":
            cpy = [[v for v in p] for p in prog]
            cpy[i][0] = "nop" if cpy[i][0] == "jmp" else "jmp"

            state, acc = run(cpy)
            if state == "BOOT":
                print(i, prog[i])
                print(acc)
                return


PROG = [line.strip().split() for line in open(FNAME, "r")]
part1(PROG)
part2(PROG)
