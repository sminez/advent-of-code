FNAME = "../inputs/03.txt"


def check_slope(grid, dx, dy):
    w, h = len(grid[0]), len(grid)
    hits = 0

    for step in range(0, h + 1):
        x, y = (step * dx, step * dy)

        if grid[y % h][x % w] == "#":
            hits += 1

        if y >= h:
            break

    return hits


def part1(grid):
    print(check_slope(grid, 3, 1))


def part2(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1

    for (dx, dy) in slopes:
        total *= check_slope(grid, dx, dy)
    print(total)


GRID = [list(line.strip()) for line in open(FNAME, "r")]
part1(GRID)
part2(GRID)
