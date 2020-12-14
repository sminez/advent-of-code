FNAME = "../inputs/12.txt"
DIRS = ["N", "E", "S", "W"]
TEST = """F10
N3
F7
R90
F11"""


def part1(instructions):
    def step(direction, position, instruction):
        cmd, val = instruction
        x, y = position
        if cmd in "LR":
            val = -val if cmd == "L" else val
            direction = DIRS[(DIRS.index(direction) + val // 90) % 4]
        else:
            cmd = direction if cmd == "F" else cmd
            if cmd == "N":
                y += val
            elif cmd == "E":
                x += val
            elif cmd == "S":
                y -= val
            elif cmd == "W":
                x -= val
        return direction, (x, y)

    direction, position = "E", (0, 0)
    for i in instructions:
        # print(direction, position)
        direction, position = step(direction, position, i)

    print(direction, position, abs(position[0]) + abs(position[1]))


def part2(instructions):
    def step(ship, waypoint, instruction):
        cmd, val = instruction
        x, y = waypoint
        if cmd in "LR":
            if val == 90:
                return ship, (y, -x) if cmd == "R" else (-y, x)
            elif val == 180:
                return ship, (-x, -y)
            elif val == 270:
                return ship, (y, -x) if cmd == "L" else (-y, x)
        elif cmd == "F":
            return (ship[0] + x * val, ship[1] + y * val), waypoint
        else:
            if cmd == "N":
                y += val
            elif cmd == "E":
                x += val
            elif cmd == "S":
                y -= val
            elif cmd == "W":
                x -= val
        return ship, (x, y)

    ship, waypoint = (0, 0), (10, 1)
    for i in instructions:
        # print(ship, waypoint)
        ship, waypoint = step(ship, waypoint, i)

    print(ship, waypoint, abs(ship[0]) + abs(ship[1]))


INSTRUCTIONS = [(line[0], int(line[1:])) for line in open(FNAME, "r")]
# INSTRUCTIONS = [(line[0], int(line[1:])) for line in TEST.split()]
part1(INSTRUCTIONS)
part2(INSTRUCTIONS)
