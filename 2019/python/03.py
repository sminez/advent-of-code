def manhattan_distance(dx, dy):
    return abs(dx) + abs(dy)


class PathMapper:
    def __init__(self, path_str1, path_str2):
        self._path_strs = [path_str1, path_str2]
        self._path_points = []

        self._generate_path_point_sets()

    def _generate_path_point_sets(self):
        paths = []

        for path_str in self._path_strs:
            path = [(0, 0)]

            for step in path_str.split(","):
                x, y = path[-1]
                direction, length = step[0], int(step[1:])

                if direction == "R":
                    path.extend((x, y + dy) for dy in range(1, length + 1))
                elif direction == "L":
                    path.extend((x, y - dy) for dy in range(1, length + 1))
                elif direction == "U":
                    path.extend((x + dx, y) for dx in range(1, length + 1))
                elif direction == "D":
                    path.extend((x - dx, y) for dx in range(1, length + 1))
                else:
                    raise ValueError(f"Invalid direction: {direction}")

            paths.append(path)

        self._path_points = paths

    def locate_intersections(self):
        point_set_1 = set(self._path_points[0])
        point_set_2 = set(self._path_points[1])
        return [p for p in point_set_1 if p in point_set_2 and p != (0, 0)]

    def locate_minimal_intersection(self):
        intersections = self.locate_intersections()
        return min([manhattan_distance(*i) for i in intersections])

    def locate_minimal_steps(self):
        intersections = self.locate_intersections()
        min_steps = None

        for i in intersections:
            s1 = self._path_points[0].index(i)
            s2 = self._path_points[1].index(i)

            steps = s1 + s2

            if min_steps is None:
                min_steps = steps
            elif steps < min_steps:
                min_steps = steps

        return min_steps


if __name__ == "__main__":
    examples = [
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83", 159, 610),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
            410,
        ),
    ]

    for (p1, p2, length, _) in examples:
        mapper = PathMapper(p1, p2)
        minimal = mapper.locate_minimal_intersection()
        if length != minimal:
            raise ValueError(f"Failed test cases: {length} != {minimal}")

    for (p1, p2, _, steps) in examples:
        mapper = PathMapper(p1, p2)
        minimal = mapper.locate_minimal_steps()
        if steps != minimal:
            raise ValueError(f"Failed test cases: {steps} != {minimal}")

    part = 2

    with open("../inputs/03.txt", "r") as f:
        p1, p2 = f.readlines()

    print("mapping paths...")
    mapper = PathMapper(p1, p2)

    if part == 1:
        print("finding intersections...")
        print(mapper.locate_minimal_intersection())
    elif part == 2:
        print("finding steps...")
        print(mapper.locate_minimal_steps())
