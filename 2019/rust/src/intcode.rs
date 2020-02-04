use super::op::{Op, OpCode};
use super::param::{Param, ParamMode};
use std::collections::HashMap;
use std::io;

#[derive(Debug)]
pub struct Instruction {
    op: Op,
    params: Vec<Param>,
    raw_params: Vec<i8>,
}

pub struct IntCodeComputer {
    known_ops: HashMap<OpCode, Op>,
    program: Vec<i8>,
    instruction_pointer: u8,
    current_instruction: Option<Instruction>,
}

impl IntCodeComputer {
    pub fn new() -> IntCodeComputer {
        let program = vec![];
        let instruction_pointer = 0;
        let mut known_ops = HashMap::new();
        let current_instruction = None;

        known_ops.insert(
            OpCode::ADD,
            Op::Binary(Box::new(|a, b, loc, prog| prog[loc] = a + b)),
        );
        known_ops.insert(
            OpCode::MUL,
            Op::Binary(Box::new(|a, b, loc, prog| prog[loc] = a * b)),
        );
        known_ops.insert(
            OpCode::PUT,
            Op::Unary(Box::new(|loc, prog| {
                let mut s = String::new();
                io::stdin()
                    .read_line(&mut s)
                    .expect("failed to read from stdin");
                let n: i8 = s.trim().parse().expect("expected an integer");
                prog[loc] = n;
            })),
        );
        known_ops.insert(
            OpCode::GET,
            Op::Unary(Box::new(|loc, prog| println!("OUTPUT: {}", prog[loc]))),
        );

        IntCodeComputer {
            program,
            instruction_pointer,
            known_ops,
            current_instruction,
        }
    }

    pub fn load_program(&mut self, program: Vec<i8>) {
        self.instruction_pointer = 0;
        self.program = program;
    }

    pub fn run(&mut self, debug: bool) {
        let mut complete = false;

        while !complete {
            self.get_next_instruction();

            if debug {
                println!("{:?}", self.current_instruction);
            }

            match self.current_instruction {}
            self.execute_current_instruction();
        }
    }

    fn get_next_instruction(&mut self) {}

    fn execute_current_instruction(&mut self) {}
}
