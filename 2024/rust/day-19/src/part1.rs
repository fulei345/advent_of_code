use cached::proc_macro::cached;

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut input = _input.trim().split("\n\n");
    let towels: Vec<&str> = input.next().unwrap().split(",").collect();
    let designs: Vec<&str> = input.next().unwrap().lines().collect::<Vec<&str>>();

    let towels: Vec<&str> = towels.iter().map(|towel| towel.trim()).collect();
    dbg!(&towels, &designs);

    let count = designs
        .iter()
        .filter(|design| validate_design(design, &towels))
        .count();

    Ok(count.to_string())
}

#[cached(key = "String", convert = r##"{ format!("{design}") }"##)]
fn validate_design(design: &str, towels: &[&str]) -> bool {
    return towels
        .iter()
        .map(|towel| {
            design
                .strip_prefix(*towel)
                .is_some_and(|input| input.is_empty() || validate_design(input, towels))
        })
        .any(|v| v);
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
        assert_eq!("6", process(input)?);
        Ok(())
    }
}
