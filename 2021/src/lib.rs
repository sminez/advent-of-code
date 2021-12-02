pub mod day01;
pub mod day02;

pub fn input_as_ints(input: &'static str) -> impl Iterator<Item = i32> {
    input
        .split_whitespace()
        .filter(|s| !s.is_empty())
        .map(|s: &str| s.parse().expect("invalid numeric line"))
}

pub fn split_off<T>(iter: &mut impl Iterator<Item = T>, n: usize) -> Vec<T> {
    let mut v = Vec::with_capacity(n);
    for _ in 0..n {
        v.push(iter.next().unwrap());
    }

    v
}
