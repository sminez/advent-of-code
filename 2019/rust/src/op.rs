use std::fmt;

#[derive(Hash, Eq, PartialEq, Debug)]
pub enum OpCode {
    ADD,
    MUL,
    PUT,
    GET,
    END,
}

impl OpCode {
    pub fn try_from_u8(i: u8) -> Result<OpCode, String> {
        match i {
            1 => Ok(OpCode::ADD),
            2 => Ok(OpCode::MUL),
            3 => Ok(OpCode::PUT),
            4 => Ok(OpCode::GET),
            99 => Ok(OpCode::END),
            _ => Err(String::from(format!("Unknown OpCode {}", i))),
        }
    }
}

pub enum Op {
    Unary(Box<dyn Fn(usize, &mut Vec<i8>)>),
    Binary(Box<dyn Fn(i8, i8, usize, &mut Vec<i8>)>),
}

impl fmt::Debug for Op {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            Op::Unary(_) => write!(f, "Unary"),
            Op::Binary(_) => write!(f, "Binary"),
        }
    }
}

impl Op {
    pub fn n_params(&self) -> u8 {
        match *self {
            Op::Unary(_) => 1,
            Op::Binary(_) => 3,
        }
    }
}
