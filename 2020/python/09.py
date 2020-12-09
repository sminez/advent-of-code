FNAME = "../inputs/09.txt"


def first_invalid(nums, preamble):
    head = nums[:preamble]
    for n in nums[preamble:]:
        valid = any(n - k in head and (n - k) != k for k in head)
        if not valid:
            return n
        head = head[1:] + [n]


def part1(nums):
    print(first_invalid(nums, 25))


def part2(nums):
    invalid = first_invalid(nums, 25)
    i = 1

    while True:
        for n in range(i, len(nums)):
            r = nums[i:n]
            total = sum(r)

            if total == invalid:
                print(r)
                print(max(r) + min(r))
                return
            elif total > invalid:
                i += 1
                break


NUMS = [int(line) for line in open(FNAME, "r")]
part1(NUMS)
part2(NUMS)
