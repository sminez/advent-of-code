from operator import add, mul
from copy import copy

ADD = 1
MUL = 2
END = 99
KNOWN_OPS = [ADD, MUL, END]


class OpCodeError(Exception):
    pass


class IntcodeComputer:
    _op_map = {ADD: add, MUL: mul}

    def __init__(self, program):
        self._initial_program = program
        self._program = copy(program)
        self._program_counter = 0
        self._complete = False

    @property
    def result(self):
        if not self._complete:
            raise OpCodeError("Program is not complete")
        return self._program[0]

    def reset(self):
        self._program = copy(self._initial_program)
        self._program_counter = 0
        self._complete = False

    def override(self, loc, val):
        self._program[loc] = val

    def run_next_opcode(self):
        if self._complete:
            raise OpCodeError("Program is already complete")

        segment = self._program[self._program_counter : self._program_counter + 4]
        op = segment[0]

        if op == END:
            self._complete = True
            return

        loc1, loc2, loc3 = segment[1:]
        arg1 = self._program[loc1]
        arg2 = self._program[loc2]

        try:
            op = self._op_map[op]
        except KeyError:
            raise OpCodeError(f"Unknown opcode: {op}")

        self._program[loc3] = op(arg1, arg2)
        self._program_counter += 4

    def run(self, debug=False):
        while not self._complete:
            self.run_next_opcode()

            if debug:
                print(self._program)

        return self.result


def test_case(prog, expected):
    comp = IntcodeComputer(prog)
    comp.run()

    assert comp._program == expected, f"Failing test case: {prog}"


if __name__ == "__main__":
    part = 2

    cases = [
        (
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ),
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ]
    for (prog, expected) in cases:
        test_case(prog, expected)

    with open("../inputs/02.txt", "r") as f:
        s = f.read().strip()
        prog = [int(c) for c in s.split(",")]

    if part == 1:
        # Restore grav assist -> 1202 program alarm
        prog[1] = 12
        prog[2] = 2

        comp = IntcodeComputer(prog)
        result = comp.run()
        print(result)

    else:
        target = 19_690_720
        comp = IntcodeComputer(prog)
        found = False

        for noun in range(100):
            for verb in range(100):
                comp.reset()
                comp.override(1, noun)
                comp.override(2, verb)
                try:
                    if comp.run() == target:
                        print(f"Target ({target}) found: noun={noun}, verb={verb}")
                        print(f"100 * noun + verb = {100 * noun + verb}")
                        found = True
                        break

                except OpCodeError:
                    # Invalid program
                    pass

            if found:
                break
