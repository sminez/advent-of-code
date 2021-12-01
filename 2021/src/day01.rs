use crate::{input_as_ints, split_off};
use anyhow::Result;

const INPUT: &str = include_str!("../input/01.txt");

pub fn part1() -> Result<()> {
    let iter = input_as_ints(INPUT);
    let count = compare_lines(iter);
    println!("Number of increases: {}", count);

    Ok(())
}

pub fn part2() -> Result<()> {
    let iter = input_as_ints(INPUT);
    let count = compare_blocks(iter);
    println!("Number of increases: {}", count);

    Ok(())
}

fn compare_lines(mut iter: impl Iterator<Item = i32>) -> i32 {
    let mut prev = iter.next().unwrap();
    let mut count = 0;

    for line in iter {
        if line > prev {
            count += 1;
        }

        prev = line;
    }

    count
}

fn compare_blocks(mut iter: impl Iterator<Item = i32>) -> i32 {
    let ns = split_off(&mut iter, 3);
    let (mut first, mut second, mut third) = (ns[0], ns[1], ns[2]);
    let mut prev = first + second + third;
    let mut count = 0;

    for current in iter {
        first = second;
        second = third;
        third = current;

        let total = first + second + third;

        if total > prev {
            count += 1;
        }

        prev = total;
    }

    count
}

#[cfg(test)]
mod tests {
    use super::*;

    const DATA: [i32; 10] = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];

    #[test]
    fn part_1_example() {
        assert_eq!(compare_lines(DATA.into_iter()), 7);
    }

    #[test]
    fn part_2_example() {
        assert_eq!(compare_blocks(DATA.into_iter()), 5);
    }
}
