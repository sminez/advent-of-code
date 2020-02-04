from operator import add, mul
from copy import copy

# opcodes
ADD = 1
MUL = 2
PUT = 3
GET = 4
END = 99
KNOWN_OPS = {ADD: 4, MUL: 4, PUT: 3, GET: 3, END: 0}

# parameter modes
POSITION = 0
IMMEDIATE = 1


class OpCodeError(Exception):
    pass


class IntcodeComputer:
    _op_map = {ADD: add, MUL: mul}

    def __init__(self, program):
        self._initial_program = program
        self._program = copy(program)
        self._instruction_pointer = 0
        self._complete = False

    @property
    def result(self):
        if not self._complete:
            raise OpCodeError("Program is not complete")
        return self._program[0]

    def reset(self):
        self._program = copy(self._initial_program)
        self._instruction_pointer = 0
        self._complete = False

    def override(self, loc, val):
        self._program[loc] = val

    def run_next_opcode(self):
        if self._complete:
            raise OpCodeError("Program is already complete")

        op_block = self._program[self._instruction_pointer]
        op, params = self.parse_op_block(op_block)

        if op == END:
            self._complete = True
            return

        op(*params, self._program)
        self._instruction_pointer += len(params) + 1

    def parse_op_block(self, op_block):
        s = str(op_block)
        op_code = int(s[-2:])
        n_params = KNOWN_OPS[op_code]
        param_modes = reversed([int(p) for p in s[:-2]])

        segment = self._program[self._instruction_pointer : self._instruction_pointer + n_params]
        param_modes = []
        params = []

        # need to pad right w. 0
        for mode, param in zip(param_modes, segment):
            if mode == POSITION:
                param = self._program[param]

            params.append(param)

        return op, params

    def run(self, debug=False):
        while not self._complete:
            self.run_next_opcode()

            if debug:
                print(self._program)

        return self.result
