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
    let mut counts: Vec<isize> = vec![0; n_bits];

    for line in input.lines() {
        for (i, c) in line.char_indices() {
            if c == '0' {
                counts[i] -= 1;
            } else {
                counts[i] += 1;
            }
        }
    }

    let gamma = map_counts(&counts, |b| b > 0)?;
    let epsilon = map_counts(&counts, |b| b < 0)?;

    Ok((gamma, epsilon))
}

fn map_counts<F>(counts: &[isize], cond: F) -> Result<u32>
where
    F: Fn(isize) -> bool,
{
    let bits: String = counts
        .iter()
        .map(|&b| if cond(b) { '1' } else { '0' })
        .collect();

    Ok(u32::from_str_radix(&bits, 2)?)
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
