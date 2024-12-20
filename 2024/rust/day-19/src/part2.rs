use cached::proc_macro::cached;

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut input = _input.trim().split("\n\n");
    let towels: Vec<&str> = input.next().unwrap().split(",").collect();
    let designs: Vec<&str> = input.next().unwrap().lines().collect::<Vec<&str>>();

    let towels: Vec<&str> = towels.iter().map(|towel| towel.trim()).collect();

    let count: usize = designs
        .iter()
        .map(|design| validate_design(design, &towels))
        .sum();

    Ok(count.to_string())
}

#[cached(key = "String", convert = r##"{ format!("{design}") }"##)]
fn validate_design(design: &str, towels: &[&str]) -> usize {
    return towels
        .iter()
        .filter_map(|towel| {
            if design.starts_with(*towel) {
                let new_design = &design[towel.len()..];
                if new_design.is_empty() {
                    return Some(1);
                }
                Some(validate_design(new_design, towels))
            } else {
                None
            }
        })
        .sum();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb";
        assert_eq!("16", process(input)?);
        Ok(())
    }
}
