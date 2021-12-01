use anyhow::Result;
use aoc2021::input_as_lines;

fn main() -> anyhow::Result<()> {
    let lines = input_as_lines("01")?
        .iter()
        .map(|line| Ok(line.parse()?))
        .collect::<Result<Vec<u32>>>()?;

    let mut prev = lines[0];
    let mut count = 0;

    for &line in lines[1..].iter() {
        if line > prev {
            count += 1;
        }

        prev = line;
    }

    println!("Number of increases: {}", count);

    Ok(())
}
