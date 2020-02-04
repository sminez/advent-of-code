from dataclasses import dataclass


@dataclass
class Claim:
    ID: str
    dy: int
    dx: int
    w: int
    h: int

    @property
    def squares(self):
        s = set()

        for x in range(self.dx, self.dx + self.w):
            for y in range(self.dy, self.dy + self.h):
                s.add((x, y))

        return s

    def overlap(self, other):
        return self.squares.intersection(other.squares)


def parse_to_claim(line: str) -> Claim:
    """#123 @ 3,2: 5x4"""
    s_id, _, s_delta, s_dims = line.split()

    ID = s_id[1:]
    dy, dx = map(int, s_delta.strip(":").split(","))
    w, h = map(int, s_dims.split("x"))

    return Claim(ID, dy, dx, w, h)


if __name__ == "__main__":
    with open("../inputs/03.txt", "r") as f:
        claims = [parse_to_claim(line) for line in f]

    part = 1

    if part == 1:
        for c in claims:
            print(c)
