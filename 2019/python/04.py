LOWER = 273_025
UPPER = 767_253


def has_double(s):
    for offset in range(5):
        if s[offset] == s[offset + 1]:
            return True
    return False


def has_double_not_more(s):
    digits = list(s)
    k = digits[0]
    size = 1

    for d in digits[1:]:
        if d == k:
            size += 1
        else:
            if size == 2:
                return True
            k = d
            size = 1

    return size == 2


def is_always_increasing(s):
    digits = [int(d) for d in s]
    k = 0
    for d in digits:
        if d < k:
            return False
        k = d
    return True


def check_range(lower, upper, part=1):
    viable = []
    double_check = has_double if part == 1 else has_double_not_more

    for n in range(lower, upper + 1):
        s = str(n)
        if double_check(s) and is_always_increasing(s):
            viable.append(n)

    print(f"Found {len(viable)} candidates for part {part}")


if __name__ == "__main__":
    s1 = "111111"
    assert has_double(s1) and is_always_increasing(s1) is True
    s2 = "223450"
    assert has_double(s2) is True
    assert is_always_increasing(s2) is False
    s3 = "123789"
    assert has_double(s3) is False
    assert is_always_increasing(s3) is True
    s4 = "123444"
    assert has_double(s4) is True
    assert has_double_not_more(s4) is False
    s5 = "111122"
    assert has_double(s5) is True
    assert has_double_not_more(s5) is True

    check_range(LOWER, UPPER, part=1)
    check_range(LOWER, UPPER, part=2)
