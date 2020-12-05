FNAME = "../inputs/04.txt"
FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def has_required_fields(p):
    return FIELDS.intersection(p.keys()) == FIELDS


def has_valid_fields(p):
    def is_hex_code(s):
        hex_chars = "01234567789abcdef"
        return all([len(s) == 7, s[0] == "#", all([c in hex_chars for c in s[1:]])])

    def is_valid_height(s):
        if s[-2:] == "cm":
            return 150 <= int(s[:-2]) <= 193
        elif s[-2:] == "in":
            return 59 <= int(s[:-2]) <= 76
        return False

    return all(
        [
            1920 <= int(p["byr"]) <= 2002,
            2010 <= int(p["iyr"]) <= 2020,
            2020 <= int(p["eyr"]) <= 2030,
            is_valid_height(p["hgt"]),
            is_hex_code(p["hcl"]),
            p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            p["pid"].isnumeric() and len(p["pid"]) == 9,
        ]
    )


def part1(passports):
    print(len([p for p in passports if has_required_fields(p)]))


def part2(passports):
    print(len([p for p in passports if has_required_fields(p) and has_valid_fields(p)]))


with open(FNAME, "r") as f:
    BLOCKS = f.read().split("\n\n")
    PAIRS = [b.replace("\n", " ").split() for b in BLOCKS]
    PASSPORTS = [dict(field.split(":") for field in p) for p in PAIRS]

part1(PASSPORTS)
part2(PASSPORTS)
