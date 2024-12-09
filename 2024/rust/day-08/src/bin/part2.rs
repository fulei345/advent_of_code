use day_08::part2::process;
use miette::Context;

#[tracing::instrument]
fn main() -> miette::Result<()> {
    tracing_subscriber::fmt::init();

    let file = include_str!("../../../../../aoc_inputs/2024/day08input");
    let result = process(file).context("process part 2")?;
    println!("{}", result);
    Ok(())
}
