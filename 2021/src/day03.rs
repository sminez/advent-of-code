use anyhow::Result;

const INPUT: &str = include_str!("../input/03.txt");

pub fn part1() -> Result<()> {
    let (gamma, epsilon) = gamma_epsilon(INPUT)?;
    println!(
        "gamma: {}\nepsilon: {}\ngamma x epsilon: {}",
        gamma,
        epsilon,
        gamma * epsilon
    );

    Ok(())
}

pub fn part2() -> Result<()> {
    Ok(())
}

fn gamma_epsilon(input: &str) -> Result<(u32, u32)> {
    let n_bits = input.split_once('\n').unwrap().0.len();

    let lines = char_lines(input);
    let gamma_str: String = (0..n_bits)
        .into_iter()
        .map(|n| most_common(&lines, n, false))
        .collect();

    let epsilon_str: String = gamma_str
        .chars()
        .map(|c| if c == '0' { '1' } else { '0' })
        .collect();

    let gamma = u32::from_str_radix(&gamma_str, 2)?;
    let epsilon = u32::from_str_radix(&epsilon_str, 2)?;

    Ok((gamma, epsilon))
}

fn most_common(input: &[Vec<char>], index: usize, prefer_zero: bool) -> char {
    let count = input.iter().fold(0, |mut acc, chars| {
        if chars[index] == '0' {
            acc -= 1
        } else {
            acc += 1
        }
        acc
    });

    match count {
        n if n > 0 => '1',
        n if n < 0 => '0',
        0 if prefer_zero => '0',
        _ => '1',
    }
}

fn char_lines(input: &str) -> Vec<Vec<char>> {
    input
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = r"00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010";

    #[test]
    fn part1_example() {
        assert_eq!(gamma_epsilon(TEST_INPUT).unwrap(), (22, 9));
    }
}
