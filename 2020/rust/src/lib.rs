pub mod day1;
pub mod day2;
pub mod day3;
pub mod day4;

pub trait Solution {
    fn new() -> Self;
    fn part1(&self);
    fn part2(&self);

    fn run(&self) {
        println!("\n-- PART 1 --");
        self.part1();
        println!("\n-- PART 2 --");
        self.part2();
    }
}

pub mod helpers {
    use std::{collections::HashSet, fs::File, io::Read};

    pub fn file_as_lines(fname: &str) -> Vec<String> {
        let mut file = File::open(fname).unwrap();
        let mut s = String::new();
        file.read_to_string(&mut s).expect("failed to read");
        s.split('\n')
            .filter(|s| !s.is_empty())
            .map(|s: &str| s.into())
            .collect()
    }

    pub fn file_as_blocks(fname: &str, delimiter: &str) -> Vec<Vec<String>> {
        let mut file = File::open(fname).unwrap();
        let mut s = String::new();
        file.read_to_string(&mut s).expect("failed to read");
        s.split(delimiter)
            .map(|s| s.split('\n').map(|s| s.to_string()).collect())
            .collect()
    }

    pub fn intersection<T: Eq + Copy + std::hash::Hash>(a: &[T], b: &[T]) -> Vec<T> {
        a.iter()
            .collect::<HashSet<_>>()
            .intersection(&b.iter().collect())
            .map(|&n| *n)
            .collect()
    }
}
