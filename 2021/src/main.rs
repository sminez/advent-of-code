use aoc2021::*;
use std::env;

fn parse_args() -> anyhow::Result<(usize, usize)> {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        return Err(anyhow::anyhow!("need to give day and part"));
    }

    Ok((args[1].parse()?, args[2].parse()?))
}

fn main() -> anyhow::Result<()> {
    match parse_args()? {
        (1, 1) => day01::part1(),
        (1, 2) => day01::part2(),
        (2, 1) => day02::part1(),
        (2, 2) => day02::part2(),
        (day, part) => Err(anyhow::anyhow!("Unknown day/part: {}/{}", day, part)),
    }
}
