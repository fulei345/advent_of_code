use day_07::*;

fn main() {
    // Run registered benchmarks.
    divan::main();
}

#[divan::bench]
fn part1() {
    part1::process(divan::black_box(include_str!(
        "../../../../aoc_inputs/2024/day07input",
    )))
    .unwrap();
}

#[divan::bench]
fn part2() {
    part2::process(divan::black_box(include_str!(
        "../../../../aoc_inputs/2024/day07input",
    )))
    .unwrap();
}

#[divan::bench]
fn part2_backwards() {
    part2_backwards::process(divan::black_box(include_str!(
        "../../../../aoc_inputs/2024/day07input",
    )))
    .unwrap();
}
