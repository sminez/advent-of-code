FNAME = "../inputs/11.txt"

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"


def seat_map():
    seats = {}
    for y, line in enumerate(open(FNAME, "r")):
        for x, char in enumerate(line.strip()):
            if char != FLOOR:
                seats[(x, y)] = char
    return seats, x, y


def occupied_neighbours(seats, loc, x_max, y_max, only_adjacent=True):
    x, y = loc
    count = 0
    for dx in [0, 1, -1]:
        for dy in [0, 1, -1]:
            if dx == dy == 0:
                continue

            state, k = None, 1
            while state is None:
                X, Y = x + k * dx, y + k * dy
                if 0 <= X <= x_max and 0 <= Y <= y_max:
                    state = seats.get((X, Y))
                    if only_adjacent:
                        break
                    k += 1
                else:
                    state = FLOOR

            if state == OCCUPIED:
                count += 1
    return count


def stabilise(threshold, only_adjacent=True):
    seats, x_max, y_max = seat_map()
    iterations = 0
    while True:
        new_seats = {}
        for loc, state in seats.items():
            neighbours = occupied_neighbours(seats, loc, x_max, y_max, only_adjacent)
            if state == EMPTY and neighbours == 0:
                new_seats[loc] = OCCUPIED
            elif state == OCCUPIED and neighbours >= threshold:
                new_seats[loc] = EMPTY
            else:
                new_seats[loc] = state
        if new_seats == seats:
            break
        else:
            seats = new_seats
            iterations += 1
    print(f"Took {iterations} iterations to stabilise")
    print(len([s for s in seats.values() if s == OCCUPIED]))


def part1():
    stabilise(threshold=4, only_adjacent=True)


def part2():
    stabilise(threshold=5, only_adjacent=False)


part1()
part2()
