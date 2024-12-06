use std::collections::HashMap;

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut left: Vec<usize> = vec![];
    let mut right: HashMap<usize, usize> = HashMap::new();

    // Put the right side into a hashmap when we are parsing it
    for line in _input.lines(){
        let numbers = line.split_whitespace()
            .map(|nums|nums
            .parse::<usize>()
            .unwrap())
        .collect::<Vec<usize>>();
        left.push(numbers[0]);
        right.entry(numbers[1]).and_modify(|count| *count += 1).or_insert(1);
    }

    let result: usize = left
        .iter()
        .map(|number| {
            number * right.get(number).unwrap_or(&0)
        })
        .sum();

    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "3   4
4   3
2   5
1   3
3   9
3   3";
        assert_eq!("31", process(input)?);
        Ok(())
    }
}
