#[derive(Debug)]
pub enum ParamMode {
    Position,
    Immediate,
}

#[derive(Debug)]
pub struct Param {
    mode: ParamMode,
    value: i8,
}
