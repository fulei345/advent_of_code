#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let result = itertools::fold(_input.lines(), 0, |a, line| {
        let mut parts = line.split(":");
        let total = parts.next().unwrap().parse::<usize>().unwrap();
        let numbers: Vec<usize> = parts
            .next()
            .unwrap()
            .trim()
            .split(" ")
            .map(|n| n.parse::<usize>().unwrap())
            .collect();

        let operations = [
            |a: usize, b: usize| -> usize { format!("{a}{b}").parse::<usize>().unwrap() },
            |a: usize, b: usize| -> usize { a * b },
            |a: usize, b: usize| -> usize { a + b },
        ];
        if check_line(&numbers, 0, &operations, total) {
            total + a
        } else {
            a
        }
    });

    Ok(result.to_string())
}

fn check_line(
    nums: &[usize],
    current_total: usize,
    operations: &[fn(usize, usize) -> usize],
    expected: usize,
) -> bool {
    if nums.is_empty() {
        return current_total == expected;
    }
    if current_total > expected {
        return false;
    }
    let a = current_total;
    let b = nums[0];
    for op in operations {
        let result = op(a, b);
        if check_line(&nums[1..], result, &operations, expected) {
            return true;
        }
    }
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20";
        assert_eq!("11387", process(input)?);
        Ok(())
    }
}
