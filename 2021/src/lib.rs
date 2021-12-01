use anyhow::Result;

pub mod day01;

pub fn input_as_ints(input: &'static str) -> Result<impl Iterator<Item = i32>> {
    Ok(input
        .split_whitespace()
        .filter(|s| !s.is_empty())
        .map(|s: &str| s.parse().expect("invalid numeric line")))
}
