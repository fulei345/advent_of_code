use {{crate_name}}::part1::process;
use miette::Context;

#[tracing::instrument]
fn main() -> miette::Result<()> {
    tracing_subscriber::fmt::init();

    let file = include_str!("../../../../../aoc_inputs/2024/day01input.txt");
    let result = process(file).context("process part 1")?;
    println!("{}", result);
    Ok(())
}