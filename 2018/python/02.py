import sys
from collections import Counter


def id_to_twos_and_threes(ID):
    counts = Counter(ID).values()
    has_two = 2 in counts
    has_three = 3 in counts

    return has_two, has_three


def ids_differ_by_single_char(id_1, id_2):
    has_mismatch = False

    for ix in range(len(id_1)):
        if id_1[ix] != id_2[ix]:
            if has_mismatch:
                return False

            has_mismatch = True

    return True


if __name__ == "__main__":
    with open("../inputs/02.txt", "r") as f:
        box_ids = [line.strip() for line in f]

    part = 2

    if part == 1:
        twos = 0
        threes = 0

        for box_id in box_ids:
            has_two, has_three = id_to_twos_and_threes(box_id)

            if has_two:
                twos += 1
            if has_three:
                threes += 1

        checksum = twos * threes
        print(checksum)

    else:
        for ix, box_id in enumerate(box_ids):
            for candidate in box_ids[ix + 1 :]:
                if ids_differ_by_single_char(box_id, candidate):
                    print(box_id)
                    print(candidate)
                    sys.exit()
