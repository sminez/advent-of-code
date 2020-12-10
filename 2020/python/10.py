FNAME = "../inputs/10.txt"


def find_runs(nums):
    runs = []
    run = [0]
    for n in sorted(nums):
        if n - run[-1] == 1:
            run.append(n)
        else:
            if len(run) > 1:
                runs.append(run)
            run = [n]
    return runs


def variants(run):
    n_variants = {2: 1, 3: 2, 4: 4, 5: 7}
    return n_variants[len(run)]


def part1(nums):
    counts = {1: 0, 1: 0, 2: 0, 3: 1}
    current = 0
    for n in sorted(nums):
        counts[n - current] += 1
        current = n
    print(counts[1] * counts[3])


def part2(nums):
    total = 1
    for r in find_runs(nums):
        total *= variants(r)
    print(total)


NUMS = [int(line) for line in open(FNAME, "r")]
part1(NUMS)
part2(NUMS)
