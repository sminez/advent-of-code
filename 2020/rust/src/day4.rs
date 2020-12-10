use crate::{helpers::file_as_blocks, Solution};
use std::collections::HashMap;

const REQUIRED_FIELDS: &[&str] = &["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

pub struct Day4 {
    passports: Vec<HashMap<String, String>>,
}

impl Solution for Day4 {
    fn new() -> Self {
        let passports = file_as_blocks("../inputs/04.txt", "\n\n")
            .iter()
            .map(|block| {
                block
                    .iter()
                    .map(|line| {
                        let mut parts = line.split(':').map(|s| s.to_string());
                        (parts.next().unwrap(), parts.next().unwrap())
                    })
                    .collect()
            })
            .collect();

        Self { passports }
    }

    fn part1(&self) {}

    fn part2(&self) {}
}
