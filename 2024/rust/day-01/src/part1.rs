#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut left_list: Vec<i32> = vec![];
    let mut right_list: Vec<i32> = vec![];

    for line in _input.lines(){
        let numbers = line.split_whitespace().map(|nums|nums.parse::<i32>().unwrap()).collect::<Vec<i32>>();
        left_list.push(numbers[0]);
        right_list.push(numbers[1])
    }

    left_list.sort();
    right_list.sort();

    let result: i32 = std::iter::zip(left_list, right_list)
        .map(|(l, r)| (l - r).abs())
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
        assert_eq!("11", process(input)?);
        Ok(())
    }
}
