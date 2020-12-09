use crate::{helpers::file_as_lines, Solution};

struct Parsed {
    n: usize,
    m: usize,
    c: char,
    pass: String,
}

impl Parsed {
    fn new(line: &str) -> Self {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let nums: Vec<usize> = parts[0]
            .split('-')
            .map(|s| s.parse::<usize>().unwrap())
            .collect();

        Self {
            n: nums[0],
            m: nums[1],
            c: parts[1].chars().next().unwrap(),
            pass: parts[2].into(),
        }
    }
}

pub struct Day2 {
    values: Vec<Parsed>,
}

impl Solution for Day2 {
    fn new() -> Self {
        Self {
            values: file_as_lines("../inputs/02.txt")
                .iter()
                .map(|line| Parsed::new(line))
                .collect(),
        }
    }

    fn part1(&self) {
        let n_valid = self
            .values
            .iter()
            .filter(|p| {
                let n_chars = p.pass.chars().filter(|&c| c == p.c).count();
                p.n <= n_chars && n_chars <= p.m
            })
            .count();

        println!("{}", n_valid);
    }

    fn part2(&self) {
        let n_valid = self
            .values
            .iter()
            .filter(|p| {
                let c1 = p.pass.chars().nth(p.n - 1).unwrap();
                let c2 = p.pass.chars().nth(p.m - 1).unwrap();
                (c1 == p.c) ^ (c2 == p.c)
            })
            .count();

        println!("{}", n_valid);
    }
}
