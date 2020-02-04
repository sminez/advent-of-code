def get_fuel(mass):
    return mass // 3 - 2


def get_total_fuel(mass):
    fuel = get_fuel(mass)
    total = 0

    while fuel > 0:
        total += fuel
        fuel = get_fuel(fuel)

    return total


if __name__ == "__main__":
    total = 0
    part = 2

    with open("../inputs/01.txt", "r") as f:
        for line in f:
            mass = int(line.strip())
            if part == 1:
                total += get_fuel(mass)
            else:
                total += get_total_fuel(mass)

    print(total)
