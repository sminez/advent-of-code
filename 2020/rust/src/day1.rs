use crate::{
    helpers::{file_as_lines, intersection},
    Solution,
};

fn get_compliments(values: &[isize], target: isize) -> Vec<isize> {
    values.iter().map(|n| target - n).collect()
}

pub struct Day1 {
    values: Vec<isize>,
}

impl Solution for Day1 {
    fn new() -> Self {
        Self {
            values: file_as_lines("../inputs/01.txt")
                .iter()
                .map(|s| s.parse().unwrap())
                .collect(),
        }
    }

    fn part1(&self) {
        let vals = intersection(&self.values, &get_compliments(&self.values, 2020));
        println!(
            "{} x {} = {}",
            vals[0],
            vals[1],
            vals.iter().product::<isize>()
        );
    }

    fn part2(&self) {
        for v in self.values.iter() {
            let vals = intersection(&self.values, &get_compliments(&self.values, 2020 - v));
            if !vals.is_empty() {
                println!(
                    "{} x {} x {} = {}",
                    v,
                    vals[0],
                    vals[1],
                    v * vals.iter().product::<isize>()
                );
                return;
            }
        }
    }
}
