use crate::{helpers::file_as_lines, Solution};

pub struct Day3 {
    grid: Vec<Vec<char>>,
    w: usize,
    h: usize,
}

impl Day3 {
    fn check_slope(&self, dx: usize, dy: usize) -> usize {
        let mut hits = 0;
        for step in 0..self.h + 1 {
            let (x, y) = (step * dx, step * dy);
            if self.grid[y % self.h][x % self.w] == '#' {
                hits += 1;
            }
            if y >= self.h {
                break;
            }
        }

        hits
    }
}

impl Solution for Day3 {
    fn new() -> Self {
        let grid: Vec<Vec<char>> = file_as_lines("../inputs/03.txt")
            .iter()
            .map(|l| l.chars().collect())
            .collect();
        let w = grid[0].len();
        let h = grid.len();

        Self { grid, w, h }
    }

    fn part1(&self) {
        println!("{}", self.check_slope(3, 1))
    }

    fn part2(&self) {
        let total: usize = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
            .iter()
            .map(|(dx, dy)| self.check_slope(*dx, *dy))
            .product();
        println!("{}", total);
    }
}
