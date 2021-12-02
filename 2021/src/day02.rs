use crate::line_iter;
use anyhow::Result;

const INPUT: &str = include_str!("../input/02.txt");

pub fn part1() -> Result<()> {
    let (h, d) = run_simple(INPUT)?;

    println!("h: {}, d: {}, hxd: {}", h, d, h * d);
    Ok(())
}

pub fn part2() -> Result<()> {
    let (h, d) = run_with_aim(INPUT)?;

    println!("h: {}, d: {}, hxd: {}", h, d, h * d);
    Ok(())
}

fn run_simple(input: &'static str) -> Result<(i32, i32)> {
    let mut h = 0;
    let mut d = 0;

    for line in line_iter(input) {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let n: i32 = parts[1].parse()?;

        match parts[0] {
            "down" => d += n,
            "up" => d -= n,
            "forward" => h += n,
            _ => anyhow::bail!("invalid input: {}", line),
        }
    }

    Ok((h, d))
}

fn run_with_aim(input: &'static str) -> Result<(i32, i32)> {
    let mut aim = 0;
    let mut h = 0;
    let mut d = 0;

    for line in line_iter(input) {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let n: i32 = parts[1].parse()?;

        match parts[0] {
            "down" => aim += n,
            "up" => aim -= n,
            "forward" => {
                h += n;
                d += aim * n;
            }
            _ => anyhow::bail!("invalid input: {}", line),
        }
    }

    Ok((h, d))
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = r"
forward 5
down 5
forward 8
up 3
down 8
forward 2
";

    #[test]
    fn part1_example() {
        assert_eq!(run_simple(TEST_INPUT).unwrap(), (15, 10));
    }

    #[test]
    fn part2_example() {
        assert_eq!(run_with_aim(TEST_INPUT).unwrap(), (15, 60));
    }
}
